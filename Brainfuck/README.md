## Brainfuck


This is a `Hello World` Example :
```
++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.
```

```
Brainfuck，是一种极小化的计算机语言，它是由Urban Müller在1993年创建的。
这种语言，是一种按照“Turing complete（完整图灵机）”思想设计的语言，
它的主要设计思路是：用最小的概念实现一种“简单”的语言，BrainF**k 语言只有八种符号，所有的操作都由这八种符号的组合来完成。
```

```
Brainfuck基于一个简单的机器模型，除了八个指令，这个机器还包括：
一个以字节为单位、被初始化为零的数组、一个指向该数组的指针(初始时指向数组的第一个字节)、以及用于输入输出的两个字节流。
```

#### Try It

```
$ python brainfuck.py '++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.' ''
```

#### Run Tests
```
python tests.py
```

* Read more about Befunge on the [ESO Language Wiki](https://esolangs.org/wiki/Brainfuck) page.
* An online [Brainfuck interpreter](https://fatiherikli.github.io/brainfuck-visualizer/)
* [A CodeWars Kata for Brainfuck](https://www.codewars.com/kata/my-smallest-code-interpreter-aka-brainf-star-star-k/train/python)

