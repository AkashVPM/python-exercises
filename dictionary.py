students_data = [
      {
            "Name":"Akash S",
            "age":22,
            "Course":"production"   
      }
]

def new_student (name,age,course):
      new_student={}
      new_student["Name"]=name
      new_student["age"]=age
      new_student["Course"]=course
      students_data.append(new_student)

new_student("ram",22,"prod")
print(students_data)


