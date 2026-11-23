from pathlib import Path

samples=1000#0#0#0
# deathrates=[0.2]#,0.5]
deathrates = [0.2]
# ks = [4]
# ks = [4,6,8,12]
ks = [3,4,6,8,12]
# ks = [4,8]
#K=98 # for m 0.5
# K=93 # for n 0.5
# K=95 # for n 0.2
K=100
timerelax=10
graphs=[
    {"code":"M","name":"Well-mixed"}]+[
    {"code":f"r{k}","name":f"{k}-Regular"} for k in ks]+[
    {"code":"n","name":"von Neumann square lattice","equivalent_k":4},
    {"code":"m","name":"Moore square lattice","equivalent_k":8},
    # # {"code":"+","name":"Strong amplifier"},
    # # {"code":"-","name":"Strong suppressor"},
    {"code":"f3","name":"Scale free av.deg. 3"},
    {"code":"f4","name":"Scale free av.deg. 4","equivalent_k":4},
    {"code":"f6","name":"Scale free av.deg. 6"},
    {"code":"f8","name":"Scale free av.deg. 8"},
    {"code":"f12","name":"Scale free av.deg. 8"},
    
]
folder_loc = Path(__file__).parent.resolve()
results_loc = str(folder_loc / 'results') + '/'