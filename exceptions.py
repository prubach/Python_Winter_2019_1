a = 210
b = 67
try:
    c = b / d
    if a>b:
        raise Exception('a>b')
except Exception as e:
    print(e)
print('continuing...')