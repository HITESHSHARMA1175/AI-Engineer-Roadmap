# --- Exercise 1: Variables and Strings ---
# Create a variable to hold your name and print a greeting.

name = "Hitesh"
greeting = f"Hello, {name}! Welcome to Day 1 of your AI Engineer journey."
print(greeting)

# --- Exercise 2: Variables and Strings ---
# Create a variable and find the length of it's charecter

msg='hello world'
print(len(msg))

# here i learn how to print a specific word of any string
print(msg[0])
print(msg[4])

# here i learn about slishing
print(msg[7:])

# here i learn about lower and uper case printing
print(msg.lower())
print(msg.upper())

# here i learn about how to count charcter or word in your sting
print(msg.count("l"))

# here i learn about how tol find any char or word index
print(msg.find("l"))

# if it not in your string it will return -1
print(msg.find('a'))

# here i learn about how to replace any thing in your string
# note that i never repalce origenal value it create a new for it
# origenal remans same
new_msg=msg.replace("hello","namste")
print(new_msg)

# here i learn about how to concatinate tow or maore sting
first="hello"
second="hitesh"
new=first+second
print(new) #but here wo see that there is no space or comma 

new=first+", "+second
print(new)
# we can add somtin by us

new=first+", "+second+", welcom!"
print(new)

# insted of this we can make a formate alao like this by using the format()
new='{}, {}, welcome!'.format(first,second)
print(new)

# we can also write it somting like this by the f string
new=f'{first}, {second}, welcome!'
print(new)
# here intresting thig we direct make upper or lower what want in this
new=f'{first}, {second.upper()}, welcome!'
print(new)

# here by the dir() function we can cheak all about any string what attributs and ethod are applyed on that
# print(dir(msg))

# if we want to learn more about the attributs and functions then write this
# print(help(str)) 
# the help() will give you discription about method and what will it dose (this function is realy graet it will give all infor cheak it diffinetly)

print("\n--- Arithmetic Operations ---\n")

# here learn how to know tpye
num=3
print(type(num))

num=1.33
print(type(num))

# addition substration multiplication division
print(3+5)
print(1-4)
print(4*5)
print(3/4)

# power or exponent oprater **
print(7**3)
# modulus
print(3%2)

# incriment and dicriment
num=1
num=num+1
print(num)

num=4
num= num-2
print(num)

# absolute of any value it will give positive
print(abs(-10.66))

# round off any num by round()
print(round(3.45)) #it will give you full rond of 3
print(round(3.45 , 1)) #it will give you 3.5

# airhmatic opration
print(3<2) #false
print(3>1) #true
print(3==2) #false
print(3!=2) #true
print(3>=2)#true
print(2<=1)#false


# here somting looking like integer but string
num_1='100'
num_2='200'
print(num_1+num_2)

# now covert in integer
num_1='100'
num_2='200'

num_1=int(num_1)
num_2=int(num_2)
print(num_1+num_2)