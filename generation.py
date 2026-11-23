import os
from pathlib import Path
import subprocess
import tempfile

def generate_arguments_string(arguments_dict):
    """Build Java argument tokens from option names and their values.

    Use None for a flag and a tuple or list for options with multiple values.
    """
    arguments = []
    for key, value in arguments_dict.items():
        arguments.append(f"--{key}")
        if isinstance(value, (tuple, list)):
            arguments.extend(str(part) for part in value)
        elif value is not None:
            arguments.append(str(value))
    return arguments


def run_simulation(results_loc, output_name, jar_env, arguments):
    """Run a simulation using a JAR path or the name of an environment variable."""
    destination = Path(results_loc) / f"{output_name}.txt"
    if destination.exists():
        print(f"Already exists: {destination}")
        return

    jar_spec = os.fspath(jar_env)
    if isinstance(jar_env, os.PathLike) or "/" in jar_spec or jar_spec.endswith(".jar"):
        jar_value = jar_spec
    else:
        jar_value = os.environ.get(jar_spec)
        if not jar_value:
            raise RuntimeError(
                f"Set the environment variable {jar_spec} to the EvoLudo JAR path, "
                "or pass the JAR path directly."
            )
    jar = Path(jar_value).expanduser().resolve()
    if not jar.is_file():
        raise FileNotFoundError(f"EvoLudo JAR not found: {jar}")

    destination.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=".evoludo-", dir=destination.parent) as temp:
        output = Path(temp) / destination.name
        command = ["java", "-jar", str(jar), *map(str, arguments), "--output", output.name]
        subprocess.run(command, cwd=temp, check=True)
        if not output.is_file():
            raise FileNotFoundError(f"Simulation did not create {output.name}")
        os.link(output, destination)
    print(f"Generated: {destination}")
