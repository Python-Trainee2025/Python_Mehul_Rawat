sentence=input('enter your sentence:').lower()

character=list(sentence)

vowel=['a','e','i','o','u']

for v in vowel:
    count=character.count(v)
    print(f'{v} appears {count} times')