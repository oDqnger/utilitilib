
# Array API Reference

this subpackage contains utility functions specificaly for arrays.

| Function | Description                                     | Parameters            | Returns   |
|---------------|-------------------------------------------------|-----------------------|-----------|
| `chunk_list`  | Chunks a list into smaller lists of a specified size | `lst` (list): original list to be chunked<br>`size` (int): size of each chunk | `list`: a list containing all the chunks |
| `remove_all` | Removes all specified elements from a list | `arr` (list): the array that needs the object to be removed from<br>`item` (any): the item/object that needs to get removed from the array. | `list`: the new list (all elements removed from it) |
| `remove_duplicate` | A function that removes duplicates from an array | `array` (list): Can be any length list, with any type | `array` (list): Returns a list with unique characters (all duplicates removed) |
| `shuffle` | Shuffles a list      | `array` (list): the list to be shuffled | `list`: the shuffled list |
| `unique_value_counter` | Generates a dictionary that contains occurrences of unique values | `arr` (list): the list that the dict needs to be generated on | `dict`: a dictionary that contains the occurrences of each unique value in a list |
