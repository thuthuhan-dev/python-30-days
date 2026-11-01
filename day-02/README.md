\# Day 02: Variables, Built-in Functions



\*\*Date:\*\* 2026-11-01

\*\*Time spent:\*\* 50 min



\## What I learned

\- How to declare variables (`first\_name = "Thu"`) and that Python picks the data type automatically

\- Variable naming rules: letters, numbers and underscores, no spaces, and it can't start with a number

\- How to check types with `type()` and the length of a string with `len()`

\- How to declare several variables on one line (`x, y, z = 10, 20, 30`)

\- How to do arithmetic with variables and use the results

\- How `input()` takes values from the user. It always returns a string, so numbers need `int()`

\- How to use `help()` to read the documentation of Python's built-in names



\## Code I wrote

\- `variables.py`: variables for my details, type checks, string length, arithmetic with `num\_one` and `num\_two`, circle area and circumference, and user input



\## What confused me

1\. \*\*Naming a variable `sum`.\*\* I used `sum` for `num\_one + num\_two` because I know SUM from Excel. But in Python `sum` is already a built-in function, and using it as a variable name hides that function. I renamed it to `total`.

2\. \*\*`help(str)` seemed to freeze.\*\* The screen filled with text and I didn't know how to get back to the prompt, so I pressed Enter again and again.



\## How I solved it / questions still open

\- For `sum`: variable names shouldn't reuse built-in names like `sum`, `len`, `type`, `input` or `str`. Descriptive names like `total` avoid the problem.

\- For `help(str)`: it wasn't an error. `help()` shows long documentation in a pager, which is a viewer that shows one screen at a time. Enter only scrolls one line. Pressing \*\*q\*\* quits and returns to the prompt. (Space scrolls a full page.)

\- Open question: how do I know which names are built-ins so I don't overwrite them by accident?



\## My own example

```python

\# Excel's SUM, but in Python

prices = \[5, 4, 10]

total\_price = sum(prices)   # the built-in sum() works on a list

print(total\_price)          # 19

```

