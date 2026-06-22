    #waf to remove last word from string#coplete ......
#waf to remove words if vowel present from string
#waf to count total white space in string
#waf to extract only numbers from string
#waf to remove all whitespace from stringwhitespace, 
# waf to print all the words in string which are palindrome
#waf to print all special symbols from string.
#waf to reverseall words of string.
#
#print("Hello, World!")

#waf to remove last word from string#
str1="this is a pythn code123 in vs verson-35 address noida-11096"
print(str1.endswith("noida-11096"))

##waf to remove words if vowel present from string
data_list=['This','is','python', 'for','data-science']
emp_list=[]
con="abcdfghjklmnpqrstvwxyz"
for i in data_list:
    for c in con:
        i=i.lower().replace(c,'')
    emp_list.append(i)
print(emp_list)

#waf to count total white space in string
my_string = "this is our python class"
total_spaces = sum(1 for char in my_string if char.isspace())
print(total_spaces)

#waf to extract only numbers from string
str1="this is a pythn code123 in vs verson-35 address noida-11096"
numbers = ''.join(filter(str.isdigit, str1))
print(numbers)

#waf to remove all whitespace from stringwhitespace, 
str1="this is a pythn code123 in vs verson-35 address noida-11096"
new_str = str1.replace(" ", "")
print(new_str)
#second method to remove all whitespace from string
text="this is a pythn code123 in vs verson-35 address noida-11096"
result = ''.join(text.split())
print(result)


#waf to print all special symbols from string.
str1="this is$ a pythn$ code123$ in vs verson-35$ address noida-11096$"
for char in str1:
    if not char.isalnum() and not char.isspace():
        print(char, end=' ')


        #waf to reverseall words of string.
str1="this is a pythn code123 in vs verson-35 address noida-11096"
words = str1.split()
reversed_words = [word[::-1] for word in words]
print(' '.join(reversed_words))