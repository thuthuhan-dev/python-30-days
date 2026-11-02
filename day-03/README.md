# Day 03: Operators

**Date:** 2026-11-02
**Time spent:** 75 min

## What I learned
- Arithmetic operators: `+`, `-`, `*`, `/`, `%`, `//`, `**`
- Comparison operators: `==`, `!=`, `>`, `<`, `>=`, `<=`. They give `True` or `False`
- Logical operators: `and`, `or`, `not`
- Membership operators: `in` and `not in` check whether text is inside other text
- Type conversion: `int()`, `float()` and `str()` change a value from one type to another
- How to combine `input()` with `int()` to build small calculators (triangle area, perimeter, pay, seconds lived)
- How to use a conditional expression to check even or odd with `%`: `'Even' if n % 2 == 0 else 'Odd'`

## Code I wrote
- `operators.py`: variables for age, height and a complex number; calculators for triangle, rectangle and circle; slope and Euclidean distance; `y = x² + 6x + 9`; string comparisons with `in`; type checks; weekly pay; seconds lived; and a number table

## What confused me
1. **`int('9.8')` and `int(9.8)` are not the same.** I wrote `int(9.8)` without quotes and it worked, but the exercise has quotes around the number.
2. **I overwrote `height`.** I made `height = 5.5` as a float, then used `height` again for the triangle input, which replaced it.
3. **The `y = x² + 6x + 9` exercise.** I jumped straight to the answer instead of trying different x values.

## How I solved it / questions still open
- `int(9.8)` converts a float and gives 9. `int('9.8')` crashes with a `ValueError`, because `int()` can't read a string with a decimal point. To convert it I need `int(float('9.8'))`.
- I gave the triangle input its own name, `triangle_height`, so the first variable stays safe. Each new value needs a unique name, or the old one is lost.
- I tried x = 0, -1, -2 and -3, and got y = 9, 4, 1 and 0. The pattern is `y = (x + 3)²`, so y is 0 only when x = -3.
- Open question: `input()` with `int()` crashes if someone types a decimal. When will I learn how to handle that? (Probably exception handling on Day 17.)

## My own example
```python
# Does a word contain a smaller word?
print('py' in 'python')      # True
print('java' in 'python')    # False
print('py' in 'python' and 'on' in 'python')   # True
```
