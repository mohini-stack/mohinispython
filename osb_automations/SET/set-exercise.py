#Create a new set
#Note that duplicas are discarded in sets
myset={23,42,3,2,12,12,'g'}
print(type(myset))
print(myset)
#Creating empty set
emptyset=set()
emptyset
#We can remove duplicas from list using set
list=[1,3,3,1,3,6]
new=set(list)
print(new)
#membership is done using in & not in operators
print(7 in new)
print(7 not in new)
#To add single element in set , use add method
new.add(7)
print(7 in new)
#Adding new element to set makes no change nor does it shows any error
#multiple elements can be added using update method
new.update([2,3,4,5])
print(new)
#Two methods are there to remove elements from the set remove & discards
new.remove(7)
new.discard(4)
new.discard(4)
#Shallow copying means copying objects
