from pathlib import Path

timestop=10000
relaxation=100
r=2
single_d = 0.1
deathrates=[0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8]
ks= [3]
K=30
single_N=1000
Ns = [25,50,100,150,200,250,300,350,400]
timerelax=10
graphs=[{"code":f"r{k}","name":"Regular"} for k in ks]+[
    {"code":"M","name":"Well-mixed"}
]
folder_loc = Path(__file__).parent.resolve()
results_loc = str(folder_loc / 'results') + '/'