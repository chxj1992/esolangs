import sys
import numpy as np

def run():
    print(interpret(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])))

def move(a, b, width, height):
    return ((a[0] + b[0]) % height, (a[1] + b[1]) % width)

def interpret(code, iterations, width, height):
    matrix = np.zeros((height, width), dtype=np.int)
    point = (0, 0)
    index = 0
    jump = 0
    tag = []
    while iterations > 0 and index < len(code):
        c = code[index]
        index += 1
        if c not in 'nesw*[]':
            continue
            
        if jump > 0 and c not in '[]':
            continue
        
        if c == 'n':
            point = move(point, (-1, 0), width, height)
        elif c == 'e':
            point = move(point, (0, 1), width, height)
        elif c == 's':
            point = move(point, (1, 0), width, height)
        elif c == 'w':
            point = move(point, (0, -1), width, height)
        elif c == '*':
            matrix[point[0]][point[1]] = int(not matrix[point[0]][point[1]])
        elif c == '[':
            tag.append(index - 1)
            if matrix[point[0]][point[1]] == 0:
                jump += 1
            continue
        elif c == ']':
            i = tag.pop()
            jump = (jump - 1 > 0) if jump - 1 else 0
            if matrix[point[0]][point[1]] != 0:
                index = i
        iterations -= 1

    return "\r\n".join(map(lambda row: ''.join(map(lambda x: str(x), row)), matrix))


if __name__ == "__main__":
    run()

