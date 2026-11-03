# Day 04: Strings

**Date:** 2026-11-03
**Time spent:** 100 min

## What I learned
- How to join strings with `+` and with f-strings (`f"{a} {b} {c}"`)
- Changing case with `upper()`, `lower()`, `capitalize()`, `title()` and `swapcase()`
- Slicing: `company[7:]` cuts out the first word, and `company[0]` gets one character
- Searching: `index()`, `find()`, `rfind()`, `rindex()`, `startswith()`, `endswith()` and `in`
- Changing text: `replace()`, `strip()`, `split()` and `join()`
- Escape sequences: `\n` for a new line and `\t` for a tab
- String formatting with f-strings, including `:.2f` to show two decimals
- Checking names with `isidentifier()`

## Code I wrote
- `strings.py`: all the Day 4 exercises, from joining strings to formatting a table of arithmetic results

## What confused me
1. **`company[10]` printed a blank line.** I thought something was wrong.
2. **The tab table wasn't aligned.** The `Name`, `Age`, `Country` and `City` columns didn't line up with the row below.
3. **`index()` vs `find()`.** Both find the position of a word, so I wasn't sure why Python has two.
4. **`isidentifier()`.** I didn't know why `'30DaysOfPython'` gave `False`.

## How I solved it / questions still open
- Index 10 in `Coding For All` is the space between `For` and `All`. Python counts from 0 and spaces count as characters. `repr(company[10])` prints `' '`, which makes the space visible.
- A tab jumps to the next tab stop (every 8 characters), so a short word like `Name` ends earlier than `Asabeneh`. Adding a second tab after `Name` fixed the alignment.
- If the word isn't found, `index()` raises a `ValueError` and `find()` returns `-1`.
- `'30DaysOfPython'.isidentifier()` is `False` because variable names can't start with a digit. This matches the naming rules from Day 2.
- Open question: when I use `''.join(...)` for the acronym, I want to understand the shorter loop version better. I'll come back to it on Day 13.

## My own example
```python
word = 'python'
print(word.upper())           # PYTHON
print(word[0] + word[-1])     # pn
print(f'{word} has {len(word)} letters')   # python has 6 letters
```
