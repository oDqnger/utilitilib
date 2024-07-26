# utilitilib

> A python utility package that provides commonly used functionalities or helper methods that you can use to improve productivity or efficiency in your work flow.

## Installation

To install this package, do:

```bash
pip3 install utilitilib
```

## Example Usage

Here's an example of how you would use utilitilib:

```python
from utilitilib.arrays import remove_duplicate
# this imports the remove_duplicate module from the arrays subpackage.

if __name__ == "__main__":
    print(remove_duplicate.remove_duplicate([1,1,1,2,2,2,3,3,3,4,4]))
```

## Uninstall

To uninstall this package, do:

```bash
pip3 uninstall -y utilitilib
```

## Contributing

If you would like to contribute, please check out the [CONTRIBUTING.md](/CONTRIBUTING.md) file

Thank you for your interest in contributing.

## API Reference

- [arrays](/utilitilib/arrays/README.md)
  - [chunk_list](/utilitilib/arrays/chunk_list.py)
  - [remove_all](/utilitilib/arrays/remove_all.py)
  - [remove_duplicate](/utilitilib/arrays/remove_duplicate.py)
  - [shuffle](/utilitilib/arrays/shuffle.py)
  - [unique_value_counter](/utilitilib/arrays/unique_value_counter.py)
- [math](/utilitilib/math/README.md)
  - [mean](/utilitilib/math/mean.py)
  - [median](/utilitilib/math/median.py)
  - [range](/utilitilib/math/range.py)
- [strings](/utilitilib/strings/README.md)
  - [are_anagrams](/utilitilib/strings/are_anagrams.py)
  - [censor_string](/utilitilib/strings/censor_string.py)
  - [format_num](/utilitilib/strings/format_num.py)
  - [replace_one](/utilitilib/strings/replace_one.py)
  - [to_title_case](/utilitilib/strings/to_title_case.py)
- [dateandtime](/utilitilib/dateandtime/README.md)
  - [days_between_dates](/utilitilib/dateandtime/days_between_dates.py)

## Licence

Released under the MIT licence
