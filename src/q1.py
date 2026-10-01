"""HW5 Question 1

Please write a function called replace_word() that takes a sentence and returns a version of 
the sentence with all occurrences of specified words replaced with new specified words.

replace_word() should take a sentence and any number of pairs of old and new words to replace.
Its first argument should always be required (the sentence to modify).
The remaining arguments should be pairs of old and new words to replace. The client can pass any
number of old and new word pairs.

If the client passes an odd number of old and new word pairs, the last word without a pair will 
be ignored.

Example usage:
replace_word("drums drums guitar drums", "drums", "piano") -> "piano piano guitar piano"
replace_word("drums drums guitar drums", "drums", "piano", "guitar", "violin") -> 
        "piano piano violin piano"
replace_word("drums drums guitar drums", "drums", "piano", "piano", "violin") -> 
        "violin violin guitar violin"
replace_word("drums drums guitar drums") -> "drums drums guitar drums"

Notice: Replacements are done left to right. The order of replacements matters.
For example, in the third usage example above, "drums" is replaced with "piano" first, and then 
"piano" is replaced with "violin".
"""
