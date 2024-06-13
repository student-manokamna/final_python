
'''
9. Write a python program that checks if a substring is present in a given
string.
'''

def is_substring_present(main_strg, substrg):
    if substrg in main_strg:
        return True
    else:
        return False
main_strg = input("Enter the main string: ")
substrg= input("Enter the substring to check for: ")

if is_substring_present(main_strg, substrg):
    print("The substring is present in the main string.")
else:
    print("The substring is not present in the main string.")
