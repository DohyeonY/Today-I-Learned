# words = ['eat', 'tea', 'tae', 'ate', 'nat', 'nat', 'bat']

# d = {}

# for w in words :
#     t1 = sorted(w)
#     t = ''.join(t)
#     if t in d:
#         d[t].append(w)
#     else :
#         d[t] = [t]
        
# print(d)

# words = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']

# d = {}

# for w in words :
#     t = ''.join(sorted(w))
#     if t in d:
#         d[t].append(w)
#     else:
#         d[t] = [t]
# print(d)

words = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
d = {}
for w in words:
    t1 = sorted(w)
    t = ''.join(t1)
    # print(t1, t)
    if t in d:
        d[t].append(w)
    else:
        d[t] = [w]
print(d)