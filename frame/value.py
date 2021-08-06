class Cart:
    def __init__(self, regdate, custid, itemid, price, num, total, imgname):
        self.regdate = regdate;
        self.custid = custid;
        self.itemid = itemid;
        self.price = price;
        self.num = num;
        self.total = total;
        self.imgname = imgname;
    def __str__(self):
        return self.regdate+' '+self.custid+' '+self.itemid+' '\
            +self.price+' '+self.num+' '+self.total+' '+self.imgname;

class Cust:
    def __init__(self, id, pwd, name):
        self.id = id;
        self.pwd = pwd;
        self.name = name;
    def __str__(self):
        return self.id+' '+self.pwd+' '+self.name+' ';

class Item:
    def __init__(self, id, name, price, imgname, regdate):
        self.id = id;
        self.name = name;
        self.price = price;
        self.imgname = imgname;
        self.regdate = regdate;


    def __str__(self):
        return str(self.id) + ' ' + self.name + ' ' \
               + str(self.price) + ' '+ str(self.regdate) + ' '+self.imgname;