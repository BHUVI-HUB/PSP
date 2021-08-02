brands = ['puma','nike','adidas']
names  = ['virat','neyamr','messi']

n = min(len(names),len(brands))
for names,brands in zip(names,brands):
    print(names, '-->',brands)
