from frame.db import Db
from frame.error import ErrorCode
from frame.sql import Sql
from frame.value import Cust, Item


class ItemDB(Db):

    def update(self,id,name,price,imgname):
        try:
            conn = super().getConnection();
            cursor = conn.cursor();
            cursor.execute(Sql.itemupdate % (name,price,imgname,id));
            conn.commit();
        except:
            conn.rollback();
            raise Exception;
        finally:
            super().close(cursor,conn);
    def delete(self,id):
        try:
            conn = super().getConnection();
            cursor = conn.cursor();
            cursor.execute(Sql.itemdelete % (id));
            conn.commit();
        except:
            conn.rollback();
            raise Exception;
        finally:
            super().close(cursor,conn);
    def insert(self,name,price,imgname):
        try:
            conn = super().getConnection();
            cursor = conn.cursor();
            cursor.execute(Sql.iteminsert % (name,price,imgname));
            conn.commit();
        except:
            conn.rollback();
            raise Exception;
        finally:
            super().close(cursor,conn);


    def selectone(self,id):
        item = None;
        conn = super().getConnection();
        cursor = conn.cursor();
        cursor.execute(Sql.itemlistone % id);
        c = cursor.fetchone();
        item = Item(c[0],c[1],c[2],c[3],c[4]);
        super().close(cursor,conn);
        return item;

    def select(self):
        all = [];
        conn = super().getConnection();
        cursor = conn.cursor();
        cursor.execute(Sql.itemlist);
        result = cursor.fetchall();
        for c in result:
            item = Item(c[0],c[1],c[2],c[3],c[4]);
            all.append(item);
        super().close(cursor,conn);
        return all;

if __name__ == '__main__':
    result = ItemDB().select();
    for r in result:
        print(r);

    # cust = ItemDB().selectone(1000);
    # print(cust);

    # try:
    #     ItemDB().delete(1002);
    #     print('OK');
    # except:
    #     print(ErrorCode.e0001);

    # try:
    #     ItemDB().update(1003,'shirts3',5555,'shirts3.jpg');
    #     print('OK');
    # except:
    #     print(ErrorCode.e0001);
