sentence=input("Give us your thoughts\n").split(" ")
unique_word=[]
for word in sentence:
    if word not in unique_word:
        unique_word.append(word)
    # else:
    #     unique_word.remove(word)
print(unique_word)


# unique_words=set(sentence)
# print(len(unique_words))
