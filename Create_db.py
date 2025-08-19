import sqlite3


def create_db():
    con = sqlite3.connect(database=r"ims.db")
    cur = con.cursor()

    # cur.execute("drop table category")
    # con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS admin(e_id INTEGER PRIMARY KEY AUTOINCREMENT, name text, email text, gender text, contact text, dob text, doj text, pass text, u_type text, address text, salary text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS employee(e_id INTEGER PRIMARY KEY AUTOINCREMENT, name text, email text, gender text, contact text, dob text, doj text, pass text, u_type text, address text, salary text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS supplier(invoice INTEGER PRIMARY KEY AUTOINCREMENT, name text, contact text, desc text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS category(c_id INTEGER PRIMARY KEY AUTOINCREMENT, name text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS product(p_id INTEGER PRIMARY KEY AUTOINCREMENT, Category text, Supplier text, name text, price text, quantity text, status text)")
    con.commit()

    # ================= To Reinitialize index no. rerun these below lines ===================

    # cur.execute("insert into category (c_id, name) values(?, ?)", ("5", "Mobile"))
    # cur.execute("update category set name=? where c_id=?", ("Data Cables", "5"))
    # cur.execute("insert into product (p_id, Category) values(?, ?)", ("5", "Mobile"))
    con.commit()

    con.close()


create_db()
