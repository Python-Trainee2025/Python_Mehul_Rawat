words=input("enter two words separated by comma\n").split(',')
if (len(words[0])==len(words[1])):
    if sorted(words[0])==sorted(words[1]):
        print("Anagram")
    else:
        print("Not Anagram")
else:
    print("Not Anagram")
