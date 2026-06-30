#. Switch values of two integers.

#a=5
#b=10

#a,b=b,a

#print("a =",a)
#print("b =",b)

#Switch values of two strings (characters) 
#a = input("Enter first character: ")
#b = input("Enter second character: ")

#a, b = b, a

#print("After swapping:")
#print("a =", a)
#print("b =", b)

#Switch one string value with one integer value 
name = "Rohan"
age = 26

name, age = age, name

print(name)
print(age)

## Update balance after withdrawal 
balance = 5000
withdrawal_amount = 1200

balance -= withdrawal_amount
print("Updated balance:", balance)

#Increase shopping cart items by 3 
cart_items =5
cart_items +=3
print("updated card items:", cart_items)

##calculate student percentage.
marks_obtained =400
total_marks = 500
percentage =(marks_obtained / total_marks) * 100
print("percentage:",percentage)

##. Calculate average of 3 numbers 
num1 =40
num2 =50
num3 =60
average =(num1 + num2 + num3) / 3
print("average:",average)

## Calculate profit or loss percentage 
cost_price =1000
sheling_price =1200
profit = sheling_price -cost_price
profit_percentage = (profit / cost_price) * 100
print("Profit percentage:", profit_percentage)

str1="python"
new_str=""
for i in str1:
    if i not in "aeiou":
        new_str+=i
        print(new_str)


        #find vowels
        str1="this is python"
        vowels = "aeiou"
        found_vowels = ""
        for i in str1:
            if i in vowels:
                found_vowels += i
        print("Vowels found:", found_vowels)

        #find numbers in string.
        str1 ="this is python 123"
        find_digits = ""
        for i in str1:
            if i.isdigit():
                find_digits += i
        print("Digits found:", find_digits)

#ood even print
str1=[22,43,24,55,78,90,33,44,66]
new_list=[]
for i in str1:
    if i % 2 == 0:
        new_list.append(f"{i} is even")
    else:
        new_list.append(f"{i} is odd")
print(new_list)

#reverse string first method .
lis = ["python programming"]
new_string = ""
for i in lis[0]:
    new_string = i + new_string 
print(new_string)

#reverse string .type two methods.
str1=["python programming"]
for i in str1:
    print(i[::-1])

#reverse word in string, by using endwith,,startswith method.
str1=["python programming"]
print(str1[0].endswith("ing"))
print(str1[0].startswith('py'))

##nested dictionary.
student = {
    "name": "raghav gurjar",
    "subjects": {
        "maths": 90,
        "science": 85,
        "english": 90
    }
}

print(student["subjects"]["maths"])


####while loop practice .
num=(1,4,8,9,10,20,26,)
print (num)
print (loop ended)

#3 
str1="this is python programming"

for char in str1:
    print(char)
else:
    print("END")
               