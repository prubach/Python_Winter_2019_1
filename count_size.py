import os

def count_size(f):
    size = 0
    if os.path.isdir(f):
        for file in os.listdir(f):
            size += count_size(os.path.join(f, file))
    else:
        size += os.path.getsize(f)
    return size

dir = 'h:\\Podania'
print(count_size(dir))
