found = False
name = "Christina"
last_name = "Nkya"
age = 100
print(name, last_name, age)

#if /else statements

if age<100:
    print("great your not that old")

elif age >100:
    print("you are really old")
else:
    print("I don't know how you get here")    
print("I am outside of the if statement")

#functions

def sayHello():
    print("Hello")

sayHello()

#list......this is arrays
colors = ["black", "blue", "red", "yellow"]
#add a new color
colors.append("purple")

print(colors)
#get an element
print(colors[4])

#travel the list - for loop

for x in colors:
    print(x)

#dictionary
me = {
    "first-name": "Christina",
    "last-name": "Nkya",
    "age": 100,
    
}
print(me)
#modify
me["age"] = 44
#get the value
print(me["first-name"])
print(me)