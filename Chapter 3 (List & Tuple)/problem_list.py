# Find largest number in a list
list = [10, 20, 4, 45, 99]

max = list[0]

for i in list: 
        if  i >max:
            max=i

print("Largest element is:",max)



# Count even and odd numbers in a list

list=[2,5,7,6,8,7,1,0,525,63,85,7,59,5]


for i in range(len(list)):
      
      if i% 2==0:
            print(i,"is even")
      else:
            print(i,"is odd")




