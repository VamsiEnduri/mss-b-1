# # function 2 types

# # 1.in-built r pre-defined
# # print(),input(),sum,min,max,int,str
# # 2.user-defined 
# # dev writes his own functions based on reqs

# # # def :-- 
# # function is a block of code which is used multiple times whene ever call it 

# # # syntax :-- 
# # def f_name(): # create
# #     #code
# # f_name()   # call r invoke 
# a=10
# b=20
# def add():
#     a=10
#     b=20
#     c=a+b
#     print(c)

# add()   
# add()   
# add()   
# add()   

# def mul():
#     a=10
#     b=20
#     c=a*b
#     print(c)
# mul()    

# # # r-topics :-- 
# # how does memeory works in python ?
# # why function memeory getting vanished after executing the function ?


# # streamlit
# # fastapi 
# # python 
# # llm 
# # lmm apis 
# # rag 
# # rag piplines 
# # langchain

# # ds 
# # gen ai 
# # agentic ai 
# # FDE


# user-defined functions
# 1.function without args and params and return keyword

def mul(): # params
    a=10
    b=20
    c=a*b
    print(c)
mul() #args



# function with args and params 
def mul(x,y): # params
    a=10
    b=20
    c=a*b
    print(c)
    print(x*y)
mul(100,200) #args



# function with return keyword
def mul(): # params
    a=10
    b=20
    c=a*b
    print(c)
    return c

v=mul() #args #v=200

print(v)

# function with args and params and return keuyword


def mul(s,l): # params
    a=10
    b=20
    c=a*b
    print(c)
    print(s,l)
    return c,s,l

v=mul("vamsi",[1,2,3])
print(v)


#function with more args and single param *args :-- variable length args

def mul(*p): # params
    a=10
    b=20
    c=a*b
    print(c)
    print(p)
mul(10,20,30) #args


# function with key:value args


def details(name,age):
    print(name,age)
details(name="vamsi",age=27)    


# function with multiple key:value args but one single param **kwargs


def details(**p):#dict
    print(name,age)
details(name="vamsi",age=27) 




