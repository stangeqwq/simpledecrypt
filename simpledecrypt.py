#!/usr/bin/env python3

path = input("/path/to/file:")

# the frequency table created by analyzing character frequency in the first chapter of Harry Potter
# this may vary between text inputs, but the general pattern of having "e", "t", "a", etc. on top should be expected
# if you do not get a fully decrypted text, that's fine. Some patters should be made obvious upon decrypting regardless. This can be useful and revealing.
freqRef = {
  25 : "e",
  24 : "t",
  23 : "a",
  22 : "o",
  21 : "h",
  20 : "n",
  19 : "r",
  18 : "i",
  17 : "s",
  16 : "d",
  15 : "l",
  14 : "u",
  13 : "g",
  12 : "y",
  11 : "w",
  10 : "m",
  9 : "f",
  8 : "c",
  7 : "p",
  6 : "b",
  5 : "k",
  4 : "v",
  3 : "q",
  2 : "x",
  1 : "j",
  0 : "z"
}
freqTable = {
  "a" : 0,
  "b" : 0,
  "c" : 0,
  "d" : 0,
  "e" : 0,
  "f" : 0,
  "g" : 0,
  "h" : 0,
  "i" : 0,
  "j" : 0,
  "k" : 0,
  "l" : 0,
  "m" : 0,
  "n" : 0,
  "o" : 0,
  "p" : 0,
  "q" : 0,
  "r" : 0,
  "s" : 0,
  "t" : 0,
  "u" : 0,
  "v" : 0,
  "w" : 0,
  "x" : 0,
  "y" : 0,
  "z" : 0
}

# open file given in the input and start reading
with open(path, "r") as file:
    content = file.readlines()

    # create our frequency table along with it being sorted for easier comparison with reference dictionary
    for line in content:
        for char in line:
            if (char.isalpha() == True): freqTable[char.lower()] += 1
            else: continue

    sortedFreqT = {k: v for k, v in sorted(freqTable.items(), key=lambda item: item[1])}
    print(sortedFreqT)

    # start indexing the values so that it's easier to connect with the reference dictionary
    counter = 0
    for key in sortedFreqT:
        sortedFreqT[key] = counter 
        counter += 1

    print(sortedFreqT)

    # decrypt and write the result on an output text file
    output = open("decrypted.txt", "a")
    for line in content:
        for char in line:
            if (char.isalpha() == True): output.write(freqRef[sortedFreqT[char.lower()]])
            else: output.write(char)
    output.close()

