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


    def delete(self, id):
        try:
            conn = super().getConnection();
            cursor = conn.cursor();
            cursor.execute(Sql.itemdelete % id);
            conn.commit();
        except:
            conn.rollback();
            raise Exception;
        finally:
            super().close(cursor, conn);


    def insert(self, name, price, imgname):
        try:
            conn = super().getConnection();
            cursor = conn.cursor();
            cursor.execute(Sql.iteminsert % (name, price, imgname));
            conn.commit();
        except:
            conn.rollback();
            raise Exception;
        finally:
            super().close(cursor, conn);


    def selectone(self, id):
        item = None;
        conn = super().getConnection();
        cursor = conn.cursor();
        cursor.execute(Sql.itemlistone % id);
        i = cursor.fetchone();
        item = Item(i[0], i[1], i[2], i[3], i[4]);
        super().close(cursor, conn); # 꼭 close해줘야~
        return item;

    def select(self):
        all = [];
        conn = super().getConnection();
        cursor = conn.cursor();
        cursor.execute(Sql.itemlist); # 어떤 SQL문을 날릴지?
        result = cursor.fetchall();
        for i in result:
            item = Item(i[0], i[1], i[2], i[3], i[4]);
            all.append(item);
        super().close(cursor, conn); # 꼭 close해줘야~
        return all;


if __name__ == '__main__':
    # result = ItemDB().select();
    # for r in result:
    #     print(r);

    # item = ItemDB().selectone(1001);
    # print(item);
    try:
        ItemDB().insert('1005', 'pwd04', '이말자');
        print('OK');
    except:
        print(ErrorCode.e0001)

    # try:
    #     ItemDB().update('pwd04다시', '이길자', 'id05');
    #     print('OK');
    # except:
    #     print(ErrorCode.e0002)
    # try:
    #     ItemDB().delete('id04');
    #     print('OK');
    # except:
    #     print(ErrorCode.e0002)