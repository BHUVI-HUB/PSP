# Distinguishing multiple exit points in loops

def find(seq,target):
    found = False
    for i, value in enumerate(seq):
        if value == tgt:
            found = True
            break
        if not found:
            return -1
        return i
