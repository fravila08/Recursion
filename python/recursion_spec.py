# Write your unit tests here
##This are all the test for Palindrome
from recursion_challenge import roman_num
from recursion_challenge import palindrome
from recursion_challenge import factorial


print("These are all the Palindrome Challenges")
print(palindrome('racecar') == True)
print(palindrome('Noon') == True)
print(palindrome('ciVic') == True)
print(palindrome('nice') == False)
print(palindrome(434) == True)
print(palindrome(123) == False)
print(palindrome('bomb') == False)
print(palindrome('Sore was I ere I saw Eros.') == True)
print(palindrome('A man, a plan, a canal -- Panama') == True)


print('These are the test cases for Roman Numeras')
print(roman_num(1) == 'I')
print(roman_num(3) == 'III')
print(roman_num(4) == 'IV')
print(roman_num(3944)=='MMMCMXLIV')

print('These are the test cases for Factorial')
print(factorial(8) == 40320)
print(factorial(18) == 6402373705728000)
print(factorial(45) == 119622220865480194561963161495657715064383733760000000000)