# Swap Elements with Iterable Unpacking
```python
palette_1 = "foie"
palette_2 = "barata"
palette_1, palette_2 = palette_2, palette_1
```
This solution works because the righthand side of the statement places our two variables in a `tuple`, which is an immutable list. This following code snippet works exactly the same way:
```python
palette_1 = "foie"
palette_2 = "barta"
_ = palette_2, palette_1 # creates a tuple from the two palettes
palette_1, palette_2 = _ 
```
# Performance 
As always, I like to take all of the solutions and run them through a quick performance test. To do that, we’ll need to store each solution in a string:
```python
setup = """
palette_1 = "foie"
palette_2 = "barta"
"""
temp = """
_ = palette_1
palette_1 = palette_2
palette_2 = _
"""
unpack = """
palette_1, palette_2 = palette_2, palette_1
"""
```
Here, we created three strings: one for each solution and one to introduce our strings. Naturally, all we have to do now is import our testing utility, `timeit`, and we’ll be ready to go:
```python
import timeit
min(timeit.repeat(setup=setup, stmt = temp))
min(timeit.repeat(setup=setup, stmt = unpack))
```

