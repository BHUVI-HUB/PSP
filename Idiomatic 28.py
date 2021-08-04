# Harmful

def contains_zero(iterable):
for e in iterable:
if e == 0:
return True
return False



# Idiomatic

def contains_zero(iterable):
# 0 is "Falsy," so this works
return not all(iterable)
