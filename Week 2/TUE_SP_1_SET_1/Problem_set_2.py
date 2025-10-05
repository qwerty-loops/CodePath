# Question description
# Given a string s, find the first substring of length k that appears exactly twice in the string and return its
# starting index. If no such substring exists, return -1

# Example usage:
# Input: s = "abcabcabc" k = 3
# Expected Output: 0
# Example Usage 2:
# Input: s = "banana" k = 2
# Expected Output: 1


def substring(s,k):

    i=0
    substrd={}
    while i+k <=len(s):
        if s[i:i+k] not in substrd:
            # print(s[i:i+k])
            substrd[s[i:i+k]]=1
            i+=1
        else:
            # print(s[i:i+k])
            substrd[s[i:i+k]]+=1
            i+=1
    print(substrd)
    for i,v in substrd.items():
        if v==2 and i in s:
            return s.find(i)
    return -1

    # return max(substrd.items(),key = lambda i:i[1])
    
    # for k,v in substrd.items():
    #     if v>1:
    #         print (k)
        # elif v==1:
        #     return -1
    
    # print (s.find('na'))

print(substring("abcabcabc", 3))  # 1 ("bca")
print(substring("banana", 2))     # 1 ("an")
print(substring("aaaa", 2))       # -1 (since "aa" appears 3 times, not 2)
print(substring("abcabc", 3))     # 0 ("abc")
