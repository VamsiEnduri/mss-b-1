# class FoodOrder:
#     platFormName="zomato"
    
#     def __init__(self,cn,fi,q,p):
#         self.CustomerName=cn
#         self.FoodItem=fi
#         self.Quantity=q # 2
#         self.Price=p # 350
    
#     def display_order_details(self):
#         totalBillAmt=  self.Quantity * self.Price
#         print(totalBillAmt)
#         print(self.CustomerName,self.FoodItem,self.Quantity,self.Price)
            

# obj1=FoodOrder("vamsi","mutton biryani",2,350)     
# obj1.display_order_details()


# multiple objects and accessing properties of class at outside of class

abc=10 # gloabl var
class A:

    name__ ="A class" # class var
    print(name__)

    def __init__(self,v1,v2,v3):
        t=10 # local var
        self.name="vamsi" # instance var
        self.loc="hyd"
        self.value1=v1 
        self.value2=v2
        self.value3=v3
        print(self.name.self.loc)

    def xyz(self):
        xyzv1=10 # local var
        print(xyzv1)

    def abc(self):
        abcv1=10 #local var
        print(abcv1)

obj=A("v",22,12)  
print(obj.name__)    # class var outside class access
obj.xyz() # class user-defined method outside class access
obj.abc()    # class user-defined method outside class access

obj2=A("B",200,100)
print(obj2.name__)
obj2.xyz()
obj2.abc()


