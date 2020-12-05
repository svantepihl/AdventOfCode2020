'''
--- Day 4: Passport Processing ---

You arrive at the airport only to realize that you grabbed your North Pole Credentials instead of your passport. While these documents are extremely similar, North Pole Credentials aren't issued by a country and therefore aren't actually valid documentation for travel in most of the world.

It seems like you're not the only one having problems, though; a very long line has formed for the automatic passport scanners, and the delay could upset your travel itinerary.

Due to some questionable network security, you realize you might be able to solve both of these problems at the same time.

The automatic passport scanners are slow because they're having trouble detecting which passports have all required fields. The expected fields are as follows:

byr (Birth Year)
iyr (Issue Year)
eyr (Expiration Year)
hgt (Height)
hcl (Hair Color)
ecl (Eye Color)
pid (Passport ID)
cid (Country ID)
Passport data is validated in batch files (your puzzle input). Each passport is represented as a sequence of key:value pairs separated by spaces or newlines. Passports are separated by blank lines.

Here is an example batch file containing four passports:

ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
The first passport is valid - all eight fields are present. The second passport is invalid - it is missing hgt (the Height field).

The third passport is interesting; the only missing field is cid, so it looks like data from North Pole Credentials, not a passport at all! Surely, nobody would mind if you made the system temporarily ignore missing cid fields. Treat this "passport" as valid.

The fourth passport is missing two fields, cid and byr. Missing cid is fine, but missing any other field is not, so this passport is invalid.

According to the above rules, your improved system would report 2 valid passports.

Count the number of valid passports - those that have all required fields. Treat cid as optional. In your batch file, how many passports are valid?
'''
input = '''
byr:2010 pid:#1bb4d8 eyr:2021 hgt:186cm iyr:2020 ecl:grt

pid:937877382 eyr:2029
ecl:amb hgt:187cm iyr:2019
byr:1933 hcl:#888785

ecl:hzl
eyr:2020
hcl:#18171d
iyr:2019 hgt:183cm
byr:1935

hcl:#7d3b0c hgt:183cm cid:135
byr:1992 eyr:2024 iyr:2013 pid:138000309
ecl:oth

ecl:hzl
hgt:176cm pid:346059944 byr:1929 cid:150 eyr:1924 hcl:#fffffd iyr:2016
'''
class Passport:
    birth_year  = None
    issue_year = None
    expiration_year = None
    height = None
    hair_color = None
    eye_color = None
    passport_id = None
    country_id = None

    def __init__(self,field_list):
        self.parse_list_to_passport(field_list)

    def add_data(self,string):
        field,value = string.split(':')
        if field == 'byr':
            self.birth_year = value
        elif field == 'iyr':
            self.issue_year = value
        elif field == 'eyr':
            self.expiration_year = value
        elif field == 'hgt':
            self.height = value
        elif field == 'hcl':
            self.hair_color = value
        elif field == 'ecl':
            self.eye_color = value
        elif field == 'pid':
            self.passport_id = value
        elif field == 'cid':
            self.country_id = value
        else: 
            print(field + ' is not a valid field!')

    def parse_list_to_passport(self,field_list):
        for field in field_list:
            self.add_data(field)

    def validate_1(self):
        valid = True
        if self.birth_year == None:
            valid = False
        if self.issue_year == None:
            valid = False
        if self.expiration_year == None:
            valid = False
        if self.height == None:
            valid = False
        if self.hair_color == None:
            valid = False
        if self.eye_color == None:
            valid = False
        if self.passport_id == None:
            valid = False
        return valid

    def validate_2(self):
        valid = True
        if not validate_byr(self.birth_year):
            valid = False
        if not validate_iyr(self.issue_year):
            valid = False
        if not validate_eyr(self.expiration_year):
            valid = False
        if not validate_hgt(self.height):
            valid = False
        if not validate_hcl(self.hair_color):
            valid = False
        if not validate_ecl(self.eye_color):
            valid = False
        if not validate_pid(self.passport_id):
            valid = False
        return valid

'''
--- Part Two ---

The line is moving more quickly now, but you overhear airport security talking about how passports with invalid data are getting through. Better add some data validation, quick!

You can continue to ignore the cid field, but each other field has strict rules about what values are valid for automatic validation:

byr (Birth Year) - four digits; at least 1920 and at most 2002.
iyr (Issue Year) - four digits; at least 2010 and at most 2020.
eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
hgt (Height) - a number followed by either cm or in:
If cm, the number must be at least 150 and at most 193.
If in, the number must be at least 59 and at most 76.
hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
pid (Passport ID) - a nine-digit number, including leading zeroes.
cid (Country ID) - ignored, missing or not.
Your job is to count the passports where all required fields are both present and valid according to the above rules. Here are some example values:
'''
import re
def validate_byr(byr):
    if not byr == None and len(byr) == 4:
        if int(byr) in range(1920,2003):
            return True
    return False


def validate_iyr(iyr):
    if not iyr == None and len(iyr) == 4:
        if int(iyr) in range(2010,2021):
            return True
    return False


def validate_eyr(eyr):
    if not eyr == None and len(eyr) == 4:
        if int(eyr) in range(2020,2031):
            return True
    return False


def validate_hgt(hgt):
    cm = re.compile("\d+cm")
    inch = re.compile("\d+in")
    if not hgt == None:
        if cm.match(hgt):
            if int(hgt[:-2]) in range(150,194):
                return True
        elif inch.match(hgt):
            if int(hgt[:-2]) in range(59,77):
                return True
    return False


def validate_hcl(hcl):
    hcl_regex = re.compile('(#[a-fA-F0-9]{6})')
    if not hcl == None and len(hcl) == 7:
        if hcl_regex.match(hcl):
            return True
    return False

def validate_ecl(ecl):
    valid_colors = ['amb','blu','brn','gry','grn','hzl','oth']
    if not ecl == None and len(ecl) == 3:
        if ecl in valid_colors:
            return True
    return False

def validate_pid(pid):
    pid_regex = re.compile('([0-9]{9})')
    if not pid == None and len(pid) == 9:
        if pid_regex.match(pid):
            return True
    return False


# Read input into list of strings
file = open('day4/input.txt','r')
input = file.read().split('\n\n')

# Parse strings into list of strings
passport_list = [string.split() for string in input]

# List to store password objects in and create counters for valid passwords
passports = []
valid_passports_part1 = 0
valid_passports_part2 = 0


for field_list in passport_list:
    temp = Passport(field_list)
    passports.append(temp)
    if temp.validate_1() == True:
        valid_passports_part1 += 1
    if temp.validate_2() == True:
        valid_passports_part2 += 1



print('Valid passwords part 1: ' + valid_passports_part1)
print('Valid passwords part 2: ' + valid_passports_part2)

    










    




