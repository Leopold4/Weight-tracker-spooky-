import sqlite3 as s


def clear_data():
    con = s.connect("Weight_data.db")
    cur = con.cursor()
    cur.execute("DELETE FROM weight_table")
    con.commit()


def insert(weight):
    con = s.connect("Weight_data.db")
    cur = con.cursor()
    cur.execute(
        f"INSERT INTO weight_table(weight, date) VALUES ({weight}, CURRENT_DATE)")
    con.commit()
    con.close()


def current_weight_avg():
    con = s.connect("Weight_data.db")
    cur = con.cursor()
    weight_values = list(cur.execute("""SELECT weight FROM weight_table 
                WHERE date > DATE(CURRENT_DATE, '-7 day')"""))
    avg = 0
    divider = len(weight_values)
    for x in weight_values:
        avg += x[0]
    try:
        return round(avg/divider, 2)
    except ZeroDivisionError:
        return 0


def last_week_avg():
    con = s.connect("Weight_data.db")
    cur = con.cursor()
    weight_values = list(cur.execute("""SELECT weight FROM weight_table 
                WHERE date <= DATE(CURRENT_DATE, '-7 day') 
                AND date >= DATE(CURRENT_DATE, '-14 day')"""))
    con.commit()
    avg = 0
    divider = len(weight_values)
    for x in weight_values:
        avg += x[0]
    try:
        return round(avg/divider, 2)
    except ZeroDivisionError:
        return 0


def week_before_avg():
    con = s.connect("Weight_data.db")
    cur = con.cursor()
    weight_values = list(cur.execute("""SELECT weight FROM weight_table 
                WHERE date <= DATE(CURRENT_DATE, '-14 day') 
                AND date >= DATE(CURRENT_DATE, '-21 day')"""))
    avg = 0
    divider = len(weight_values)
    for x in weight_values:
        avg += x[0]
    try:
        return round(avg/divider, 2)
    except ZeroDivisionError:
        return 0


def insert_funny(weight):
    con = s.connect("Weight_data.db")
    cur = con.cursor()
    cur.execute(
        f"INSERT INTO weight_table(weight, date) VALUES ({weight}, DATE(CURRENT_DATE, '-10 day'))")
    con.commit()
    con.close()
