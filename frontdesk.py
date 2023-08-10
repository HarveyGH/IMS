from basic import Basic
from product import Product
from prettytable import PrettyTable
from cashier import Cashier
import os
class ShopCar:
    """"Storage product object and purchase quantity"""
    def __init__(self):
        self.shop_list=[]
    def addCommodity(self,com,com_cnt):#传入商品信息和购买数量

        """Guaranteed stock must be in stock
         If the product is repeated, add the quantity directly, otherwise add it to the list"""
        com_no=com.getNo()
        for i in range(len(self.shop_list)):
            now_com=self.shop_list[i][0]
            if now_com.getNo()==com_no:
                self.shop_list[i][1]+=com_cnt
                return
        #The item does not exist in the shopping cart
        self.shop_list.append([com,com_cnt])
        return
    def delCommodity(self,com_num,com_cnt):
        '''保证满足
        '''
        for i in range(len(self.shop_list)):
            now_com=self.shop_list[i][0]
            if now_com.getNo()==com_num:
                self.shop_list[i][1]-=com_cnt
                if self.shop_list[i][1]==0:
                    self.shop_list.pop(i)
                return
    def clear(self):
        """Guaranteed to meet the conditions"""
        self.shop_list.clear()

    def getMonery(self):
        """Get the total amount of money"""
        res=0.0
        for com,cnt in self.shop_list:
            res+=com.getPrice()*cnt
        return res
    def getCommodityCnt(self,com_num):
        """Return the quantity corresponding to the product ID"""
        res=0
        for com,cnt in self.shop_list:
            if com.getNo()==com_num:
                res=cnt
                break
        return res
    def printList(self):

        """
        Print the current shopping cart information
         ["Product ID", "Product Name", "Product Type", "Specification", "Unit Price", "Purchase Quantity"]
        """

        table=PrettyTable(["Product ID", "Product Name", "Product Type","Specification","Unit Price","Purchase Quantity"])
        for com, cnt in self.shop_list:
            table.add_row([com.getNo(),com.getName(),com.getType(),com.getSize(),com.getPrice(),cnt])
        print(table)
        print("total price：",self.getMonery(),end="\n\n")
    def getlist(self):
        """Return to purchase information"""
        # res_list=[]
        # for i in self.shop_list:
        #     com=i[0]
        #     cnt=i[2]
        #     res_list.append((com.getNo(),cnt))#返回商品编号和 购买的数量
        # return res_list
        return self.shop_list
    def empty(self):
        if not self.shop_list:
            return True
        return False
class FrontDesk:
    '''前台控制'''
    def __init__(self):
        self.admin=None
        self.car=ShopCar()
    def exitLogin(self):
        print("Account {} has been logged out.".format(self.admin.getNo()))
        self.admin=None

    def meta(self):
        #Front desk : Menu
        if self.login()==False:
            return
        while(True):
            os.system("cls")
            print("------------------------------------------------")
            print("1: Query single product information")
            print("2: View all product information")
            print("3: Purchase function")
            if self.admin!=None:
                print("4: logout")
            print("                                     Other numbers exit")
            print("------------------------------------------------")
            cmd=input("Please enter options:").strip()
            if cmd=="1":
                self.queryOne()
            elif cmd=="2":
                self.queryAll()
            elif cmd=="3":
                if (self.admin!=None) or self.login():
                    self.shopingMeta()
            elif self.admin!=None and cmd=="4":
                self.exitLogin()
                break
            else:
                break
            os.system("pause")
    def login(self):
        #Front desk:admin login
        in_num=input("Please enter your account number:").strip()
        cash=Basic.queryOneCashier(in_num)
        if not cash:
            print("This account does not exist.")
            return  False
        cashier=Cashier(cash)
        in_pwd=input("Please enter your password:").strip()
        if cashier.getPwd()==in_pwd:
            self.admin=cashier
            print("Successful login.")
            return True
        else:
            print("Password error.")
            return False
    def queryAll(self):
        #Front desk: query all product information
        info=Basic.queryAllCommodity()
        table = comm = Product.getTableaHead()
        for i in info:
            table.add_row(i)
        print(table)
        print("There are {} records in total.".format(len(info)))
    def queryOne(self):
        #Front desk: query all product information
        com_num=input("Please enter the number of the product to be queried:")
        res=Basic.queryOneCommodity(com_num)
        if not res:#res is null
            print("There is no such product")
        else:
            table=comm=Product.getTableaHead()
            table.add_row(res)
            print(table,end="\n\n")
    def shopingMeta(self):
        #front Purchase
        while True:
            os.system("cls")
            print("Current cart:")
            self.car.printList()
            print("-------\n")
            print("1:Add item to cart")
            print("2:Remove item from shopping cart")
            print("3:Empty shopping cart")
            print("4:Settlement")
            print("--------------------other options to exit")
            cmd=input("Please enter options:").strip()
            if cmd=="1":
                self.addCom()
            elif cmd=="2":
                self.delCom()
            elif cmd=="3":
                self.clearShopCar()
            elif cmd=="4":
                self.pay()
            else:
                break
            os.system("pause")
    def addCom(self):
        #Front desk: Add to cart
        com_num=input("Please enter the product ID:").strip()
        com_info=Basic.queryOneCommodity(com_num)
        if not com_info:
            print("The product does not exist.")
            return
        com=Product(com_info)
        com_cnt=int(input("Please enter the product quantity:").strip())
        if com_cnt <=0:
            print("Please enter the product quantity:")
            return
        if com_cnt>com.getQuantiy() :
            print("Product inventory is insufficient.")
        else :
            self.car.addCommodity(com,com_cnt)
            print("Added to the shopping cart successfully..")

    def clearShopCar(self):
        #Front desk: Empty shopping cart
        cmd=input("Enter 1 to confirm emptying the shopping cart:").strip()
        if cmd=="1":
            self.car.clear()
            print("The shopping cart is empty.")
        else:
            print("The operation has been cancelled.")

    def delCom(self):
        #Front desk: Delete an item in the shopping cart
        com_num = input("Please enter the product ID:").strip()
        have_cnt=self.car.getCommodityCnt(com_num)
        if have_cnt==0:
            print("There is no item in the cart")
        else:
            del_cnt=int(input("There are {} items in the shopping cart, please enter the quantity of the item to be deleted".format(have_cnt)).strip())
            self.car.delCommodity(com_num,min(del_cnt,have_cnt))
            print("Deleted successfully.")
    def getFlowNum(self):
        while True:
            num=Basic.getFlowNum()
            info=Basic.queryOneSellFlowNum(num)
            if info==[]:
                return num
    def pay(self):
         #Front desk: Settlement
         if self.car.empty():
             print("The shopping cart is empty.")
             return
         all_money=self.car.getMonery()
         pay_money=float(input("Please pay ${}:".format(all_money)).strip())
         if pay_money<all_money :
             print("Payment failed.")
         else:
             print("Successful payment, change ${}. ".format(pay_money-all_money))
             shop_list=self.car.getlist()
             for com,com_cnt in shop_list:
                 #delete stock quantity
                 Basic.delCommodityCnt(com.getNo(),com_cnt)
                 #Add purchase information
                 num=self.getFlowNum()
                 Basic.addOneSell(self.admin.getNo(),com.getNo(),num,com_cnt,com.getPrice()*com_cnt)
             print("You have successfully purchased the following items, paid ${} , and gave change ${}  .".format(pay_money,pay_money-all_money))
             self.car.printList()
             self.car.clear()