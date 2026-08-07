# # # learn daily at least 10 mins 

# # # inheritance :-- 
# # # multiple inheritance :-- 
# # # more than one parent

# # class Father:
# #     name="srinu"

# #     def __init__(self) :
# #         print("father init method")

# #     def properties(self):
# #         land=1
# #         gold=1
# #         print(gold,land)    

# # class Mother:
# #     name="anjali"

# #     def __init__(self) :
# #         print("mother init method")

# #     def Iq(self):
# #         i=150
# #         print(i)

# # class Child(Father,Mother):
# #     # name="Vamsi"
# #     def __init__(self):
# #         # n=super().name # n = srinu / anjali
# #         # print(n)
# #         n1=Father.name 
# #         n2=Mother.name
# #         print(n1,n2)
# #         Father.properties(self)
# #         Mother.Iq(self)

# # obj=Child()
# # print(obj.name) # srinu
# # # ambiguity




# # hierarchial inheritance 
# # one parent but multiple child classes 

# class parent:
#     sur_name="Enduri"

#     def __init__(self):
#         print("parent class init method")

#     def p(self):
#         land=1
#         print(land)     

# class Child1(parent):
#     name="vamsi"
#     def __init__(self):
#         print(super().sur_name)
#         parent.p(self)

# obj1=Child1()

# class Child2(parent):
#     def __init__(self):
#         print(super().sur_name)

# obj2=Child2()

# print(obj1.name)

# # 





# encapsulation
# the process of securing the sensitive data is encapsulation
# en - capsule - ation
# secure - closed - process 

# secure :-- data 
# public 
# private -- secure 

# public data 


class parent:
    sur_name="Enduri"

    def __init__(self):
        self.__pin=1234
        self._bal=45000
        print("parent class init method")
        print(self.__pin)
        print(self._bal)

    def p(self):
        land=1
        print(land)   
obj=parent()
print(obj.sur_name)
print(obj._bal)
print(obj._parent__pin) # name mangling







# protetced data 
# private data