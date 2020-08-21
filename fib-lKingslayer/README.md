# Fibonacci

## 问题描述

你需要编写一个 Python 程序完成计算斐波那契数。具体来说，你需要修改项目中的 `fib.py`，并完成以下功能：

1. 从标准读入读入一个整数n。
2. 输出斐波那契数第n项。

为了避免模糊，我们定义该数列第零项为0，第一项为1。

## 样例与评分

我们在 `data` 目录下提供了八组数据，分别对应不同的情况和数据量大小。和之前的题目一样，你可以通过 `python3 grade.py` 来进行一次的本地测评。

这次会考验你代码编写的效率，如果代码运行的不够快，可能不到黑盒的满分。本题设置了 1s 的时间限制，如果超过了这个时间，评测程序会提示你超时；对于未超时的数据，它会输出你的代码的实际用时。

在提交到Github之后，可以在commit旁边查看小绿勾或者小红叉，此可用于自测，当为小绿勾的时候，你的程序可以在助教机器上运行，且有大概率你的程序完成了题目要求。

最终评分以在助教机器上运行的时间为准。所用电脑的 CPU 为 Intel i7-8750H。

最终分数构成为：

* 黑盒 80 分：共 8 个测例，每个 10 分
* 白盒 20 分：代码风格与 Git 使用 20 分（包括恰当注释、合理命名、提交日志等）

请注意，由于斐波那契数列是确定的，一个粗暴的方法是在代码中写下数列，然后输出，在此题中不允许这样做。

助教以 deadline 前 GitHub 上最后一次提交为准进行评测。