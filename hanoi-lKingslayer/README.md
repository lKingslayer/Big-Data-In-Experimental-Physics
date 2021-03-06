# Hanoi

## 问题背景

天才少年爱迪生正在玩家里的汉诺塔，玩到中途突然被叫出去录节目了。回来时发现，
自己已经忘了自己移到哪了，他将天才的目光投向你，你能帮他将汉诺塔移完吗？

## 问题描述

你需要编写一个 Python 程序输出之后的移动顺序。
具体来说，你需要修改项目中的 `hanoi.py`，并完成以下功能：

1. 读入已经移动了一部分的汉诺塔。从标准输入读入三行，每一行表示一个柱子的情况，
从左到右是从底向上的盘子，数字表示盘子的大小。
2. 输出之后的系列移动动作。例如要将0号柱子最顶上盘子移动到2号柱子，我们输出0 2

输入输出的具体细节，请参看 `data` 目录下的样例。

为了不动脑子，我们采用维基百科中的算法生成中间状态，且后续移动也约定使用该算法。
同时我们约定我们的目标是将塔从0号柱子移动到2号。

对于无法访问维基的同学，我们摘录以下关键信息：

解法的基本思想是递归。假设有 0、1、2 三个塔，0 塔有 N 块盘，目标是把这些盘全部移到 2 塔。那么先把 0 塔顶部的 N-1 块盘移动到 1 塔，再把 0 塔剩下的大盘移到 2，最后把 1 塔的 N-1 块盘移到 2。

示例算法表示为（以下不符合本题的输入输出要求），

```python
def hanoi(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        hanoi(n - 1, a, c, b)
        hanoi(1    , a, b, c)
        hanoi(n - 1, b, a, c)

hanoi(5, 'A', 'B', 'C')
```

## 样例与评分

我们在 `data` 目录下提供了十组数据，分别对应不同的情况和数据量大小，这次正式评测不会使用额外的数据。和之前的题目一样，你可以通过 `python3 grade.py` 来进行一次的本地测评。

对于in5.txt与ans5.txt，由于in5给出的是依照该算法不可能出现的中间状态，ans5为空。为了避免修改，我们规定，对于不可能出现的中间状态，我们不做移动。

这次会考验你代码编写的效率，如果代码运行的不够快，可能不到黑盒的满分。本题设置了 1s 的时间限制，如果超过了这个时间，评测程序会提示你超时；对于未超时的数据，它会输出你的代码的实际用时。

最终评分以在助教机器上运行的时间为准。所用电脑的 CPU 为 Intel Core i7-7820HQ。

最终分数构成为：

* 黑盒 80 分：共 8 个测例，每个 10 分
* 白盒 20 分：代码风格与 Git 使用 20 分（包括恰当注释、合理命名、提交日志等）

助教以 deadline 前 GitHub 上最后一次提交为准进行评测。
