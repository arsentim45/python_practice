import sqlite3
def main():
    conn = sqlite3.connect("main_database.db")
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE constants (variable, value)""")
    conn.commit()
    cursor.execute("""INSERT INTO constants 
            VALUES ('size','(2048,2048)')""")
    conn.commit()
    cursor.execute("""INSERT INTO constants 
            VALUES ('subscription_key' ,'d7c63760ead5413f87a1563405ca190a')""")
    conn.commit()
    cursor.execute("""INSERT INTO constants 
            VALUES ('search_url','https://api.cognitive.microsoft.com/bing/v7.0/images/search?')""")
    conn.commit()
    cursor.execute("""INSERT INTO constants 
            VALUES ('name','cats')""")
    conn.commit()
    cursor.execute("""INSERT INTO constants 
            VALUES ('count','20')""")
    conn.commit()

if __name__ == '__main__':
    main()