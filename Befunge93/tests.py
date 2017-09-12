from befunge93 import interpret

# 1-9
assert interpret('>987v>.v\nv456<  :\n>321 ^ _@') == '123456789'

#Hello World!
assert interpret('>25*"!dlroW olleH":v\n                v:,_@\n                >  ^') == 'Hello World!\n'

# Factorial (8! = 40320)
assert interpret('08>:1-:v v *_$.@ \n  ^    _$>\:^') == '40320'

# Quine
assert interpret('01->1# +# :# 0# g# ,# :# 5# 8# *# 4# +# -# _@') == '01->1# +# :# 0# g# ,# :# 5# 8# *# 4# +# -# _@'

# Sieve of Eratosthenes
assert interpret('2>:3g" "-!v\  g30          <\n |!`"&":+1_:.:03p>03g+:"&"`|\n @               ^  p3\\" ":<\n2 2345678901234567890123456789012345678') == '23571113171923293137'

print('Successed!')
