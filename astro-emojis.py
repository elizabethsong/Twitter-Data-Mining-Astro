import bertmoticon
import csv

# split up between reddit posts and tweets


#print(bertmoticon.emojis)
#ls_of_strings =  ["angry", "anger", "hate"]


with open('aries.csv', newline='') as f:
    reader = csv.reader(f)
    ls_of_strings = list(reader) # this is where u convert to list
print(ls_of_strings[:10])

# figure out how to get summary stats of bertmoticon
emojis = bertmoticon.infer(ls_of_strings, 5)
print("entering dictionary")

dict = {}
for set in emojis:
    for emoji in set:
        if emoji in dict:
            dict[emoji] += 1
        else:
            dict[emoji] = 1
#print(emojis)
print(dict)


"""
Aries:😂😭😍 {'😂': 11, '😭': 11, '😍': 11, '😊': 11, '🙏': 11}
Pisces: {'😂': 11, '😭': 11, '😍': 11, '😊': 11, '🙏': 11}
"""
