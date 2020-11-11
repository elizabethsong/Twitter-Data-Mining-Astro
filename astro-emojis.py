import bertmoticon
import csv
from csv import DictReader

# split up between reddit posts and tweets


#print(bertmoticon.emojis)
#ls_of_strings =  ["Weekly love tips: You might wonder if your eyes deceive you and if your ears interpret something correctly, too."]



with open('gemini.csv', newline='') as f:
    ls_of_strings = [row["text"] for row in DictReader(f)]
    #reader = csv.reader(f)
    #ls_of_strings = list(reader) # this is where u convert to list
print(ls_of_strings[:10])


# figure out how to get summary stats of bertmoticon
emojis = bertmoticon.infer(ls_of_strings, 4) # try 1 and see if less?
print("entering dictionary")
print(emojis)

dict = {}
for set in emojis:
    for emoji in set:
        if emoji in dict:
            dict[emoji] += 1
        else:
            dict[emoji] = 1

print(dict)
print(len(emojis))


"""
Aries:😂😭😍 {'😂': 11, '😭': 11, '😍': 11, '😊': 11, '🙏': 11}
Pisces: {'😂': 11, '😭': 11, '😍': 11, '😊': 11, '🙏': 11}
"""
