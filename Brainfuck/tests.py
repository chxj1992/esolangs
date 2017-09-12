from brainfuck import interpret

# Echo until byte(255) encountered
assert interpret(',+[-.,+]', 'Codewars' + chr(255)) == 'Codewars'

# Echo until byte(0) encountered
assert interpret(',[.[-],]', 'Codewars' + chr(0)) == 'Codewars'

# Two numbers multiplier
assert interpret(',>,<[>[->+>+<<]>>[-<<+>>]<<<-]>>.', chr(8) + chr(9)) == chr(72)

# Hello World!
assert interpret('++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.', '') == 'Hello World!'

assert interpret(',+[-.,+]', '31acx3j9xj2g\xff') == '31acx3j9xj2g'

assert interpret(',[.[-],]', 'eh6hn3dmxv67\x00') == 'eh6hn3dmxv67'

print('Successed!')
