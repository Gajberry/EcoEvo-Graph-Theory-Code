from pathlib import Path

samples = 500#00000#00000#0000
timestop = 100000#
deathrates = [0.45,0.5,0.55]
rs =[1,1.1,1.2]
ks= [3,6,12]
timerelax=10
graphs=[
    {"code":f"r{k}","name":f"{k} Regular","comparison_graphs" : []} for k in ks
]
folder_loc = Path(__file__).parent.resolve()
results_loc = str(folder_loc / 'results') + '/'