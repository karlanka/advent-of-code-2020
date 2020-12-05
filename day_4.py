from aoc_utils import get_input, get_input_no_line
import sys
import re

codes = ['byr','iyr','eyr','hgt','hcl','ecl','pid','cid']

def one(input):
    """
    >>> one(['ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm', 'iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884 hcl:#cfa07d byr:1929', 'hcl:#ae17e1 iyr:2013 eyr:2024 ecl:brn pid:760753108 byr:1931 hgt:179cm', 'hcl:#cfa07d eyr:2025 pid:166559648 iyr:2011 ecl:brn hgt:59in'])
    2
    """
    valid = 0
    for passport in input:
        pp_codes = [x[:3] for x in passport.split(' ') if x[:3] != 'cid']
        valid += len(pp_codes) == 7
    return valid


def validator(pp_dict):
    # check length there is 7 fields (would not catch if an unknown field is there...)
    if len(pp_dict) < 7:
        return False
    # year checks
    if not 1920 <= int(pp_dict['byr']) <= 2002:
        return False
    if not 2010 <= int(pp_dict['iyr']) <= 2020:
        return False
    if not 2020 <= int(pp_dict['eyr']) <= 2030:
        return False
    # eye check
    if pp_dict['ecl'] not in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
        return False
    # height check
    if pp_dict['hgt'][-2:] not in ('cm', 'in'):
        return False
    if 'cm' in pp_dict['hgt'] and not 150 <= int(pp_dict['hgt'][:-2]) <= 193:
        return False
    if 'in' in pp_dict['hgt'] and not 59 <= int(pp_dict['hgt'][:-2]) <= 76:
        return False
    # hair color check
    if not re.match(r'(#[a-f0-9]{6})', pp_dict['hcl']):
        return False
    # id check
    if not (pp_dict['pid'].isdigit() and len(pp_dict['pid']) == 9):
        return False
    
    return True

def two(input):
    """
    >>> two(['iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719','eyr:2029 ecl:blu cid:129 byr:1989 iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm', 'hcl:dab227 iyr:2012 ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277','eyr:1972 cid:100 hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926'])
    2
    """
    valid = 0
    for passport in input:
        pp_dict = {x[:3]:x[4:] for x in passport.split(' ') if x[:3] != 'cid'}
        valid += validator(pp_dict)
    return valid

def main():
    input = [x.replace('\n', ' ') for x in get_input_no_line(day=4).split('\n\n')]

    print("first:", one(input))
    print("second:", two(input))

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == '-t':
        import doctest
        doctest.testmod()
    else:
        main()