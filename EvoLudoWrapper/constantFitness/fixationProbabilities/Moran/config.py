from pathlib import Path

samples = 1000000
r=2
ks= range(3,21)
# rs = [1.2,1.4,1.6,1.8,2]
rs = [2]
graphs=[
    {"code":"r","name":"Regular","pop_size":30,"updates":["Bd","dB"],"comparison_graphs" : [{"code":"M","name":"Well-mixed","updates":["Bd","dB"]}]},
        # {"code":"s","name":"Star","pop_size":30,"updates":["Bd","dB"],"comparison_graphs" : []},
        # {"code":"-","name":"Strong suppressor","pop_size":117,"comparison_graphs" : [{"code":"r","name":"Regular"}]},
        # {"code":"n","name":"von Neumann square lattice","pop_size":(None,4),"comparison_graphs" : [{"code":"r","name":"Regular"}]},
        # {"code":"m","name":"Moore square lattice","pop_size":(None,8),"comparison_graphs" : [{"code":"r","name":"Regular"}]},
        # {"code":"w","name": "Wheel","pop_size":200,"comparison_graphs" : [{"code":"r","name":"Regular"}]},
        # {"code":"f2","name":"Scale free av.deg. 2","pop_size":100,"comparison_graphs" : [{"code":"r","name":"Regular"}]},
        # {"code":"f4","name":"Scale free av.deg. 4","pop_size":100,"comparison_graphs" : []},
        # {"code":"f6","name":"Scale free av.deg. 6","pop_size":100,"comparison_graphs" : []},
        # {"code":"f8","name":"Scale free av.deg. 8","pop_size":100,"comparison_graphs" : []}
]
folder_loc = Path(__file__).parent.resolve()
results_loc = str(folder_loc / 'results') + '/'