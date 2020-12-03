'''
--- Day 2: Password Philosophy ---

Your flight departs in a few days from the coastal airport; the easiest way down to the coast from here is via toboggan.

The shopkeeper at the North Pole Toboggan Rental Shop is having a bad day. "Something's wrong with our computers; we can't log in!" You ask if you can take a look.

Their password database seems to be a little corrupted: some of the passwords wouldn't have been allowed by the Official Toboggan Corporate Policy that was in effect when they were chosen.

To try to debug the problem, they have created a list (your puzzle input) of passwords (according to the corrupted database) and the corporate policy when that password was set.

For example, suppose you have the following list:

1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
Each line gives the password policy and then the password. The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid. For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.

In the above example, 2 passwords are valid. The middle password, cdefg, is not; it contains no instances of b, but needs at least 1. The first and third passwords are valid: they contain one a or nine c, both within the limits of their respective policies.

How many passwords are valid according to their policies?
'''

# Counts the number of valid passwords with the given validation function
def count_valid_psws(psw_list,validation_function):
    valid_psws = 0
    for input in psw_list:
        rule, psw = input.split(':')
        rule, psw = rule.strip(),psw.strip()
        if validation_function(rule,psw):
            valid_psws = valid_psws + 1
    return valid_psws

# Checks if password adhers to rule, returns true if valid and false if not.
def validate_psw_p1(rule,psw):
    result = False
    key_char_count = 0
    count, key_char = rule.split()
    min_count,max_count = count.split('-')
    for char in psw:
        if char == key_char:
            key_char_count = key_char_count + 1
    if key_char_count >= int(min_count) and key_char_count <= int(max_count):
        result= True
    return result
    
# Read input from textfile and save in list.
file = open('day2/input.txt','r')
input_list = file.read().split('\n')

print("Number of valid passwords:" + str(count_valid_psws(input_list,validate_psw_p1)))


'''
--- Part Two ---

While it appears you validated the passwords correctly, they don't seem to be what the Official Toboggan Corporate Authentication System is expecting.

The shopkeeper suddenly realizes that he just accidentally explained the password policy rules from his old job at the sled rental place down the street! The Official Toboggan Corporate Policy actually works a little differently.

Each policy actually describes two positions in the password, where 1 means the first character, 2 means the second character, and so on. 
(Be careful; Toboggan Corporate Policies have no concept of "index zero"!) Exactly one of these positions must contain the given letter. Other occurrences of the letter are irrelevant for the purposes of policy enforcement.

Given the same example list from above:

1-3 a: abcde is valid: position 1 contains a and position 3 does not.
1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.
How many passwords are valid according to the new interpretation of the policies?
'''
# Checks if password adhers to rule, returns true if valid and false if not.
def validate_psw_p2(rule,psw):
    result = False
    psw_len = len(psw)
    index, key_char = rule.split()
    index1,index2 = index.split('-')
    index1,index2 = int(index1), int(index2)
    index1_valid = checkIndex(index1,key_char,psw)
    index2_valid = checkIndex(index2,key_char,psw)
    
    if (index1_valid and not index2_valid) or (not index1_valid and index2_valid):
        result = True
    return result

# Checks if index is not out-of-bounds and if index position in string is equal to char, if so returns true otherwise returns false. 
def checkIndex(index,char,string):
    result = False
    if index > len(string):
        return result
    elif string[index-1] == char:
        result = True
    return result


print("Number of valid passwords:" + str(count_valid_psws(input_list,validate_psw_p2)))