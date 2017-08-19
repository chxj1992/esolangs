import random
import sys

def run():
    print(interpret(sys.argv[1]))

def interpret(code):
    out = ''
    stack = []
    code = code.split('\n')
    c = code[0][0]
    position = (0, 0)
    direction = (1, 0)
    ascii_mode = False
    while c != '@':
        if ascii_mode:
            if c == '"':
                ascii_mode = False
            else:
                stack.insert(0, str(ord(c)))
        else:
            if c in "0123456789":
                stack.insert(0, c)
            if c == '+':
                stack.insert(0, str(int(stack.pop(0)) + int(stack.pop(0))))
            if c == '-':
                stack.insert(0, str(-(int(stack.pop(0)) - int(stack.pop(0))))) 
            if c == '*':
                stack.insert(0, str(int(stack.pop(0)) * int(stack.pop(0)))) 
            if c == '/':
                a = stack.pop(0)
                b = stack.pop(0)
                if a == '0':
                    stack.insert(0, '0')
                else:
                    stack.insert(0, str(b // a))
            if c == '%':
                a = stack.pop(0)
                b = stack.pop(0)
                if a == '0':
                    stack.insert(0, '0')
                else:
                    stack.insert(0, str(b % a)) 
            if c == '!':
                if stack.pop(0) == '0':
                    stack.insert(0, '1')
                else:
                    stack.insert(0, '0')
            if c == '`':
                a = stack.pop(0)
                b = stack.pop(0)
                if int(b) > int(a):
                    stack.insert(0, '1')
                else:
                    stack.insert(0, '0')
            if c == '>':
                direction = (1, 0)
            if c == '<':
                direction = (-1, 0)
            if c == 'v':
                direction = (0, 1)
            if c == '^':
                direction = (0, -1)
            if c == '?':
                direction = random.choice([(1, 0),(0, 1),(-1, 0),(0, -1)])
            if c == '_':
                v = stack.pop(0)
                if v == '0':
                    direction = (1, 0)
                else:
                    direction = (-1, 0)
            if c == '|':
                v = stack.pop(0)
                if v == '0':
                    direction = (0, 1)
                else:
                    direction = (0, -1)
            if c == '"':
                ascii_mode = True
            if c == ':':
                if len(stack) > 0:
                    stack.insert(0, stack[0])
                else:
                    stack.insert(0, '0')
            if c == '\\':
                if len(stack) > 1:
                    v = stack.pop(0)
                    stack.insert(1, v)
                else:
                    stack.insert(0, '0')
            if c == '$':
                stack.pop(0)
            if c == '.':
                out += stack.pop(0)
            if c == ',':
                out += chr(int(stack.pop(0)))
            if c == '#':
                position = tuple([x+y for x, y in zip(direction, position)])
            if c == 'p':
                y = stack.pop(0)
                x = stack.pop(0)
                v = stack.pop(0)
                l = list(code[int(y)])
                l[int(x)] = chr(int(v))
                code[int(y)] = ''.join(l)
            if c == 'g':
                y = stack.pop(0)
                x = stack.pop(0)
                stack.insert(0, str(ord(code[int(y)][int(x)])))
        position = tuple([x+y for x, y in zip(direction, position)])
        c = code[position[1]][position[0]]

    return out

if __name__ == "__main__":
    run()

