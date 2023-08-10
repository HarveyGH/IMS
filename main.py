import pymssql

from purchasing import Purchasing

"""import generaloperation"""
from basic import Basic
from frontdesk import FrontDesk
from product import Product
from adminmanage import AdminManage
import os
def link():
    conn = pymssql.connect(host="127.0.0.1",
                           server="CHEN_PC\SQLEXPRESS",
                           port="1433",
                           user="sa",
                           password="1q2w3e",
                           database="IMS",
                           charset="utf8")
    return conn
def meta():
    while True:
        os.system("cls")
        print("------------------------------------------------")
        print("1: Salesperson")
        print("2: Purchaser")
        print("3: Administrator")
        print("                                     Other numbers exit")
        print("------------------------------------------------")
        cmd = input("Please enter options:").strip()
        if cmd=="1":
            front_desk=FrontDesk()
            front_desk.meta()
        elif cmd=="2":
            purchase_manage = Purchasing()
            purchase_manage.meta()
        elif cmd=="3":
            admin_manage = AdminManage()
            admin_manage.meta()
        else:
            break
        os.system("pause")

if __name__ == '__main__':
    try:
        conn=link()
        Basic.setConn(conn)
        meta()
    except Exception as e:
        print("An error occurred, the reason：",e)