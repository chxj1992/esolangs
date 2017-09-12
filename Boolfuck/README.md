## Boolfuck


This is a `Hello World` Example :
```
;;;+;+;;+;+;+;+;+;+;;+;;+;;;+;;+;+;;+;;;+;;+;+;;+;+;;;;+;+;;+;;;+;;+;+;+;;;;;;;+;+;;+;;;+;+;;;+;+;;;;+;+;;+;;+;+;;+;;;+;;;+;;+;+;;+;;;+;+;;+;;+;+;+;;;;+;+;;;+;+;+;
```

```
Boolfuck是一种继承于[Brainfuck](https://github.com/chxj1992/esolangs/tree/master/Brainfuck)的编程语言，在设计思想上与Brainfuck十分相似。
```

```
与Brainfuck相比，Boolfuck主要有如下几个区别：
* 每一个数据位只能保存0或1（Brainfuck可以保存0-255）
* ; 表示输出数据（Brainfuck用 .）
* + 表示反转数据，没有 - 
```

#### Try It

```
$ python boolfuck.py ';;;+;+;;+;+;+;+;+;+;;+;;+;;;+;;+;+;;+;;;+;;+;+;;+;+;;;;+;+;;+;;;+;;+;+;+;;;;;;;+;+;;+;;;+;+;;;+;+;;;;+;+;;+;;+;+;;+;;;+;;;+;;+;+;;+;;;+;+;;+;;+;+;+;;;;+;+;;;+;+;+;' ''
```

#### Run Tests
```
python3 tests.py
```

* Read more about Boolfuck on the [ESO Language Wiki](https://esolangs.org/wiki/Boolfuck) page.
* An online [Boolfuck interpreter](https://tio.run/#boolfuck)
* [A CodeWars Kata for Boolfuck](https://www.codewars.com/kata/esolang-interpreters-number-4-boolfuck-interpreter/train/python)

