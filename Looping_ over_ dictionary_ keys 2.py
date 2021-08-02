d = {'mathew' :'blue','rachel':'green','raymond':'red'}

for k in d.keys():
    if k.startswith('r'):
        del d[k]
