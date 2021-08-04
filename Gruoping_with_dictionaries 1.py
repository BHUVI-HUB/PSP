# Is dictionary popitem()atomic ?

d = {'mathew':'blue','rachel':'green','raymond':'red'}

while d:
    key,value = d.popitem()
    print(key, '-->',value)
