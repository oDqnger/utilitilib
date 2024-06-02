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


- [arrays](/pyUtilities/arrays)
    - [chunk_list](/pyutilities/arrays/chunk_list.py)
    - [remove_all](/pyutilities/arrays/remove_all.py)
    - [remove_duplicate](/pyutilities/arrays/remove_duplicate.py)
    - [shuffle](/pyutilities/arrays/shuffle.py)
    - [unique_value_counter](/pyutilities/arrays/unique_value_counter.py)
- [math](/pyutilities/math)
    - [mean](/pyutilities/math/mean.py)
    - [median](/pyutilities/math/median.py)
    - [range](/pyutilities/math/range.py)
- [strings](/pyutilities/strings)
    - [are_anagrams](/pyutilities/strings/are_anagrams.py)
    - [censor_string](/pyutilities/strings/censor_string.py)
    - [format_num](/pyutilities/strings/format_num.py)
    - [replace_one](/pyutilities/strings/replace_one.py)
    - [to_title_case](/pyutilities/strings/to_title_case.py)
