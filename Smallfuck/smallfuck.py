import sys

def run():
    print(interpret(sys.argv[1], sys.argv[2]))

def interpret(code, tape):    
    tape = list(tape)
    tape_index = 0
    code_index = 0
    tag = []
    jump = 0
    
    while True:
        c = code[code_index]
        code_index += 1
        if jump > 0 and c not in '[]':
            continue
        elif c == '*':
            tape[tape_index] = str(int(not int(tape[tape_index])))
        elif c == '>':
            tape_index += 1
        elif c == '<':
            tape_index -= 1
        elif c == '[':
            tag.append(code_index - 1)
            if tape[tape_index] == '0':
                jump += 1
        elif c == ']':
            jump -= 1
            index = tag.pop()
            if tape[tape_index] != '0':
                code_index = index
        
        if code_index < 0 or code_index > len(code) - 1:
            break
        if tape_index < 0 or tape_index > len(tape) - 1:
            break
            
    return ''.join(tape)


if __name__ == "__main__":
    run()

