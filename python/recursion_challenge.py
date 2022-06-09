def factorial(n,answer=1):
    answer=answer
    if n==0:
        return answer
    else:
        if n>0:
            answer=answer * n
            return factorial(n-1,answer)


def palindrome(word):
    word=str(word)
    word=word.lower()
    word=''.join(e for e in word if e.isalnum())
    if len(word)== 1 or len(word)==0:
        return True
    else:
        if word[-1]==word[0]:
            word=word[1:-1]
            return palindrome(word)
        else: 
            return False
 
def bottles(num):
    num2=num-1
    if num == 2:
        print(f'''{num} bottles of beer on the wall, {num} bottles of beer. Take one down and pass it around, 1 bottle of beer on the wall.
1 bottle of beer on the wall, 1 bottle of beer. Take one down and pass it around, no more bottles of beer on the wall.
No more bottles of beer on the wall, no more bottles of beer. Go to the store and buy some more, 99 bottles of beer on the wall.''')
    if num == 1:
        print(f'''1 bottle of beer on the wall, 1 bottle of beer. Take one down and pass it around, no more bottles of beer on the wall. 
              No more bottles of beer on the wall, no more bottles of beer. Go to the store and buy some more, 99 bottles of beer on the wall.''')
    elif num>2:
        print(f'''{num} bottles of beer on the wall, {num} bottles of beer. Take one down and pass it around, {num2} bottles of beer on the wall.''')
        return bottles(num2)
    
        
bottles(10)

def roman_num(n, answer=''):
    numerals={
        'M': 1000,
        'CM': 900,
        'D': 500,
        'CD': 400,
        'C': 100,
        'XC': 90,
        'L': 50,
        'XL': 40,
        'X': 10,
        'IX': 9,
        'V': 5,
        'IV': 4,
        'I': 1,
    }
    
    if n!=0:
        for i in numerals:
            if n>=numerals[i]:
                answer+= i
                return roman_num(n-numerals[i],answer)
    else:
        return answer
        



