def reverse_sentence(sentence):
    # return sentence[::-1]
    words = sentence.split()
    if len(words) == 1:
        return "".join(words)
    else:
        return " ".join(reversed(words))


sentence = "tubby little cubby all stuffed with fluff"
print(reverse_sentence(sentence))

sentence = "Pooh"
print(reverse_sentence(sentence))