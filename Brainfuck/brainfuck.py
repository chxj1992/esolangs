import sys

def run():
    print(interpret(sys.argv[1], sys.argv[2]))

def increment(c):
  return (c + 1) % 256
  
def decrement(c):
  if c == 0:
      return 255
  return (c - 1) % 256    
  
def interpret(code, input):
  output = ''
  data = [0]
  input = list(input)
  code_pointer = 0
  data_pointer = 0
  jump = 0
  tag = []
  while True and code_pointer < len(code):
    c = code[code_pointer]
    if jump > 0 and c not in '[]':
        code_pointer += 1
        continue
    if c == ',':
      if len(input) == 0:
        break
      data[data_pointer] = ord(input.pop(0))
    elif c == '.':
      output += chr(data[data_pointer])
    elif c == '>':
      data_pointer += 1
      if data_pointer > len(data) - 1:
        data.append(0)
    elif c == '<':
      data_pointer = data_pointer - 1 if data_pointer > 0 else 0
    elif c == '+':
      data[data_pointer] = increment(data[data_pointer])
    elif c == '-':
      data[data_pointer] = decrement(data[data_pointer])
    elif c == '[':
      tag.append(code_pointer)
      if data[data_pointer] == 0:
        jump += 1
    elif c == ']':
      t = tag.pop()
      jump = jump - 1 if jump > 0 else 0
      if data[data_pointer] != 0:
        code_pointer = t
        continue
    code_pointer += 1
    
  return output
  

if __name__ == "__main__":
    run()

