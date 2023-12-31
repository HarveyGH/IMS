from prettytable import PrettyTable
class Product:
    def __init__(self,info_list=None):
        self.info=info_list
    def getNo(self):
        return self.info[0]
    def getName(self):
        return self.info[1]
    def getType(self):
        return self.info[2]
    def getSize(self):
        return self.info[3]
    def getPrice(self):
        return self.info[4]
    def getDate(self):
        return self.info[5]
    def getmDate(self):
        return self.info[6]
    def getQuantiy(self):
        return self.info[7]
    @classmethod
    def getTableaHead(cls):
        return  PrettyTable(["product ID", "product name", "product type","specification","unit price","production date","expiration date","stock quantity"])