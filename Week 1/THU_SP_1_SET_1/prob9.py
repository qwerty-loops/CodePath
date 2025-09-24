def merge_alternately(word1, word2):
    str=""
    i,j=0,0
    while i<len(word1) and j<len(word2):
        str+=word1[i]
        i+=1
        str+=word2[j]
        j+=1

    # if i<len(word1):
    #     str+=word1[i:]

    # if j<len(word2):
    #     str+=word2[j:]

    str+= word1[len(word2):]
    str+= word2[len(word1):]

    return str

word1 = "wol"
word2 = "oze"
print(merge_alternately(word1, word2))

word1 = "hfa"
word2 = "eflump"
print(merge_alternately(word1, word2))

word1 = "eyre"
word2 = "eo"
print(merge_alternately(word1, word2))