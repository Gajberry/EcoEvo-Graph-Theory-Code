# EcoEvo Graph Theory Code

Code and data for generating publication figures. The notebooks are organized
by model and use the `results` folders alongside them. Shared population-size
data is in `pop_sizes`.

Run notebooks with their own directory as the working directory. Analysis
notebooks use the existing results; generation notebooks create missing results.
Some extended numerical calculations can take a long time.

GenAI was used to aggregate notebooks from multiple files, organise folder structure, and for creating code to generate figures.

## EvoLudo JAR configuration

EvoLudo simulation notebooks require Java and the appropriate EvoLudo JAR files.
Set the following environment variables to the full paths of the JAR files you
need **before starting Jupyter**:

```sh
export SIM_EMORAN_JAR="/path/to/simEMoran.jar"
export SIM_EMORAN_FIX_JAR="/path/to/simEMoranFix.jar"
export EVOLUDO_JAR="/path/to/EvoLudo.jar"
```

Only the variables used by the notebook being run need to be set. Alternatively,
set them in a notebook with `os.environ` before running its simulation cells.
JAR files are not included in this repository.

The included result data occupies several gigabytes. The extended
`NonEvoludo` analysis requires its corresponding generated result files.
