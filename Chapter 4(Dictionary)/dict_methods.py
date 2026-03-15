marks = {
     "Maths": 80,
     "Science": 90,
     "Social Science": 86
}

print("Hello World ")
print("Dictionary Methods")
print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Maths": 88, "English": 90})
print(marks)
print(marks.get("Dhruv")) 
print(marks.get("Maths")) 

print(marks.get("Dhruv3"))
print(marks.popitem()) 

 


 # print key values and dictionary

student={
  "marks": 86,
     "name": "Dhruv",
     "age": 20,
     "city": "Delhi",
     "country": "India",
     "language": "Python",
     "hobby": "Coding",
     "favorite_color": "Blue"
}


print(student.keys())
print(student.values())


# Count frequency of an elemnets using dictionary

freq={}
numbers = [1, 2, 2, 3, 3, 3, 4, 4,4,4]


for num in numbers:
    freq[num] = numbers.count(num)

print(freq)