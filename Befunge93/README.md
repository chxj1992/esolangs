## Befunge


This is a `Hello World` Example :
```
>25*"!dlroW olleH":v
                v:,_@
                >  ^
```

```
Befunge 是一个基于堆栈的编程语言，大部分指令都是堆栈操作：往堆栈里压入一个东西，从堆栈里弹出一个东西，交换堆栈顶部的两个东西。
Befunge 中也有加减乘除、模、逻辑非、大于等常见的运算，只不过要理解为堆栈操作。
比如说，加法 + 表示从堆栈里弹出两个数，把它们加起来，然后把结果压会堆栈。

```
```
除了堆栈操作的指令之外，Befunge 中还有一些指示方向的指令。
比如说， ^v<> 分别表示上下左右四个方向的箭头；问号 ? 表示随机的一个方向；| 和 _ 这两个符号表示条件选择，
比如说 _ 表示从堆栈里弹出一个值，如果它等于0就转向右边，否则转向左边。
此外，# 表示跳过一个指令，@ 表示结束程序。
```

#### Try It

```
$ python befunge93.py '>25*"!dlroW olleH":v\n                v:,_@\n                >  ^'
```

#### Run Tests
```
python tests.py
```

* Read more about Befunge on the [ESO Language Wiki](https://esolangs.org/wiki/Befunge) page.
