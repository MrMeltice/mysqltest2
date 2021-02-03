import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user="root",
    passwd="",
    database="game"
)

mycursor = mydb.cursor()
def createTable():
    mycursor.execute("CREATE TABLE IF NOT EXISTS customers(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

createTable()

def menu():
    ans = input("Enter name or 'remove'/'update': ")
    if ans == "Done":
        print("close")
    elif ans == "update":
        update()
        ans = input("Enter 0 to go back")
        
        if ans == "0":
            menu()
    elif ans == "remove":
        remove()
        ans = input("Enter 0 to go back")
        if ans == "0":
            menu()
    else:
        name = ans
        address = input("Enter address: ")
        exist(name, address)
        menu()

def insertonerow(x, y):
    query = "INSERT INTO IF NOT EXISTS customers (name, address) VALUES (%s,%s)"
    val = (x, y)
    mycursor.execute(query, val)
    
    mydb.commit()
    
    print(mycursor.rowcount, "records inserted.")


def exist(name, address):
    query = "SELECT count(*) FROM customers where name ='{}'".format(name)
    
    mycursor.execute(query)
    
    myresult = mycursor.fetchall()
    
    count = myresult[0][0]
    print(count)
    
    if count == 0:
        query = "INSERT INTO customers (name, address) VALUES (%s, %s)"
        val = (name, address)
        mycursor.execute(query, val)
        mydb.commit()
        print(mycursor.rowcount, "records inserted")
    else:
        print("Already Exists")
        
def update():
    ID = input("Enter ID: ")
    name = input("Enter new name: ")
    address = input("Enter new address: ")
    query = "UPDATE customers SET name = '{}', address = '{}' where id = '{}'".format(name, address, ID)
    mycursor.execute(query)
    mydb.commit()
    print("Updated")
    
def remove():
    name = input("Enter name of the element you are removing: ")
    query = "DELETE FROM customers where name = '{}'".format(name)
    mycursor.execute(query)
    mydb.commit()
    print("Deleted")
        
menu()
