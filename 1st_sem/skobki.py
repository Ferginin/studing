st = []
def push(a):
    st.append(a)

def pop():
    return st.pop()

def isempty():
    return len(st) == 0

def top():
    if not isempty():
        return st[-1]
    
def bracet_sequence(s):
    for i in range(len(s)):
        if s[i] in '({[':
            push(s[i])
        elif isempty():
            return 'no'
        elif top() + s[i] in {'()', '[]', '{}'}:
            pop()
        else:
            return 'no'
    if isempty():
        return 'yes'
    else:
        return 'no'

bracket = input()
print(bracet_sequence(bracket)) 