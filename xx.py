import babay

data = []
for name in dir(babay):
    if name.startswith('resolve_'):
        print(name)
        data.append(name)

for i in data:
    print(babay.__dict__[f'{i}'])