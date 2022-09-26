import numpy as np

textwidth = 16

words = ["Check", "out", "these", "9", "hilarious", "things", "Purdue", "Pete", "was", "caught", "doing.", "I",
         "couldn't", "believe", "number", "5!"]


def badness(line, textwidth):

    # Number of gaps
    length_line = len(line) - 1

    for word in line:
        length_line += len(word)

    if length_line <= textwidth:
        if "5!" in line:
            return 0


    return (textwidth - length_line) ** 2

DP = [0]*(len(words))


for i in range(len(words)-1,-1,-1):
    minum = 999
    minEnd = -1

    for j in range(i, len(words)):
        iTojBadness = badness(words[i:j + 1], textwidth)
        try:
            cost = iTojBadness + DP[j + 1]
        except Exception:
            cost = iTojBadness
        if cost < minum:

            minum = cost





    DP[i] = minum

print(DP[0])
