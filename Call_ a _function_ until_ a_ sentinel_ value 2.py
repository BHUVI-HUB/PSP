blocks = []
for blocks in iter(partial(f.read,32), ''):
    blocks.append(block)
