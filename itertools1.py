import itertools
from collections import Counter

def get_state(person):
    return person['state']

people = [
    {'name':'jaya',
     'city':'tirupati',
     'state':'AP'
     },
    {'name':'raj',
     'city':'krishnagiri',
     'state':'TN'
     },
    {'name':'sonu',
     'city':'kolar',
     'state':'KA'
     },
    {'name':'jaya',
     'city':'tirupati',
     'state':'AP'
     },
    {'name':'perumal',
     'city':'krishnagiri',
     'state':'TN'
     },
    {'name':'dood',
     'city':'mehaboobnagar',
     'state':'TLG'
     },
    {'name':'ram',
     'city':'tirupati',
     'state':'AP'
     },
    {'name':'lanja',
     'city':'krishnagiri',
     'state':'TN'
     },
    {'name':'lovely',
     'city':'kolar',
     'state':'KA'
     }
    ]

person_group = itertools.groupby(people,get_state)
l=[]
for key,group in person_group:
    l.append(key)
#print(l)
cnt=Counter(l)
#print(cnt)
for i,j in cnt.items():
    print(i,j)
   # print(i[0],i[1])
    #print(key)

##    print(key)
##    for per in group:
##        print(per,end="")
##    print()
