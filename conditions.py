# # # conditional statements
# # # statements = lines 
# # # conditional = based on certain condition 

# # # what are conditional statements ?
# # # conditional statements are nothing but certain statements will execute only when a specific condition gets satisfied

# # # what are the types  of conditional statements in python ?
# # # we have 4 types of conditional sta
# # # # 1.if
# # # # 2.if-else
# # # # 3.if-elif-elif-else :-- elif ladder 
# # # # 4.nested if 
# # # # 5.ternary opeartor



# # # # if :- 
# # # #if syntax :- 
# # # if condition :
# # #     #code to execute if codition gets true / satisfy


# # # exampples :-  

# # if False :
# #     print(100)


# # if True :
# #     print("hello")



# # # synatx if-else 

# # if condition :
# #     #code 
# # else :
# #     #code     

# # # indentation 
# # if True : # if True
# #     print("vamsi")
# #     print("vasavi")
# #     print("srilkeha")
# #     print("srinu")
# # else:
# #     print("hyd kphb road no 4 near remedy MSS")    



# # if False :
# #     print("vamsi")
# #     print("vasavi")
# #     print("srilkeha")
# #     print("srinu")
# # else:
# #     print("hyd kphb road no 4 near remedy MSS")       


    
# # if 0 :
# #     print("vamsi")
# #     print("vasavi")
# #     print("srilkeha")
# #     print("srinu")
# # else:
# #     print("hyd kphb road no 4 near remedy MSS")      



# # if 0 == 0: 
# #     print("vamsi")
# #     print("vasavi")
# #     print("srilkeha")
# #     print("srinu")
# # else:
# #     print("hyd kphb road no 4 near remedy MSS")            



# # if False == True : 
# #     print("vamsi")
# #     print("vasavi")
# #     print("srilkeha")
# #     print("srinu")
# # else:
# #     print("hyd kphb road no 4 near remedy MSS") 


# # if False == not True : 
# #     print("vamsi")
# #     print("vasavi")
# #     print("srilkeha")
# #     print("srinu")
# # else:
# #     print("hyd kphb road no 4 near remedy MSS")               




# # # main example :--

# # loggedinUser=False

# # rEmail="vamsi@gmail.com"
# # rPassword="vamsi@123"

# # lEmail=input("enter yr email to login     ")
# # lPassword=input("enter password to login    ")
  


# # if rEmail == lEmail and rPassword == lPassword: # if True
    
# #     loggedinUser=True
# # else:
# #     print("login failed invalid credentials") 


# # if loggedinUser:
# #     print("loggedin successfuly...")
# #     navigate("/admin_dashboard")


# # if False :
# #     print(100)



# # elif-ladder :-- 

# # syntax 

# # if condition:
# #     #CODE
# # elif condition:
# #     #code
# # elif condition:
# #     #code
# # else :
# #     #code

# # ex:--1 

# if True :
#     print("if block")
# elif False:
#     print("elif 1 block")
# elif True:
#     print("elif 2 block")
# else:
#     print("else block")    


# # ex:--2
# marks =77
# if marks >=92 : # 77 >=92
#     print("A+")
# elif marks 81>= and marks <= 91 : # 
#     print("A")
# elif marks >=71 and marks <=80:# 77 >=71 and 77 <=80
#     print("B+")
# elif marks >=35 and marks <=70:
#     print("C")    
# else :
#     pringt("Fail")        



# nested if :

# # example :-- 

# if True :

#     if True:
#         print("child if")

#     else :
#         print("child else")

# else:
#     print("parent else")       

# role :-- 
# recruiter 
# job_seeker

# email and password 

# nested if 



rEmail="vamsi@gmail.com"
rPassword="vamsi@123"


print("try to register as seller , buyer otherwise you will be guest user")
lRole =input("enter role here :-- ") # seller r buyer , lRole=""
# lRole ="seller"
# a=10

if lRole == "seller":
    print("seller role")
    lEmail=input("enter yr login mail here :--  ")
    lPassword=input("enter yr login password here :--  ")

    if rEmail == lEmail and rPassword == lPassword:
        print("login successful as seller")
    else:
        print("invalid cred")    
elif lRole == "buyer":
    print("buyer role")
    lEmail=input("enter yr login mail here :--  ")
    lPassword=input("enter yr login password here :--  ")

    if rEmail == lEmail and rPassword == lPassword:
        print("login successful as buyer")
    else:
        print("invalid cred")   
else :
    print("you are guest user")        
