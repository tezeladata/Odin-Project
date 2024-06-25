# get character from ASCII Value
# 1
def get_char(c):
    
    myascii = {}
    myascii['32'] = ' '
    myascii['33'] = '!'
    myascii['34'] = '"'
    myascii['35'] = '#'
    myascii['36'] = '$'
    myascii['37'] = '%'
    myascii['38'] = '&'
    myascii['39'] = ''
    myascii['40'] = '('
    myascii['41'] = ')'
    myascii['42'] = '*'
    myascii['43'] = '+'
    myascii['44'] = ','
    myascii['45'] = '-'
    myascii['46'] = '.'
    myascii['47'] = '/'
    myascii['48'] = '0'
    myascii['49'] = '1'
    myascii['50'] = '2'
    myascii['51'] = '3'
    myascii['52'] = '4'
    myascii['53'] = '5'
    myascii['54'] = '6'
    myascii['55'] = '7'
    myascii['56'] = '8'
    myascii['57'] = '9'
    myascii['58'] = ':'
    myascii['59'] = ';'
    myascii['60'] = '<'
    myascii['61'] = '='
    myascii['62'] = '>'
    myascii['63'] = '?'
    myascii['64'] = '@'
    myascii['65'] = 'A'
    myascii['66'] = 'B'
    myascii['67'] = 'C'
    myascii['68'] = 'D'
    myascii['69'] = 'E'
    myascii['70'] = 'F'
    myascii['71'] = 'G'
    myascii['72'] = 'H'
    myascii['73'] = 'I'
    myascii['74'] = 'J'
    myascii['75'] = 'K'
    myascii['76'] = 'L'
    myascii['77'] = 'M'
    myascii['78'] = 'N'
    myascii['79'] = 'O'
    myascii['80'] = 'P'
    myascii['81'] = 'Q'
    myascii['82'] = 'R'
    myascii['83'] = 'S'
    myascii['84'] = 'T'
    myascii['85'] = 'U'
    myascii['86'] = 'V'
    myascii['87'] = 'W'
    myascii['88'] = 'X'
    myascii['89'] = 'Y'
    myascii['90'] = 'Z'
    myascii['91'] = '['
    myascii['92'] = '\\'
    myascii['93'] = ']'
    myascii['94'] = '^'
    myascii['95'] = '_'
    myascii['96'] = '`'
    myascii['97'] = 'a'
    myascii['98'] = 'b'
    myascii['99'] = 'c'
    myascii['100'] = 'd'
    myascii['101'] = 'e'
    myascii['102'] = 'f'
    myascii['103'] = 'g'
    myascii['104'] = 'h'
    myascii['105'] = 'i'
    myascii['106'] = 'j'
    myascii['107'] = 'k'
    myascii['108'] = 'l'
    myascii['109'] = 'm'
    myascii['110'] = 'n'
    myascii['111'] = 'o'
    myascii['112'] = 'p'
    myascii['113'] = 'q'
    myascii['114'] = 'r'
    myascii['115'] = 's'
    myascii['116'] = 't'
    myascii['117'] = 'u'
    myascii['118'] = 'v'
    myascii['119'] = 'w'
    myascii['120'] = 'x'
    myascii['121'] = 'y'
    myascii['122'] = 'z'
    myascii['123'] = '{'
    myascii['124'] = '|'
    myascii['125'] = '}'
    myascii['126'] = '~'
    
    if c in myascii:
        out = myascii[str(c)]
    else:
        out = chr(c)
    return out

# 2
def get_char(c):
  # Your code goes here ^_^
  return chr(c)

# 3
def get_char(c):
  c = chr(c)
  return c

# 4
def number_to_ascii_char(number):
    try:
        # Ensure the input is within the ASCII range (0-127)
        if 0 <= number <= 127:
            return chr(number)
        else:
            return "Error: Input number is out of the ASCII range (0-127)."
    except TypeError:
        return "Error: Input must be an integer."
    

# Find numbers which are divisible by given number
# 1
def divisible_by(numbers, divisor):
    return [x for x in numbers if x%divisor == 0]

# 2
def divisible_by(numbers, divisor):
    return [i for i in numbers if i%divisor == 0]

# 3
def divisible_by(numbers, divisor):
    div_by = []
    for num in numbers:
        if num % divisor == 0:
            div_by.append(num)
    return div_by

# 4
def divisible_by(numbers, divisor):
    return [n for n in numbers if n % divisor == 0]

# 5
def divisible_by(numbers, divisor):
    # Use list comprehension to filter numbers divisible by the divisor
    return [number for number in numbers if number % divisor == 0]


# Alternate capitalization
# 1
def capitalize(s):
    s = ''.join(c if i%2 else c.upper() for i,c in enumerate(s))
    return [s, s.swapcase()]

# 2
def capitalize(s):
    word = ""
    output = []
    for n in range(0, len(s)):
      if n%2==0:
        word = word+s[n].upper()
      else:
        word = word+s[n]
    output.append(word)
    output.append(word.swapcase())
    return output

# 3
def capitalize(s):
    return [''.join(c if (k + i) % 2 else c.upper() for i, c in enumerate(s)) for k in [0, 1]]

# 4
def capitalize(s):
    '''Returns two strings based on s. In one case, numbers at an 
    even index are capitalised, and in the second case, the opposite is true'''
    even = ''.join([letter.capitalize()  if i % 2 == 0 else letter for i, letter in enumerate(s)])
    odd = ''.join([letter.capitalize()  if i % 2 == 1 else letter for i, letter in enumerate(s)])
    return [even, odd]

# 5
def capitalize(s):
    even_index_cap = ''.join([char.upper() if i % 2 == 0 else char for i, char in enumerate(s)])
    odd_index_cap = ''.join([char.upper() if i % 2 != 0 else char for i, char in enumerate(s)])
    return [even_index_cap, odd_index_cap]


# Minimize Sum Of Array (Array Series #1)
# 1
def min_sum(arr):
    arr = sorted(arr)
    return sum(arr[i]*arr[-i-1] for i in range(len(arr)//2))

# 2
def min_sum(arr):
    arr.sort()
    left, right, res = 0, len(arr) - 1, 0
    while left < right:
        res += arr[left] * arr[right]
        left += 1
        right -= 1
    return res

# 3
def min_sum(arr):
    arr.sort()
    return sum(i * arr.pop() for i in arr)

# 4
def min_sum(arr):
    arr = sorted(arr)
    return sum([arr[i] * arr[-i-1] for i in range(int(len(arr)/2))])

# 5
def min_sum(arr):
    # Sort the array
    arr.sort()
    # Initialize the sum
    min_sum = 0
    # Iterate through the first half of the sorted array and multiply
    # each element with its corresponding element from the end
    for i in range(len(arr) // 2):
        min_sum += arr[i] * arr[-(i + 1)]
    return min_sum


# Sum consecutives
# 1
from itertools import groupby

def sum_consecutives(s):
    return [sum(group) for c, group in groupby(s)]

# 2
def sum_consecutives(s):
    prev = None
    x = []
    for i in s:
        if i == prev:
            x[-1] += i
        else:
            x.append(i)
        prev = i
    return x

# 3
def sum_consecutives(s):
    n,a = [s[0]],s[0]
    for i in range(1,len(s)):
        if s[i] != a:
            n.append(s[i])
            a = s[i]
        elif s[i] == a:
            n[-1] += a
    return n

# 4
from itertools import groupby

def sum_consecutives(s):
    return [sum(group) for key, group in groupby(s)]


# Sums of Parts
# 1
def parts_sums(ls):
    result = [sum(ls)]
    for item in ls:
        result.append(result[-1]-item)
    return result

# 2
def parts_sums(ls):
    L=[sum(ls)]
    for i in range(len(ls)):
        L.append(L[i]-ls[i])
    return L
  
# 3
from itertools import accumulate

def parts_sums(ls):
    return [0, *accumulate(reversed(ls))][::-1]

# 4
def parts_sums(ls):
    cop = list(ls)
    top = sum(ls)
    sums = 0
    parts = []
    for i in range(len(ls)):
        if len(parts) == 0:
            parts.append(top)
        else:
            parts.append(top - sums)
        sums += cop[i]
    parts.append(0)
    return parts

# 5
def parts_sums(ls):
    # Initialize the result list with the correct size filled with zeros
    result = [0] * (len(ls) + 1)
    
    # Calculate the total sum of the list
    total_sum = sum(ls)
    
    # Iterate over the list and populate the result list with the parts sums
    for i in range(len(ls)):
        result[i] = total_sum
        total_sum -= ls[i]
    
    # The last element of result should be 0, which is already set
    return result


# Word a10n (abbreviation)
# 1
import re

regex = re.compile('[a-z]{4,}', re.IGNORECASE)

def replace(match):
    word = match.group(0)
    return word[0] + str(len(word) - 2) + word[-1]

def abbreviate(s):
    return regex.sub(replace, s)

# 2
def abbreviate(s):
    mutate = lambda w: w[0] + str(len(w) - 2) + w[-1] if len(w) > 3 else w
    result, word = '', ''
    for char in s:
        if char.isalpha():
            word += char
        else:
            result += mutate(word) + char
            word = ''
    result += mutate(word)
    return result

# 3
import re

def abbreviate(s):
    repl = lambda w: w[0] + str(len(w) - 2) + w[-1]
    return re.sub('[a-zA-Z]{4,}', lambda m: repl(m.group(0)), s)

# 4
import re

def abbreviate(s):
    def abbrev_word(word):
        if len(word) < 4:
            return word
        return f"{word[0]}{len(word) - 2}{word[-1]}"
    
    # Use regex to find all words and substitute them with their abbreviation
    return re.sub(r'[a-zA-Z]{4,}', lambda match: abbrev_word(match.group(0)), s)


# Mean Square Error
# 1
def solution(a, b):
    return sum((x - y)**2 for x, y in zip(a, b)) / len(a)

# 2
import numpy as np


def solution(array_a, array_b):
    return np.array([(a - b) ** 2 for a, b in zip(array_a, array_b)]).mean()

# 3
def solution(array_a, array_b):
    k=[]
    a=len(array_a)
    b=len(array_b)
    if a==b:
        for i in range(a):
            k.append((abs(array_a[i]-array_b[i])**2))
        l1=sum(k)
        r=l1/a
        return r
    
# 4
def solution(array_a, array_b):
    return sum([((array_b[i] - array_a[i]) ** 2) for i in range(len(array_a))]) / len(array_a)

# 5
def average_squared_difference(arr1, arr2):
    # Ensure both arrays are of equal length
    if len(arr1) != len(arr2):
        raise ValueError("Both arrays must be of equal length")

    # Calculate the squared differences and their sum
    squared_differences = [(a - b) ** 2 for a, b in zip(arr1, arr2)]
    total_squared_difference = sum(squared_differences)

    # Calculate and return the average of the squared differences
    return total_squared_difference / len(arr1)


# ISBN-10 Validation
# 1
def valid_ISBN10(isbn):
    # Check format
    if len(isbn) != 10 or not (isbn[:-1].isdigit() and (isbn[-1].isdigit() or isbn[-1] == 'X')):
        return False
    # Check modulo
    return sum(i*(10 if x=='X' else int(x)) for i,x in enumerate(isbn, 1)) % 11 == 0

# 2
import re

def valid_ISBN10(isbn):
    return bool(re.match("\d{9}[\dX]$", isbn)) and sum("0123456789X".index(d) * i for i, d in enumerate(isbn, 1)) % 11 == 0

# 3
def valid_ISBN10(isbn: str) -> bool:
    try:
        digits = [*map(int, isbn[:-1]), 10 if isbn[-1] == 'X' else int(isbn[-1])]
        return len(digits) == 10 and sum(int(c) * i for i, c in enumerate(digits, 1)) % 11 == 0

    except ValueError:
        return False
    
# 4
# import pytest

# from solution import valid_ISBN10


tests = [
    ('1112223339', True),
    ('048665088X', True),
    ('1293000000', True),
    ('1234554321', True),
    ('1234512345', False),
    ('1293', False),
    ('X123456788', False),
    ('ABCDEFGHIJ', False),
    ('XXXXXXXXXX', False),
]


# @pytest.mark.parametrize(
#     "isbn, expected", tests
# )
def tests_valid_ISBN10(isbn, expected):
    assert valid_ISBN10(isbn) == expected

# 5
def valid_ISBN10(isbn):
    # Remove any hyphens from the ISBN (if present)
    isbn = isbn.replace('-', '')
    
    # Check if the length is exactly 10
    if len(isbn) != 10:
        return False
    
    # Check if the first 9 characters are digits
    if not isbn[:9].isdigit():
        return False
    
    # Check if the last character is either a digit from 0-9 or 'X'
    if not (isbn[9].isdigit() or isbn[9] == 'X'):
        return False
    
    # Calculate the ISBN-10 check digit
    check_digit = 10 if isbn[9] == 'X' else int(isbn[9])
    
    # Calculate the weighted sum modulo 11
    weighted_sum = sum((i + 1) * int(isbn[i]) for i in range(9))
    return weighted_sum % 11 == check_digit


# Least Common Multiple
# 1
from math import gcd
def lcm(*args):
    lcm=1
    for x in args:
        if x!=0:
            lcm=lcm*x//gcd(lcm,x)
        else:
            lcm=0
    return lcm   

# 2
# def lcm(*args):
#     gcd = lambda m,n: m if not n else gcd(n,m%n)
#     return reduce( lambda x, y: x*y/gcd(x, y), args)

# 3
def lcm(*args):
    args = set(args)  
    if 0 in args:
        return 0
    x = max(args)
    y = x
    args.remove(x)
    while any(x % z for z in args):
        x += y
    return x

# 4
from fractions import gcd


# def lcm(*args):
#     return reduce(lambda first, second: first * second / gcd(first, second), args)

# 5
import math

def lcm(*args):
    # Handle the case when no arguments are provided
    if not args:
        return 1
    
    # Handle the case when any argument is 0
    if 0 in args:
        return 0
    
    # Function to calculate LCM of two numbers using GCD
    def lcm_two_numbers(a, b):
        return abs(a * b) // math.gcd(a, b)
    
    # Calculate LCM of all arguments iteratively
    result = args[0]
    for num in args[1:]:
        result = lcm_two_numbers(result, num)
    
    return result


# Human readable duration format
# 1
times = [("year", 365 * 24 * 60 * 60), 
         ("day", 24 * 60 * 60),
         ("hour", 60 * 60),
         ("minute", 60),
         ("second", 1)]

def format_duration(seconds):

    if not seconds:
        return "now"

    chunks = []
    for name, secs in times:
        qty = seconds // secs
        if qty:
            if qty > 1:
                name += "s"
            chunks.append(str(qty) + " " + name)

        seconds = seconds % secs

    return ', '.join(chunks[:-1]) + ' and ' + chunks[-1] if len(chunks) > 1 else chunks[0]

# 2
def format_duration(seconds):
    if seconds == 0: return "now"
    units = ( (31536000, "year"  ), 
              (   86400, "day"   ),
              (    3600, "hour"  ),
              (      60, "minute"),
              (       1, "second") )
    ts, t = [], seconds
    for unit in units:
        u, t = divmod(t, unit[0])
        ts += ["{} {}{}".format(u, unit[1], "s" if u>1 else "")] if u != 0 else []
    return ", ".join([str(d)for d in ts[:-1]]) + (" and " if len(ts)>1 else "") + ts[-1]

# 3
def format_duration(s):
    dt = []
    for b, w in [(60, 'second'), (60, 'minute'), (24, 'hour'), (365, 'day'), (s+1, 'year')]:
        s, m = divmod(s, b)
        if m: dt.append('%d %s%s' % (m, w, 's' * (m > 1)))
    return ' and '.join(', '.join(dt[::-1]).rsplit(', ', 1)) or 'now'

# 4
def format_duration(seconds):
    if seconds == 0:
        return "now"
    
    # Define the number of seconds in each unit of time
    YEAR_SECONDS = 365 * 24 * 60 * 60
    DAY_SECONDS = 24 * 60 * 60
    HOUR_SECONDS = 60 * 60
    MINUTE_SECONDS = 60
    
    # Calculate years, days, hours, minutes, seconds
    years = seconds // YEAR_SECONDS
    seconds %= YEAR_SECONDS
    
    days = seconds // DAY_SECONDS
    seconds %= DAY_SECONDS
    
    hours = seconds // HOUR_SECONDS
    seconds %= HOUR_SECONDS
    
    minutes = seconds // MINUTE_SECONDS
    seconds %= MINUTE_SECONDS
    
    result = []
    
    if years > 0:
        result.append(f"{years} year" + ("s" if years > 1 else ""))
    if days > 0:
        result.append(f"{days} day" + ("s" if days > 1 else ""))
    if hours > 0:
        result.append(f"{hours} hour" + ("s" if hours > 1 else ""))
    if minutes > 0:
        result.append(f"{minutes} minute" + ("s" if minutes > 1 else ""))
    if seconds > 0:
        result.append(f"{seconds} second" + ("s" if seconds > 1 else ""))
    
    # Join the result with appropriate separators
    if len(result) == 1:
        return result[0]
    else:
        return ', '.join(result[:-1]) + ' and ' + result[-1]