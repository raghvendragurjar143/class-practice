# import random
# emp_name=["aman", "shivam", "rohan", "abhi"]
# res=random.choice(emp_name)
# print(res)
# emp_name=["aman", "shivam", "rohan", "abhi"]
# weight=[2,3,1,0]
# res=random.choice(emp_name,weights=weight , k=2)
# print(res)

## res=random.random()*1000  ## jitne 0 utne no. print krke dega 
# print(int(res))

##
# rand_int=random.randint(1,10) #isme jitna diff h utt hi ayega 
# rand_range=random.randrange(1,10) #not include 10 isme ek piche chlta h 
# print(rand_int)
# print(rand_range)


###wap to user max attemp=6
#each attemp random number generate
#random num .sum
#fix_value=150
#too farr
#too close,,,,,,,if else laga kr try krna h (work h practice krne ko ).


##shuffle()
# emp_name=["aman", "kamal","shivam","anshul"]
# random.shuffle(emp_name)
# print(emp_name)

# ##coupon code 
import random

def generate_coupon():
    a_to_z="abcdefghijklmnopqrstuvwxyz"
    num="1234567890"

    char=[random.choice(a_to_z).upper() for i in range(1,4)]
    num=[random.choice(num)for i in range(1,4)]

    print("".join(char+num))

for i in range(1,10):
    generate_coupon()


    #second method to coupon code

# import random

# def generate_coupon():
#     a_to_z = "abcdefghijklmnopqrstuvwxyz"
#     digits = "1234567890"

#     char = [random.choice(a_to_z).upper() for i in range(4)]
#     num = [random.choice(digits) for i in range(4)]

#     print("".join(char + num))

# for i in range(10):
#     generate_coupon()


