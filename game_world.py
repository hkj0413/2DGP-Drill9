world = [[],[],[]]

def add_object(o, depth):
    world[depth].append(o)

def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o)
            return

    print(f'CRITICAL: 존재 하지 않는 객체{o}를 지우 려고 합니다.')

def update():
    for layer in world:
        for o in layer:
            o.update()

def draw():
    for layer in world:
        for o in layer:
            o.draw()