# Looping over two collections

brands = ['puma','nike','adidas']
names  = ['virat','neyamr','messi']

n= min(len(names),len(brands))
for i in range(n):
    print(names[i],'-->',brands[i])
