def piglatin(s):
    '''Starts with a vowel add "ay" to end
        does not start with vowel put first letter at end, add ay
    '''
    vowels = ['a','e','i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    piglater=''
    for word in s.split():
        if word[0] in vowels:
            piglater+=word + 'ay '
        else:
            piglater+=word[1:]+word[0]+'ay '
    return piglater

print ("What do you want to translate: ")
result = raw_input()

print (piglatin(result))