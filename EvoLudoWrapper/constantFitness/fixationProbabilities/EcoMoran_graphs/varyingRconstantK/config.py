from pathlib import Path

samples = 1000000
# deathrates=[0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8]
# deathrates = [0.2]
deathrates = [0.2,0.5,0.6]
min_r = 0.85
max_r = 2.5
step_r = 0.025
rs = []
current_r = min_r
while current_r <= max_r:
    
    if current_r+step_r >=1 and current_r<1:
        rs.append(round(current_r, 5))
        rs.append(0.99)
    elif current_r-step_r <=1 and current_r>1:
        rs.append(1.01)
        rs.append(round(current_r, 5))
    else:
        rs.append(round(current_r, 5))
    current_r += step_r
rs = [0.975,1,1.025,1.05,1.1,1.15,1.2,1.25,1.3,1.35,1.4,1.45,1.5,1.55,1.6,1.65,1.7,1.75,1.8,1.9,2]
# ,2.1,2.2,2.3,2.4,2.5,5,10,20,50]
# rs = [0.975,1,1.1,1.2,1.3,1.4,1.5,1.75,2,2.25,3,4,5,10]

# rs = [0.85,0.875,0.9,0.925,0.95,0.975,1,1.05,1.1,1.15,1.2,1.25,1.3,1.35,1.4,1.45,1.5,1.55,1.6,1.65,1.7,1.75,1.8,1.85,1.9,1.95,2]
ks= [3,4,6,8]
fs= [3,4,6,8]
# ks= [3,10]
# Ms=[400,800]
K=100
timerelax=10
graphs=[
    {"code":"r","name":"Regular","pop_size":None,"comparison_graphs" : []},
    # {"code":"M","name":"Well-mixed","pop_size":None,"comparison_graphs" : []},
 # # {"code":"+","name":"Strong amplifier","pop_size":686,"comparison_graphs" : [{"code":"r","name":"Regular","match":"K"},{"code":"M","name":"Well-mixed","match":"K"}]},
        # # {"code":"-","name":"Strong suppressor","pop_size":117,"comparison_graphs" : [{"code":"r","name":"Regular","match":"K"},{"code":"M","name":"Well-mixed","match":"K"}]},
        {"code":"n","name":"von Neumann square lattice","pop_size":None,"comparison_graphs" : []},
        {"code":"m","name":"Moore square lattice","pop_size":None,"comparison_graphs" : []},
        # {"code":"w","name": "Wheel","pop_size":100,"comparison_graphs" : [{"code":"r","name":"Regular","match":"K"},{"code":"M","name":"Well-mixed","match":"K"}]},
        # {"code":"f","name":"Scale free av.deg. ","pop_size":None,"comparison_graphs" : [{"code":"r","name":"Regular","match":"K"},{"code":"M","name":"Well-mixed","match":"K"}]},
        {"code":"f","name":"Scale free av.deg. ","pop_size":None,"comparison_graphs" : []},
        # {"code":"F","name":"K-E Scale free av.deg. ","pop_size":None,"comparison_graphs" : []},
        # {"code":"s","name":"Star","pop_size":300,"comparison_graphs" : [{"code":"r","name":"Regular","match":"K"},{"code":"M","name":"Well-mixed","match":"K"}]}
        # {"code":"s","name":"Star","pop_size":100,"comparison_graphs" : [{"code":"r","name":"Regular","match":"K"},{"code":"M","name":"Well-mixed","match":"K"}]}
]
folder_loc = Path(__file__).parent.resolve()
results_loc = str(folder_loc / 'results') + '/'