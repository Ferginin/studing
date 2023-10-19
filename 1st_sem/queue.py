def isempty(deck):
    return len(deck) == 0

def push(deck,el):
    deck.append(el)
    print("ok")
    
def pop(deck):
    if isempty(deck):
        print('error')
    else:
        print(deck.pop(0))

def front(deck):
    if isempty(deck):
        print('error')
    else:
        print(deck[0])

def size(deck):
    print(len(deck))

def clear(deck):
    deck[:] = []
    print('ok')

def exit():
    global check
    print('bye')
    check = False

def menu(better,call,saul):
    if better == "push":
        push(call, saul)
    elif better == "pop":
        pop(call)
    elif better == "front":
        front(call)
    elif better == "size":
        size(call)
    elif better == "clear":
        clear(call)
    elif better == "exit":
        exit()
    
a = []
num = 0
check = True
while check:
    enter = input().split()
    if len(enter) > 1:
        num = int(enter.pop())
        enter = enter.pop()
    else:
        enter = enter.pop()
    menu(enter, a, num)