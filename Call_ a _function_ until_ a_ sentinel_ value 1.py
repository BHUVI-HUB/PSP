# Call a function until a sentinel value


blocks = []
while True:
    block = (f.read(32))
    if block =='':
        break
    blocks.append(block)
