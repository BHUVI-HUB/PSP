# Counting with dictionaries

colors = {'red','green','red','blue','green','red'}
d = {}
for color in colors:
    if color not in d:
        d[color] =0
        d[color]+=1

    {'blue':1,'green':2,'red':3}
