from basic import Basic
from product import Product
from prettytable import PrettyTable
from purchaser import Purchaser
from cashier import Cashier
from datetime import datetime,timedelta
from sell import Sell
def queryAllCommodity():
    '''Front desk: query all product information'''
    info = Basic.queryAllCommodity()
    table = comm = Product.getTableaHead()
    for i in info:
        table.add_row(i)
    print(table)
    print("A total of {} records above.".format(len(info)))


def queryOneCommodity():
    '''Query a commodity information'''
    com_num = input("Please enter the code of the product to be queried:")
    res = Basic.queryOneCommodity(com_num)
    if not res:  # res为空
        print("There is no such product")
    else:
        table = comm = Product.getTableaHead()
        table.add_row(res)
        print(table, end="\n\n")
def queryOneCahier():
    cash_no=input("Please enter the salesperson ID to be queried:").strip()
    cash=Basic.queryOneCashier(cash_no)
    if cash==[]:
        print("The salesperson does not exist.")
        return
    table=Product.getTableaHead()
    table.add_row(cash)
    print(table)
def queryOnePurchaser():
    pur_no=input("Please enter the purchaser ID to be queried:").strip()
    pur=Basic.queryOnePurchase(pur_no)
    if pur==[]:
        print("The purchaser does not exist.")
        return
    table=Purchaser.getTableaHead()
    table.add_row(pur)
    print(table)

def queryAllStock():
    '''Front desk: view all purchase information'''
    info=Basic.queryAllStock()
    table=PrettyTable(["Purchaser ID","product ID","Purchase serial number","Purchase unit price","Increase quantity","Purchase date"])
    for i in info:
        table.add_row(i)
    print(table)
    print("A total of {} records above.".format(len(info)))
def queryAllCashier():
    """Check the information of all cashiers at the front desk"""
    info=Basic.queryAllCashier()
    # print(info)
    table=Cashier.getTableaHead()
    # print(table)
    for i in info:
        table.add_row(i)
    print(table)
    print("A total of {} records above.".format(len(info)))

def queryAllPurchaser():
    """Front desk: query all purchase"""
    info=Basic.queryAllPurchaser()
    table=Purchaser.getTableaHead()
    for i in info:
        table.add_row(i)
    print(table)
    print("A total of {} records above.".format(len(info)))
def queryAllSell():
    info=Basic.queryAllSell()
    table=PrettyTable(["cashier ID","product ID","Sales serial number","Sale quantity","Total price","Date"])
    for i in info:
        table.add_row(i)
    print(table)
    print("A total of {} records above.".format(len(info)))
def statictic():
    # try:
    left=input("Please enter the start date:(for example:8-8-2020)").strip()
    left=datetime.strptime(left,"%m-%d-%Y").date()
    right=input("Please enter the end date:(for example:8-8-2021)").strip()
    right = datetime.strptime(right, "%m-%d-%Y").date()
    cnt_list=getBothTopStatic(left,right,10)
    table=PrettyTable(["Sales Ranking","Product ID","Product name","Type","Unit Price","Sales within a specified date"])
    top=min(10,len(cnt_list))
    for i in range(0,top):
        ob=cnt_list[i].ob
        cnt=cnt_list[i].cnt
        table.add_row([i+1,ob.getNo(),ob.getName(),ob.getType(),ob.getPrice(),cnt])
    print(table)
    # except Exception as e:
    #     print("error, reason:",e)
class pair:
    def __init__(self,ob=None,cnt=0):
        self.ob=ob
        self.cnt=cnt
def getBothTopStatic(left, right, com_no):
    """return list, each element is a commodity object and cnt"""
    all_sell=Basic.queryAllSell()
    cnt_dict={}
    for DA in all_sell:
        sell=Sell(DA)
        com_no=sell.getComNo()
        if com_no==None:
            continue
        now_date=sell.getTime().date()
        if now_date>=left and now_date <=right:
            cnt_dict.setdefault(com_no, 0)
            cnt_dict[com_no]+=1
    cnt_list=[]
    for com_num in cnt_dict:#key  编号,value is cnt
        ob=Basic.queryOneCommodity(com_num)
        cnt_list.append(pair(Product(ob),cnt_dict[com_num]))
    cnt_list.sort(key=lambda x:(x.cnt),reverse=True)
    return cnt_list