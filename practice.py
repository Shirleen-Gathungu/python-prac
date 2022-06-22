# a,b,c="Letter","Card","Present"
# print(a)
# print(b)
# print(c)

# n="Don't"
# o="Tell"
# p="Her"
# print(n,o,p)

# message="Jello is sweet"
# print(message[:8])

# a="a hotel A rome"
# if "a" in a:
#     print(a.replace("a","A","A","a"))
    
# def user_message(age,name,year_born,year):
#     name="Dodge"
#     age=30
#     year=2022
#     year_born=year-age
# print(f"Hello {'name'} you were born in {'year_born'} and you are{'age'}")

# message="Janitor sumari is janta"
# print(message.re.sub("J","j","I","i"))

# clothes_list=["Shirt","Sweatpants","Jacket","Skirt","Blouse","Dress"]
# clothes=[]
# c=0
# for clothe in clothes_list:
#     if "S" in clothes_list:
#         print(clothes.append())
       

# colours=("blue","green","orange","red","yellow","purple")
# a=list(colours)
# a[1]="Violet"
# colours=tuple(a)
# print(colours)

# pastry={"Cakes","Cookies","Pies"}
# pastry_two={"Macaroon","Pattie cakes","Chocolate crunch"}
# print(pastry.union(pastry_two))


# people={"student_one":"Angela","student_two":"Mariam","student_three":"Polly","student_four":"Nelly"}
# people["student_one"]="Johanne"
# people["student_five"]="Dylan"
# print(people.pop("student_two"))
# print(people)

# a=1
# while a<6:
#     print(a)
#     if a==7:
#         break
# a+=1


# def smallest(*numbers:List):
#     print(min(numbers))
    
# def chewies(food):
#     for x in food:
#         print(x)

# Write a function named capital_indexes.
# The function takes a single parameter, which is a string. 
# Your function should return a list of all the indexes in 
# the string that have capital letters.







# def capital_letters(name):
#     ans=0
    
#     for ind in name:
#         if ind.isupper():
#             indexes=findIndex(ind)
#             list_index=[]
#             list_index.append(indexes)
#             print(list_index)
   
#         # print(ind)
# capital_letters("NaImA")


# def  user_weight():
#     user_input=int(input("Enter weight:"))
#     user_input_two=input("Is your weight in Kg or Pounds:")
   
#     convert_to_kg=user_input*2.205
#     convert_pounds=user_input/2.205

#     if user_input_two=="Kg":
#          print("Your weight is correct")
    
#     elif user_input_two=="Pounds":
#         #print(convert_pounds)
#         print(f"Your weight is {convert_pounds}")
    
#     else:
#         print(f"Your weigh)
# user_weight()




# def count_strings(name):
#     dict_char={}
#     for char in name:
#         keys=dict_char.keys()
#         if char in keys:
#             dict_char[char]+=1
#         else:
#             dict_char[char]=1
#     print(dict_char)

# count_strings("JinaLina")

# def check_speed(speed):
#     demerit=0
#     limit=70
#     if speed<limit:
#         print("Ok")
    
#     elif speed>limit:
#         max_speed=speed-70
#         points=(max_speed*1)/5
#         demerit+=points
#         print(demerit)
    
#     if demerit>12:
#         print("License suspended")

# check_speed(360)

# def names(*kwargs):
#     dict=kwargs.keys() 

#     if 'name' in dict:
#         return True


# def palindrome(word):

#     if word[0]==word[-1]:
#         print("It is a palindrome")
#     else:
#         print("Not a palindrome")
    
# palindrome('nun')


# import code


# def pal(word):
#     if word[::-1]==word:
#         print("It is a palindrome")
#     else:
#         print("Not a palindrome")
# pal("lol")

# codes={67:"Jim",30:"Ian",77:"Nity",20:"Pop"}
# user_input=input("Enter a number:")
# key=codes.keys()

#     if user_input in key:
#         print(True)
#     else:
#         print(False)





          
  

    
    



