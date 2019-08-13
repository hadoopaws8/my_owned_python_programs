from collections import Counter

l=[1,3,4,3,2,3,5,1,3]

cnt=Counter(l)
print(cnt)
print(cnt[3])
print(type(cnt))
li1=cnt.most_common()
print(li1)
print(type(li1))
