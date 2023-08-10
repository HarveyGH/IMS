import generaloperation
from basic import Basic
from product import Product
from purchaser import Purchaser
from admin import Admin
import os
class AdminManage:
    def __init__(self):
        self.admin=None
    def login(self):
        '''login'''
        admin_no = input("Please enter your administrator account:").strip()
        adm = Basic.queryOneAdmin(admin_no)
        if adm==[]:
            print("This account does not exist.")
            return False
        admin = Admin(adm)
        in_pwd = input("Please enter your password:").strip()
        if admin.getPwd() == in_pwd:
            self.admin = admin
            print("login Successful.")
            return True
        else:
            print("Wrong password.")
            return False
    def metaQuery(self):
        while True:
            os.system("cls")
            print("------------------------------------------------")
            print("1: View all product information")
            print("2: View all salesperson information")
            print("3: View all purchaser information")
            print("4: View all sales information")
            print("5: View all purchase information")
            print("6: Check the information of a single salesperson (undeveloped)")
            print("7: Check the information of a single purchaser (undeveloped)")
            print("8: View single product information (undeveloped)")
            print("                                     Other numbers exit")
            print("------------------------------------------------")
            cmd = input("Please enter options:").strip()
            if cmd=="1":
                self.queryAllCommodity()
            elif cmd=="2":
                self.queryAllCashier()
            elif cmd=="3":
                self.queryAllPurchaser()
            elif cmd=="4":
                self.queryAllSell()
            elif cmd=="5":
                self.queryAllStock()
            else:
                break
            os.system("pause")
    def metaAdd(self):
        while True:
            os.system("cls")
            print("------------------------------------------------")
            print("1: add a new salesperson")
            print("2: add a new purchaser")
            print("3: Add new product")
            print("                                     Other numbers exit")
            print("------------------------------------------------")
            cmd = input("Please enter options:").strip()
            if cmd=="1":
                self.addOneCashier()
            elif cmd=="2":
                self.addOnePurchaser()
            elif cmd=="3":
                self.addOneCommodity()
            else:
                break
            os.system("pause")
    def metaDel(self):
        while True:
            os.system("cls")
            print("------------------------------------------------")
            print("1: Remove a salesperson")
            print("2: Remove a purchaser")
            print("3: Remove a product")
            print("                                     Other numbers exit")
            print("------------------------------------------------")
            cmd = input("Please enter options:").strip()
            if cmd=="1":
                self.delOneCashier()
            elif cmd=="2":
                self.delOnePurchaser()
            elif cmd=="3":
                self.delOneCommodity()
            else:
                break
            os.system("pause")
    def metaModity(self):
        while True:
            os.system("cls")
            print("------------------------------------------------")
            print("1: Modify a salesperson")
            print("2: Modify a purchaser")
            print("3: Modify a product")
            print("                                     Other numbers exit")
            print("------------------------------------------------")
            cmd = input("Please enter options:").strip()
            if cmd=="1":
                self.modifyOneCashier()
            elif cmd=="2":
                self.modifyOnePurchaser()
            elif cmd=="3":
                self.modifyOneCommodity()
            else:
                break
            os.system("pause")
    def meta(self):
        '''frontdesk menu'''
        if not self.login():
            return
        while True:
            os.system("cls")
            print("------------------------------------------------")
            print("1: enter the query menu")
            print("2: enter the add menu")
            print("3: enter delete menu")
            print("4: enter the modification menu")
            print("5: sales statistics ")
            print("                                     Other numbers exit")
            print("------------------------------------------------")
            cmd = input("Please enter options:").strip()
            if cmd=="1":
                self.metaQuery()
            elif cmd=="2":
                self.metaAdd()
            elif cmd=="3":
                self.metaDel()
            elif cmd=="4":
                self.metaModity()
            elif cmd=="5":
                generaloperation.statictic()
            else:
                break
            os.system("pause")
    def queryAllCommodity(self):
        generaloperation.queryAllCommodity()
    def queryAllCashier(self):
        '''Check the information of all cashiers at the front desk'''
        generaloperation.queryAllCashier()
    def queryAllPurchaser(self):
        '''Check the information of all purchase at the front desk'''
        generaloperation.queryAllPurchaser()
    def queryAllSell(self):
        '''Check the information of all sell at the front desk'''
        generaloperation.queryAllSell()
    def queryAllStock(self):
        '''front desk'''
        generaloperation.queryAllStock()

    def addOneCashier(self):
        '''front desk'''
        cash_no=input("Please enter the salesperson's number:").strip()
        cash=Basic.queryOneCashier(cash_no)
        if cash!=[]:
            print("This number already exists and cannot be added repeatedly.")
            return
        cash_name=input("Please enter the employee's name:").strip()
        cash_pwd=input("Please enter the employee's password:").strip()
        cash_sex=input("Please enter the employee's gender:").strip()
        cash_age=int(input("Please enter the employee's age:").strip())
        cash_hourse=float(input("Please enter the employee's daily workload:").strip())
        cash_salary=float(input("Please enter the employee's monthly salary:").strip())
        cash_phone=input("Please enter the employee's phone number:").strip()
        cash_entry=input("Please enter the employee's date of birth (eg: 2019-6-4):").strip()
        try:
            Basic.addOneCashier(cash_no,cash_name,cash_pwd,cash_sex,cash_age,cash_hourse,cash_salary,cash_phone,cash_entry)
            print("Add salesperson successfully.")
        except Exception as e:
            print("Failed to add salesperson, reason:",e)

    def addOnePurchaser(self):
        ''''''
        pur_no=input("Please enter purchaser ID:").strip()
        pur=Basic.queryOnePurchase(pur_no)
        if pur!=[]:
            print("This ID already exists and cannot be added repeatedly")
            return
        pur_name=input("Please enter the employee's name:").strip()
        pur_sex=input("Please enter the employee's gender:").strip()
        pur_age=int(input("Please enter the employee's age:").strip())
        pur_salary=float(input("Please enter the employee's monthly salary:").strip())
        pur_phone=input("Please enter the employee's phone number:").strip()
        pur_entry=input("Please enter the employee's date of birth (eg: 5-8-1989):").strip()
        try:
            Basic.addOnePurchaser(pur_no,pur_name,pur_sex,pur_age,pur_salary,pur_phone,pur_entry)
            print("Successfully enter the purchaser.")
        except Exception as e:
            print("Failed to add purchaser, reason:",e)
    def addOneCommodity(self):
        ''''''
        com_num = input("Please enter the product ID to be added:").strip()
        com = Basic.queryOneCommodity(com_num)
        if com != []:
            print("This product already exists and cannot be added repeatedly.")
            return
        com_name = input("Please enter the product name: ").strip()
        com_type = input("Please enter the product ID:").strip()
        com_size = input("Please enter the product type:").strip()
        com_price = float(input("Please enter unit price:").strip())
        com_mdate = input("Please enter the production date (format: month-day-year):").strip()
        com_edate = input("Please enter the expiration date (format: month-day-year):").strip()
        com_quantity = int(input("Please enter the inventory quantity:").strip())
        try:
            Basic.addOneCommodity(com_num, com_name, com_type, com_size, com_price, com_mdate, com_edate, com_quantity)
            print("Successfully enter the product")
        except Exception as e:
            print("Failed to add product, reason:", e)
    def delOneCashier(self):
        ''''''
        cash_no=input("Please enter the salesperson ID to be removed:").strip()
        cash=Basic.queryOneCashier(cash_no)
        if cash==[]:
            print("This employee does not exist.")
            return
        cmd=input("Confirm to remove this employee? (After removal, all sales records related to this employee will be deleted.y/n)").strip()
        if cmd[0]=='y'or cmd[0]=='Y':
            Basic.delOneCashier(cash_no)
            print("Operation succeeded.")
        else:
            print("Operation failed.")

    def delOnePurchaser(self):
        pur_no=input("Please enter the purchaser ID to be removed:").strip()
        pur=Basic.queryOnePurchase(pur_no)
        if pur==[]:
            print("This employee does not exist.")
            return
        cmd=input("Confirm to remove this employee? (After removal, all purchasing records related to this employee will be deleted.y/n").strip()
        if cmd[0]=='y'or cmd[0]=='Y':
            Basic.delOnePurchase(pur_no)
            print("Operation succeeded.")
        else:
            print("Operation failed.")
    def delOneCommodity(self):
        ''''''
        com_no=input("Please enter the product ID to be removed:").strip()
        com=Basic.queryOneCommodity(com_no)
        if com==[]:
            print("This product does not exist.")
            return
        cmd=input("Are you sure you want to remove this item? (After removal, all import and export records related to this product will be deleted.y/n").strip()
        if cmd[0]=='y'or cmd[0]=='Y':
            Basic.delOneCommodity(com_no)
            print("Operation succeeded.")
        else:
            print("Operation failed.")

    def modifyOneCashier(self):
        cash_no = input("Please enter the salesperson ID who needs to be modified:").strip()
        cash = Basic.queryOneCashier(cash_no)
        if cash == []:
            print("The salesperson does not exist.")
            return
        cash_name = input("Please enter the modified name:").strip()
        cash_pwd = input("Please enter the employee's password:").strip()
        cash_sex = input("Please enter the employee's gender:").strip()
        cash_age = int(input("Please enter the employee's age:").strip())
        cash_hourse = float(input("Please enter the employee's daily workload:").strip())
        cash_salary = float(input("Please enter the employee's monthly salary:").strip())
        cash_phone = input("Please enter the employee's phone number:").strip()
        cash_entry = input("Please enter the employee's date of birth (eg: 5-9-1999):").strip()
        try:
            Basic.modifyOneCashier(cash_no, cash_name, cash_pwd, cash_sex, cash_age, cash_hourse, cash_salary,
                                   cash_phone, cash_entry)
            print("Modified successfully.")
        except Exception as e:
            print("Modification failed, reason:", e)

    def modifyOnePurchaser(self):
        pur_no = input("Please enter the purchaser ID who needs to be modified:").strip()
        pur = Basic.queryOnePurchase(pur_no)
        if pur == []:
            print("The salesperson does not exist.")
            return
        pur_name = input("Please enter the modified name:").strip()
        pur_sex = input("Please enter the employee's gender:").strip()
        pur_age = int(input("Please enter the employee's age:").strip())
        pur_salary = float(input("Please enter the employee's monthly salary:").strip())
        pur_phone = input("Please enter the employee's phone number:").strip()
        pur_entry = input("Please enter the employee's date of birth (eg: 9-9-1998):").strip()
        try:
            Basic.modifyOnePurchaser(pur_no, pur_name, pur_sex, pur_age, pur_salary, pur_phone, pur_entry)
            print("Modified successfully.")
        except Exception as e:
            print("Modification failed, reason:", e)

    def modifyOneCommodity(self):
        com_num = input("Please enter the product ID to be modified:").strip()
        com = Basic.queryOneCommodity(com_num)
        if com == []:
            print("This product does not exist.")
            return
        com_name = input("Please enter the modified product name:").strip()
        com_type = input("Please enter the modified product type:").strip()
        com_size = input("Please enter the modified specification:").strip()
        com_price = float(input("Please enter the revised unit price:").strip())
        com_mdate = input("Please enter the modified production date (format: month-day-year):").strip()
        com_edate = input("Please enter the modified expiration date (format: month-day-year):").strip()
        com_quantity = int(input("Please enter the modified inventory quantity:").strip())
        try:
            Basic.modifyOneCommodity(com_num, com_name, com_type, com_size, com_price, com_mdate, com_edate, com_quantity)
            print("Modify product successfully")
        except Exception as e:
            print("Failed to modify product, reason: ", e)