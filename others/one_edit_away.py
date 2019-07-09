'''
Test cases
    1) Input: Both empty strings
       Output: False
    2) Input: One string is more that one character longer that the other string
       Output: False
    3) Input: Both strings are the same length but differ in more than one character.
       Output: False
    4) Input: Both strings are the same length but differ in only one character.
       Output: True
    5) Input: One string is one character longer than second string and differ in more than one character.
       Output: False
    6) Input: One string is one character longer than second string and differ in only one character.
       Output: True
   
    abc ab ac bc cb
    abc de
'''

def are_one_edit_away(str1, str2):
    len1, len2 = len(str1), len(str2)
    if not len1 and not len2:
        return False
    if abs(len1 - len2) > 1:
        return False
    
    return compare(str1, str2)


def compare(str1, str2):
    edits = 0
    str1, str2 = (str1, str2) if len(str1) < len(str2) else (str2, str1)
    j = 0
    for i in range(len(str1)):
        if j >= len(str2) and edits == 1:
            return False
        while j < len(str2):
            if str1[i] == str2[j]:
                j += 1
                break
            else:
                edits += 1
            if edits > 1:
                return False
            j += 1
    
    return True

print(are_one_edit_away('', ''))
print(are_one_edit_away('ab', 'ba'))
print(are_one_edit_away('ab', 'ac'))
print(are_one_edit_away('', 'a'))
print(are_one_edit_away('ab', 'abc'))
print(are_one_edit_away('ab', 'acb'))
print(are_one_edit_away('aaa', 'abb'))
    
