import sys
from itertools import chain

def run():
    print(interpret(sys.argv[1], sys.argv[2]))

def encode(c):
  return map(lambda x: int(x), list(format(ord(c), '08b'))[::-1])

def interpret(code, input = ''):
  output = ''
  out = []
  data = [0]
  input = list(chain.from_iterable(map(lambda x: encode(x), input)))
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
      data[data_pointer] = input.pop(0) 
    elif c == ';':
      out.append(data[data_pointer])
    elif c == '>':
      data_pointer += 1
      if data_pointer > len(data) - 1:
        data.append(0)
    elif c == '<':
      if data_pointer > 0:
          data_pointer = data_pointer - 1
      else:
          data.insert(0, 0)
    elif c == '+':
      data[data_pointer] = int(not data[data_pointer])
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

  for i in range(0, len(out), 8):
      output += chr(int(''.join(map(lambda x: str(x), out[i:i+8][::-1])), 2))

  return output


if __name__ == "__main__":
    run()

