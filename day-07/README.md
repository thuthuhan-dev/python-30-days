# Day 07: Sets

**Date:** 2026-11-12
**Time spent:** 30 min

## What I learned
- A set is an unordered collection of unique items, written with `{}`
- Adding: `add()` for one item, `update()` for several
- Removing: `remove()` raises an error if the item is missing, `discard()` does not
- Set operations: `union()`, `intersection()`, `issubset()`, `isdisjoint()` and `symmetric_difference()`
- `set()` on a list removes duplicates
- `split()` plus `set()` finds the unique words in a sentence

## Code I wrote
- `sets.py`: the Level 1 to 3 exercises, including the unique words in a sentence and the list vs set length comparison

## What confused me
1. **`{}` makes a dictionary, not a set.** An empty set needs `set()`.
2. **`remove()` vs `discard()`.** Both delete an item, so I wasn't sure why Python has two.
3. **The order of a set changed between runs.** I printed the same set twice and the items came out in a different order.
4. **Set vs dictionary.** Both use curly brackets.

## How I solved it / questions still open
- `{}` is reserved for dictionaries, so `set()` is the only way to make an empty set. A dictionary has `key: value` pairs, while a set has only items.
- `remove()` gives a `KeyError` if the item isn't there, and `discard()` stays silent.
- Sets have no order, so Python can show the items in any order and I can't use indexes like `my_set[0]`.
- Open question: when is it better to use a set than a list? I think when I need unique items or fast membership checks.

## My own example
```python
scores = [80, 90, 80, 70, 90]
unique_scores = set(scores)
print(unique_scores)         # {80, 90, 70} (order may differ)
print(len(scores), len(unique_scores))   # 5 3
```
