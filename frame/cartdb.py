from frame.db import Db
from frame.error import ErrorCode
from frame.sql import Sql
from frame.value import Cust, Item, Cart


class CartDB(Db):
    def insert(self, custid, itemid, num):
        try:
            conn = super().getConnection();
            cursor = conn.cursor();
            cursor.execute(Sql.cartinsert % (custid, itemid, num));
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

    def select(self, custid):
        all = [];
        conn = super().getConnection();
        cursor = conn.cursor();
        cursor.execute(Sql.cartlist % custid); # 어떤 SQL문을 날릴지?
        result = cursor.fetchall();
        for c in result:
            cart = Cart(c[0], c[1], c[2], c[3], c[4], c[5], c[6]);
            all.append(cart);
        super().close(cursor, conn); # 꼭 close해줘야~
        return all;


if __name__ == '__main__':
    CartDB().insert('id10', 1001, 3);