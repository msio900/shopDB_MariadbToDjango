class Sql:
    custlist = "SELECT * FROM cust";
    custlistone = "SELECT * FROM cust WHERE id= '%s' ";
    custinsert = "INSERT INTO cust VALUES ('%s','%s','%s')";
    custdelete = "DELETE FROM cust WHERE id= '%s' ";
    custupdate = "UPDATE cust SET pwd='%s',name='%s' WHERE id= '%s' ";

    itemlist = "SELECT * FROM item";
    itemlistone = "SELECT * FROM item WHERE id= %d ";
    iteminsert = "INSERT INTO item VALUES (NULL, '%s',%d,'%s', CURRENT_DATE())";
    itemdelete = "DELETE FROM item WHERE id= %d ";
    itemupdate = "UPDATE item SET name='%s',price=%d, imgname='%s' WHERE id= %d ";

    cartlist = """
                SELECT a.regdate, a.custid, a.itemid, i.price, a.num,
                    (i.price * a.num) as total, i.imgname
                    FROM cart a INNER JOIN cust c ON a.custid = c.id
                    INNER JOIN item i ON a.itemid = i.id
                    WHERE c.id = '%s'
                """;
    cartinsert = "INSERT INTO cart VALUES (NULL, '%s', '%d', '%d', CURRENT_DATE())";