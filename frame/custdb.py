from frame.db import Db
from frame.error import ErrorCode
from frame.sql import Sql
from frame.value import Cust


class CustDB(Db):
    def update(self, pwd, name, id):
        try:
            conn = super().getConnection();
            cursor = conn.cursor();
            cursor.execute(Sql.custupdate % (pwd, name, id));
            conn.commit();
        except:
            conn.rollback();
            raise Exception;
        finally:
            super().close(cursor, conn);


    def delete(self, id):
        try:
            conn = super().getConnection();
            cursor = conn.cursor();
            cursor.execute(Sql.custdelete % id);
            conn.commit();
        except:
            conn.rollback();
            raise Exception;
        finally:
            super().close(cursor, conn);

    def insert(self,id,pwd,name):
        try:
            conn = super().getConnection();
            cursor = conn.cursor();
            cursor.execute(Sql.custinsert % (id,pwd,name));
            conn.commit();
        except:
            conn.rollback();
            raise Exception;
        finally:
            super().close(cursor,conn);

    def selectone(self, id):
        cust = None;
        conn = super().getConnection();
        cursor = conn.cursor();
        cursor.execute(Sql.custlistone % id);
        c = cursor.fetchone();
        cust = Cust(c[0], c[1], c[2]);
        super().close(cursor, conn); # 꼭 close해줘야~
        return cust;



    def select(self):
        all = [];
        conn = super().getConnection();
        cursor = conn.cursor();
        cursor.execute(Sql.custlist); # 어떤 SQL문을 날릴지?
        result = cursor.fetchall();
        for c in result:
            cust = Cust(c[0], c[1], c[2]);
            all.append(cust);
        super().close(cursor, conn); # 꼭 close해줘야~
        return all;


if __name__ == '__main__':
    # result = CustDB().select();
    # for r in result:
    #     print(r);

    # cust = CustDB().selectone('id01');
    # print(cust);
    try:
        CustDB().insert('id04', 'pwd04', '이말자');
        print('OK');
    except:
        print(ErrorCode.e0001)

    # try:
    #     CustDB().update('pwd04다시', '이길자', 'id05');
    #     print('OK');
    # except:
    #     print(ErrorCode.e0002)
    # try:
    #     CustDB().delete('id04');
    #     print('OK');
    # except:
    #     print(ErrorCode.e0002)