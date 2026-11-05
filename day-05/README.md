# Day 05: Lists

**Date:** 2026-11-05
**Time spent:** 65 min

*Note: I paused for a few days because of graduation preparation and a workshop, then came back to finish Day 5.*

## What I learned
- Lists hold ordered items of any type, and I can change them after creating them
- Getting items with indexes (`list[0]`, `list[-1]`) and slices (`list[:3]`, `list[-3:]`)
- Adding items: `append()` adds to the end, `insert()` adds at a position
- Removing items: `pop()`, `del`, and `clear()`
- Sorting and reversing with `sort()` and `reverse()`
- Making a real copy with `copy()`
- Joining lists with `+` and joining list items into a string with `"#;  ".join(list)`
- `min()`, `max()`, `sum()` and `abs()` for the age statistics
- Unpacking: `first, second, third, *rest = list`
- Importing the countries list from a separate file with `from countries import countries`

## Code I wrote
- `lists.py`: all the Day 5 exercises, from the company list to the age statistics and country splitting
- `countries.py`: the country list copied from Asabeneh's course repo (not my own work)

## What confused me
1. **`copy()`.** I first wrote `full_stack = full_stack.copy()`, which copies a list onto itself and proves nothing.
2. **Middle of a list with an even number of items.** My first list had 6 items, so there is no single middle.
3. **`del` vs `clear()`.** Both seemed to remove everything.
4. **Statistics order.** The median and average depend on whether I add the min and max again first.

## How I solved it / questions still open
- I made `joined_list = front_end + back_end`, then `full_stack = joined_list.copy()`. After inserting Python and SQL, `joined_list` stays unchanged and `full_stack` has the new items, which shows the copy is separate.
- For an even length I print two middle items (`list[middle - 1:middle + 1]`). For an odd length I print one. I also added a seventh item to my own list so it has a single middle.
- `clear()` empties the list but the name still exists, so printing it gives `[]`. `del it_companies` removes the name itself, so printing it afterwards gives a `NameError`.
- The exercise says to add the min and max again before the median and average. Original average: 228 / 10 = 22.8. After adding 19 and 26: 273 / 12 = 22.75, median 24.0. The min and max differences from the average are 3.75 and 3.25, so they are not equal.
- Open question: `reverse()` only flips the current order, it doesn't sort. I want to remember to call `sort()` first if I need descending order.

## My own example
```python
tasks = ["study", "workshop", "graduation prep"]
tasks.append("python day 5")
print(tasks[-1])    # python day 5
print(len(tasks))   # 4
```
