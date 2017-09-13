from smallfuck import interpret

assert interpret("*", "00101100") == "10101100"

assert interpret(">*>*", "00101100") == "01001100"

assert interpret("*>*>*>*>*>*>*>*", "00101100") == "11010011"

assert interpret("*>*>>*>>>*>*", "00101100") == "11111111"

assert interpret(">>>>>*<*<<*", "00101100") == "00000000"

print('Successed!')
