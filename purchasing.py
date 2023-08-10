from basic import Basic
from product import Product
from prettytable import PrettyTable
from purchaser import Purchaser
import os
import generaloperation
from purchaser import Purchaser
class Purchasing:
    def __init__(self):
        self.admin=None
    def login(self):
        """The login interface of the front desk"""
        pur_num=input("Please enter your ID:").strip()
        pur=Basic.queryOnePurchase(pur_num)
        if not pur:
            print("This ID does not exist.")
            return False
        else:
            self.admin=Purchaser(pur)
            return True
    def meta(self):
        """Operation option interface"""
        if not self.login():
            return
        while True:
            os.system("cls")
            print("------------------------------------------------")
            print("1: Query single product information")
            print("2: View all product information")
            print("3: Add product information")
            print("4: View all purchase information")
            print("5: Purchase")
            print("                                     Other numbers exit")
            print("------------------------------------------------")
            cmd = input("Please enter options:").strip()
            if cmd=="1":
                self.queryOne()
            elif cmd=="2":
                self.queryAll()
            elif cmd=="3":
                self.addOne()
            elif cmd=="4":
                self.querAllStock()
            elif cmd=="5":
                self.purchase()
            else:
                self.admin=None
                break
            os.system("pause")
    def querAllStock(self):
        generaloperation.queryAllStock()
    def addOne(self):
        """Add a new product at the front desk, the stock quantity is 0"""
        com_num=input("Please enter the product ID to be added:").strip()
        com=Basic.queryOneCommodity(com_num)
        if com!=[]:
            print("This product already exists and cannot be added repeatedly.")
            return
        com_name=input("Please enter the product name:").strip()
        com_type=input("Please enter the product type:").strip()
        com_size=input("Please enter the size:").strip()
        com_price=float(input("Please enter the unit price:").strip())
        com_mdate=input("Please enter the production date (format: month-day-year):").strip()
        com_edate=input("Please enter the expiration date (format: month-day-year):").strip()
        com_quantity=0
        try:
            Basic.addOneCommodity(com_num,com_name,com_type,com_size,com_price,com_mdate,com_edate,com_quantity)
            print("Added successfully")
        except Exception as e:
            print("Failed to add, reason:",e)
    def purchase(self):
        # Front desk: purchase
        com_num=input("Please enter the product ID to be purchased:").strip()
        com=Basic.queryOneCommodity(com_num)
        if com==[]:
            print("The product does not exist, please add the product first.")
            return
        com_cnt=int(input("Please enter the quantity of purchase:").strip())
        com_price = float(input("Please enter the unit price of the purchase:").strip())
        in_date = input("Please enter the purchase date (format: month-day-year)::").strip()
        try:
            num=self.getFlowNum()
            Basic.addOneStock(self.admin.getNo(), com_num, num, com_price, com_cnt, in_date)
            Basic.addOneCommodityCnt(com_num,com_cnt)
            print("Operation succeeded.")
        except Exception as e:
            print("Operation failed, reason:",e)

    def queryAll(self):
        #View all product information at the front desk
        generaloperation.queryAllCommodity()
    def queryOne(self):
        #View a product information at the front desk
        generaloperation.queryOneCommodity()
    def exitlogin(self):
        #Exit from the front desk, make sure you have logged in'
        self.admin=None
    def getFlowNum(self):
        while True:
            num=Basic.getFlowNum()
            info=Basic.queryOneStockFlowNum(num)
            if info==[]:
                return num