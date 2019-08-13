import itertools

##counter=itertools.count()
##print(next(counter))
##print(next(counter))

##counter=itertools.count(5,2)
##print(next(counter))
##print(next(counter))
##print(next(counter))

##data=[100,200,300,400]
##daily_data=list(zip(itertools.count(),data))
##print(daily_data)

        #zip_longest is hang your system don't run this tools
##data=[100,200,300,400]
##daily_data=itertools.zip_longest(itertools.count(),data)
##print(list(daily_data))

###counter=itertools.cycle([1,2,3])
##counter=itertools.cycle(['on','off'])
##print(next(counter))
##print(next(counter))
##print(next(counter))
##print(next(counter))
##print(next(counter))
##print(next(counter))


##counter=itertools.repeat(5)
##print(next(counter))
##print(next(counter))
##print(next(counter))
##print(next(counter))
##print(next(counter))
##print(next(counter))

##squere = map(pow,range(10),itertools.repeat(2))
##print(list(squere))

##squere = itertools.starmap(pow,[(0,2),(1,2),(2,2),(3,2)])
##print(list(squere))

##leters=['a','b','c','d']
##num=[1,2,3,4]
##word=["jaya","ram"]

##comb=itertools.combinations(leters,2)
##permu=itertools.permutations(leters,2)
#comb=itertools.combinations(leters,3)
#permu=itertools.permutations(leters,3)
#print(list(comb))
#print(list(permu))

##num=[1,2,3,4]
##sum_num=itertools.combinations(num,3)
##
##for i in (list(sum_num)):
##    #print(i)
##    if i[0]+i[1]+i[2]==6:
##        print(i)
####    if i[0]+i[1]==5:
####        print(i)

num=[1,2,3,4]
sum_num=itertools.permutations(num,3)

for i in (list(sum_num)):
    #print(i)
    if i[0]+i[1]+i[2]==6:
        print(i)
##    if i[0]+i[1]==5:
##        print(i)

##num=[1,2,3,4]
##result = itertools.product(num,repeat=3)
##for i in result:
##    print(i)


