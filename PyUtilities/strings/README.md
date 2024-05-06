
# String API Reference

this subpackage contains utility methods for strings

| Function | Description                                                       | Parameters                          | Returns               |
|---------------|-------------------------------------------------------------------|-------------------------------------|-----------------------|
| `are_anagrams` | Checks if two strings are anagrams of each other                 | `str1` (str): the first string<br>`str2` (str): the second string you need to compare the first string to | `bool`: True if the two strings are anagrams, False if not. |
| `censor_string` | Censors all the swear words in a string                           | `string` (str): the string that needs to be censored<br>`censor_char` (str): the character that replaces the swear word in the string<br>`custom_swear_words` (list): a list of your own words that you would like to censor (replaces the default list of swear words)<br>`addition_swear_words` (list): a list of words that get added to the already existing default swear words | `str`: the fully censored string |
| `format_num` | Makes a number more readable by adding commas or by shortening it | `num` (int): the number that needs to be formatted or shortened (more readable) | `str`: the formatted or shortened string |
| `replace_one` | Replaces one occurrence of a value, instead of multiple occurrences | `string` (str): the string that has the characters that needs to be replaced<br>`replace_char` (str): the character that needs to be replaced in the string<br>`char` (str): the character that `replace_char` needs to be replaced with | `str`: the newly created string with the `char` removed from it |
| `to_title_case`  | Converts the first letter of each word in a sentence to uppercase, while converting all other letters to lowercase | `sentence` (str): the string/sentence you want to change | `str`: the string/sentence with the first letter of each word uppercased and all letters lowercased |
