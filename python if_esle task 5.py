x = ["parata" , "tea " , "samosa"]
y = ["pizza" , "pasta" , "risoto" ]
z = ["fried rice" , "chinese rice " , "egg role"]

# take input from user
dishes = input("Enter a dish name :" )

if dishes in x: 
    print("This is dish from x category ")
elif dishes in y :
     print("This is dish from y category")

else : 
     print("This is dish from z category")    