#create a program to convert distance of kilometer into miles.
#1 kilometer = 0.621371

# distance_in_km = float(input("enter distance: "))
# convert_km_distance_into_miles = distance_in_km * 0.621371

# print(f"converstion of kilometer into miles is " ,convert_km_distance_into_miles)
from ast import And
from audioop import mul
from cgi import print_form
from re import A

# age =18
# language = "Python"
# print("2",age>=18)
# print("3",age>18)
# print("4", age>18 and language == "java")
# print("i am also printed because i am or operator", age ==18 or language=="Python")

# number = float(input("please enter the number : "))

# if number >0 :
#     print('number is positive')

# elif number <0:
#     print("number is negative")
# else:
#     print("number is 0")

#multiplication of table from 10 to 1

# number = int(input("enter the number to see its table from 10 to 1: "))

# count = 10
# while count<=1:
#     multiplaction = count* number
#     print(number ,"X" ,count ,"= ",multiplaction)
#     count = count-1


# languages=["pyton","java","swift","C","C++"]
# for character in languages:
#     languages=["pyton","java","swift","C","C++"]
#     if character==("C++"):
#      continue
#     if  character==("swift"):
#      continue
#     print(character)

# n = input("Enter Number to calculate sum")
# n = int (n)
# sum = 0
# for num in range(0, n+1, 1):
#  sum = sum+num
#  print("SUM of first ", n, "numbers is: ", sum )

# def average_marks_of_the_student(marks):
    
    
#     total_marks_obtained = sum(marks)

    
#     number_of_subjects = len(marks)
#     average_of_total_marks = total_marks_obtained / number_of_subjects
#     return average_of_total_marks
# marks = [55,65,77,85,90]
   

# average_marks = average_marks_of_the_student(marks)


# def compute_grade(average_marks):
#     if average_marks >= 80:
#         grade = "A"
#     elif average_marks >=60:
#         grade = "B"
#     elif average_marks >=50:
#         grade = "C"
#     else:
#         grade = "D"
#     return grade
# grade_obtained = compute_grade(average_marks)

# print("your average marks is ",average_marks,"and your grade is ",grade_obtained)
#compute addition with two given input from user

# def calculator():
#     input1  = int(input("enter number 1: "))
#     input2 = int(input("enter number 2:"))
#     operator = input("choose operation type: ")
#     if operator == "+":
#         return input1+input2 
#     elif operator =="-":
#         return input1-input2
    
#     elif operator =="*":
#         return input1*input2
#     elif operator =="/":
#         if input2 ==0:
#             print("please enter valid number 0 cannot be divided ")
#         else:
#             return input1/input2
#     return operator
    
# print(calculator())

# mixed_list =["hello",-34,"python","true"]
# print("1",mixed_list[-1])
# mixed_list[1]="Hi"
# print("2",mixed_list)
# mixed_tuple = (1,3,4,5)
# # mixed_tuple[1]=200
# print(mixed_tuple)
# #tuple cant be modified

# list_of_dict = {"jungle":"forest","lion":"wild","cat":"wild"}
# # list_of_dict.pop("cat")

# for value in list_of_dict:
#     print(list_of_dict[value])

# print(list_of_dict)

# # list_of_dict[0] this is not allowed in dict as it doesnt follow indices
# print(list_of_dict)
 
# string_slash = "he said, i will never go with \"aciee's brother"
# print(string_slash)


# input = "talk is cheap.show me the code"
# print("1",input[3])
# print("1",input[-3])
# print("3",input.replace("code","program"))


#  print("total_marks",total_marks)
#  print("average_marks",average_total_marks)


# numbers = [1,2,3,4,5,6]
# sum = 0
# mul =1
# for value in numbers:
#     mul *= value
#     sum += value
# print(value)
# print(sum)
# print(mul)
# print(f"the sum of numbers is{sum}")

#arbitrary arguments\

# def greet(*names):
#     for name  in  names:
#         print("hello",name)
        
# greet("rv","raj","awanish","mohit")

#factorial
def factorial(x):
    if x ==1:
        return 1
    if x ==0:
        return 1
    else:
        return (x*factorial(x-1))
x =5
print(f"the factorial of {x} is {factorial(x)} ")


        


