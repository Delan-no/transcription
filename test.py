# words = 'His e-mail is q-lar@freecodecamp.org'
# pieces = words.split()
# parts = pieces[3].split('-')
# # n = parts[1]
# print(parts)

# dict = {"Fri": 20, "Thu": 6, "Sat": 1}
# dict["Thu"] = 13
# dict["Sat"] = 2
# dict["Sun"] = 9

# print(dict)

# counts = { 'quincy' : 1 , 'mrugesh' : 42, 'beau': 100, '0': 10}
# print(counts.get('kris', 0))

# d = dict()
# d['quincy'] = 1
# d['beau'] = 5
# d['kris'] = 9
# for (k,i) in d.items():
#     print(k, i)

import re
s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
lst = re.findall('\\S+@\\S+', s)
print(lst)