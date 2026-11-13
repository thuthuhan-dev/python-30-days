# Day 08: Dictionaries

**Date:** 2026-11-13
**Time spent:** 38 min

## What I learned
- A dictionary stores `key: value` pairs in curly brackets `{}`
- Adding and changing items with `dog['name'] = 'Bo Phyu'`
- Getting a value by its key: `student['skills']`
- A value can be any type, including a list (`skills`), so I can change it with `append()`
- `keys()`, `values()` and `items()` give views of the dictionary, and `list()` turns them into real lists
- Removing items with `pop()` and `del`, and removing the whole dictionary with `del`
- `len()` counts the key-value pairs

## Code I wrote
- `dictionaries.py`: a `dog` dictionary, a `student` dictionary, changing the skills list, getting keys, values and items, and deleting items

## What confused me
1. **`keys()` didn't print a list.** The output looked like `dict_keys([...])`, not `[...]`.
2. **Set vs dictionary.** Both use `{}`.
3. **Replacing vs adding.** I made `dog` again with a new `{...}` instead of adding to it.

## How I solved it / questions still open
- `keys()`, `values()` and `items()` return view objects, so I wrap them: `list(student.keys())`. `items()` gives a list of `(key, value)` tuples.
- A dictionary has `key: value` pairs and a set has only items. An empty `{}` is a dictionary, so an empty set needs `set()`.
- Assigning a new dictionary replaces the old one. Adding one key at a time with `dog['age'] = 3` keeps the existing items.
- Open question: what happens if I ask for a key that doesn't exist? I think `student['phone']` gives a `KeyError`, and `student.get('phone')` gives `None`. I want to try both.

## My own example
```python
book = {'title': 'Python Basics', 'pages': 200}
book['author'] = 'Me'
print(book['title'])          # Python Basics
print(list(book.keys()))      # ['title', 'pages', 'author']
print('pages' in book)        # True (checks keys)
```
