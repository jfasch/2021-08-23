x = 666

def f():
    global x
    x = 1
    print('local', x)

f()

print('global', x)
