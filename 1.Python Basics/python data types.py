i=10  
s="Hi Python"  
f = 10.5  
print(type(i))  
print(type(s))  
print(type(f))

print(type(True))  
print(type(False))

c = 1+3j  
print("The type of c", type(c))  
print(" c is a complex number", isinstance(1+3j,complex))


list1  = [1, "hi", "Python", 2]    
#Checking type of given list  
print(type(list1))  
  
#Printing the list1  
print (list1)


tup  = ("hi", "Python", 2)    
# Checking type of tup  
print (type(tup))    
  
#Printing the tuple  
print (tup)


d = {1:'Jimmy', 2:'Alex', 3:'john', 4:'mike'}     
  
# Printing dictionary  
print (d)

# Creating Empty set  
set1 = set()  
  
set2 = {'James', 2, 3,'Python'}  
  
#Printing Set value  
print(set2)


# tuple of numbers
nu = (1, 2, 3, 4, 5, 6, 7, 8, 9)
 
# converting tuple to frozenset
fnum = frozenset(nu)
 
# printing details
print("frozenset Object is : ", fnum)


typeOfNone = None 
print(type(typeOfNone))

for i in range(2,20,2):
     print(i)

