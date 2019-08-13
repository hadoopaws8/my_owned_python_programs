st="Hi Jayaram how are you"
ls=st.split()
print(st)
ls1=[]
#s=" "
for i in ls:
    ls1.append(i[::-1])
#print(ls1)
s=" ".join(ls1)
print(s)
