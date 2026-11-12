# Day 06: Tuples

**Date:** 2026-11-06
**Time spent:** 55 min

*Note: I commit this README on November 11 not November 6 and i paused for a few days because of Graduation, illness and a workshop.*

## What I learned
- A tuple is an ordered collection that can't be changed after it is created (immutable)
- Tuples use round brackets `()`, and indexing and slicing work like lists
- Tuples have few methods: `count()` and `index()`
- Joining tuples with `+` creates a new tuple, because the old one can't be modified
- Converting between types: `list(my_tuple)` to change it, `tuple(my_list)` to lock it again
- `in` checks if an item exists in a tuple
- `del` removes the whole tuple, but not single items
- Unpacking with a star: `*siblings, father, mother = family_members`

## Code I wrote
- `tuples.py`: siblings and parents tuples, joining tuples, unpacking, food tuples converted to a list, slicing, `del`, and checking Nordic countries with `in`

## What confused me
1. **`print(siblings = brothers + siblings)` crashed.** Python gave a `TypeError` about an invalid keyword argument.
2. **"Modify the siblings tuple".** Tuples can't be modified, so I wasn't sure how to add parents.
3. **Unpacking gave a list.** `*siblings` became a list, not a tuple.
4. **A `.pyc` file ended up in my repo.** My `.gitignore` didn't work.

## How I solved it / questions still open
- Inside `print(...)`, `name = value` is read as a keyword argument, not an assignment. I assign on one line and print on the next.
- I made a new tuple with `family_members = siblings + parents`.
- The starred name in unpacking always collects its items into a list.
- The `.gitignore` probably had hidden characters from pasting. I retyped it by hand and removed the file from the repo with `git rm --cached`.
- Open question: why does Python have tuples if lists can do everything tuples can? I think it is for data that should not change.

## My own example
```python
days = ('Mon', 'Tue', 'Wed')
print(days[0])        # Mon
print('Fri' in days)  # False
days_list = list(days)
days_list.append('Thu')
print(tuple(days_list))   # ('Mon', 'Tue', 'Wed', 'Thu')
```
