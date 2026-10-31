\# Day 01: Introduction



\*\*Date:\*\* 2026-10-31

\*\*Time spent:\*\* 60 min (change to your real time)



\## What I learned

\- How to write and run a Python file with `python helloworld.py`

\- How to write comments (`#`) and multiline comments (`"""..."""`)

\- The basic data types: int, float, complex, string, boolean, list, tuple, set and dictionary

\- How to check a type with `type()`

\- The arithmetic operators: `+`, `-`, `\*`, `/`, `%`, `//`, `\*\*`



\## Code I wrote

\- `helloworld.py`: prints arithmetic results, prints examples of each data type with `type()`, and solves the Euclidean distance exercise



\## What confused me

The difference between `/`, `//` and `%`. They all involve division but give different answers.



\## How I solved it / questions still open

I tried them with the same numbers, 17 and 5:

\- `17 / 5` = 3.4 (normal division, with decimals)

\- `17 // 5` = 3 (floor division: how many times 5 fits in 17, decimals dropped)

\- `17 % 5` = 2 (modulus: the remainder after dividing)



Check: 5 x 3 = 15, and 17 - 15 = 2. So `//` gives the 3 and `%` gives the 2.



The Euclidean distance exercise needed more focus. It's the straight-line distance between two points, from the Pythagorean theorem:

\- x difference: 10 - 2 = 8, y difference: 8 - 3 = 5

\- distance = √(8² + 5²) = √89 ≈ 9.43

\- In Python: `((x2 - x1) \*\* 2 + (y2 - y1) \*\* 2) \*\* 0.5`



Open question: I imported `sqrt` from `math` but used `\*\* 0.5`. I want to understand modules better on Day 12.



\## My own example

I used `%` to check if a number is even:

```python

print(10 % 2)  # 0 means even

print(7 % 2)   # 1 means odd

```

