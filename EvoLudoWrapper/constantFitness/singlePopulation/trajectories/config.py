from pathlib import Path

timestop=5000#0#00
repeats = 10#500
relaxation=0
r=1
single_d = 0.1
deathrates=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8]
# ks= [3,4,5,6,7,8,9]
ks= [4]
K=100
single_N=1000
Ns = [25,50,100,150,200,250,300,350,400]
timerelax=10
graphs=[
    {"code":f"r{k}","name":"Regular"} for k in ks]+[
# graphs = [
    {"code":"M","name":"Well-mixed"},
    # {"code":"n","name":"von Neumann square lattice"},
    # {"code":"m","name":"Moore square lattice"},
    # # {"code":"+","name":"Strong amplifier"},
    # # {"code":"-","name":"Strong suppressor"},
    # {"code":"f3","name":"Scale free av.deg. 3"},
    # {"code":"f4","name":"Scale free av.deg. 4"},
    # {"code":"f6","name":"Scale free av.deg. 6"},
    # {"code":"f8","name":"Scale free av.deg. 8"}
]
folder_loc = Path(__file__).parent.resolve()
results_loc = str(folder_loc) + '/results/'