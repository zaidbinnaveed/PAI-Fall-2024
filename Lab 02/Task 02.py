word = (str(input("Enter a word: ")))
size=len(word)
vowels = {'a','e','i','o','u','A','E','I','O','U'}
if(size>0):
    last_letter=word[-1]
    if(last_letter in vowels):
        print(f"The last letter {last_letter} is a vowel")
    elif(last_letter.isalpha()):
        print(f"The last letter {last_letter} is a consonant")
    else:
        print(f"The last letter {last_letter} is neither a vowel nor a consonent")
        
    
    
        
    
    
