# PyUtilities

> A python utility package that provides commonly used functionalities or helper methods that you can use to improve productivity or efficiency in your work flow.

## Installation

To install this package, do:

```bash
pip3 install pyutilities
```

To test if this works, select a category from down below and import its' module. For instance:

```python
from pyutilities import arrays.remove_duplicate

print(remove_duplicate([1,1,2,2,3,4,4,4,4,4]))
```
## Uninstall

To uninstall this package, do:

```bash
pip3 uninstall -y pyutilities
```

## API Reference


- [arrays](/utilitilib/arrays)
    - [chunk_list](/utilitilib/arrays/chunk_list.py)
    - [remove_all](/utilitilib/arrays/remove_all.py)
    - [remove_duplicate](/utilitilib/arrays/remove_duplicate.py)
    - [shuffle](/utilitilib/arrays/shuffle.py)
    - [unique_value_counter](/utilitilib/arrays/unique_value_counter.py)
- [math](/utilitilib/math)
    - [mean](/utilitilib/math/mean.py)
    - [median](/utilitilib/math/median.py)
    - [range](/utilitilib/math/range.py)
- [strings](/utilitilib/strings)
    - [are_anagrams](/utilitilib/strings/are_anagrams.py)
    - [censor_string](/utilitilib/strings/censor_string.py)
    - [format_num](/utilitilib/strings/format_num.py)
    - [replace_one](/utilitilib/strings/replace_one.py)
    - [to_title_case](/utilitilib/strings/to_title_case.py)
