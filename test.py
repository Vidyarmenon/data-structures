name=["India","Australia","Germany"]
name.append("America")
print(name)

//output

['India', 'Australia', 'Germany', 'America']

name.insert(0,"Canada")
name.insert(2,"Swiss")
print(name)

//output

['Canada', 'India', 'Swiss', 'Australia', 'Germany', 'America']

tuple=(1,2,3,4,5,6)
print("tuple[0]=",tuple[0])
//output

tuple[0]= 1

print("tuple[1:3] = ",tuple[1:4])
//output

tuple[1:3] =  (2, 3, 4)

dict={1:"this",2:"is",3:"an",4:"example"}
del dict[2]
print(dict)
//output

{1: 'this', 3: 'an', 4: 'example'}
