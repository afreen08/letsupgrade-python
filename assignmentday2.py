#list
list1=[21,18,6,11,27,16,13]
list1.append(15) #append()
print(list1)
print(list1[1:4]) #slice()
print(list1*3)    #replicating()
print(list1.pop(2)) #pop()
list1.remove(13)   #remove()
print(list1)
list1.insert(1,2)  #insert()
print(list1)
del list1[3] #deletee()
print(list1)
print(max(list1))#maxmium()
print(min(list1)) #mimnimum()
list1.reverse() #reverse()
print(list1)
list1.sort() #sort()
print(list1)

#dictionary
d={'name':'brother','surname':'abdul','nickname':'stuart'}
print(d)
print(d.keys())
print(d.values())
print(d.items())
d["name"]="taufi" #update()
print(d)
print(len(d)) #length()
b=d.copy() #cpoy()
print(d)
d.clear() #clear()
print(d)

#sets
a={1,2,3,4}
b={5,6,3,8}
a.discard(3) #discard()
print(a)
a.add("ali") #add()
print(a)
k=a|b #union()
print(k)
p=a-b #difference of sets
print(p)
c=a<=b #compare sets
print(c)
c=b<=a
print(c)


#tuple
l=(10,20,30,40,50)
print(l)
print(l[1:4]) #slice()
print(len(l)) #length()
print(min(l))#minimum()           
print(max(l)) #maxmimum()
print(l*2) #replicating()


#string
a="jackiechan"
b="is a stuntman"
print(a+b)
print(a[2:])
c=b.index("a")
d="l"
print(b.count(d))
print(a.isalpha())
print(b.isalnum())
print(b.isdigit())
print(b.capitalize())
print(a.swapcase())
