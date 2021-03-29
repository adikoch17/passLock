import mysql.connector
import getpass
import pyperclip


mydb = mysql.connector.connect(
  host="localhost",
  user="aditya",
  password="123456",
  database="test"
)

cursor = mydb.cursor()

def lock():

  choice = int(input("what do you want to do ?\n1.Get password\n2.add password\n3.update password\n4.delete password\n5.show all applications\n6.quit\n\n"))

  if choice == 1 :
    app = input("which application?\n")
    cursor.execute('select * from passwords where(app="' + app +'")')
    for x in cursor:
      pyperclip.copy(x[1])
    print("password copied to clipboard\n")
    lock()

  if choice == 2 :
    app = input("what application?\n")
    passw = getpass.getpass(prompt='Enter password:  ')
    cursor.execute('insert into passwords values("'+ app +'","'+ str(passw) +'");')
    mydb.commit()
    print("password added\n")
    lock()

  if choice == 3:
    app = input("what application?\n")
    passw = getpass.getpass(prompt = "Enter new password: ")
    cursor.execute('update passwords set pass ="'+ passw +'" where app = "'+ app +'"' )
    mydb.commit()
    print("password updated\n")
    lock()

  if choice == 4:
    app = input("what application?\n")
    cursor.execute('delete from passwords where app = "'+ app +'"' )
    mydb.commit()
    print("password deleted\n")
    lock()

  if choice == 5 :
    cursor.execute('select * from passwords')
    print("\n+----------------------------+")
    for x in cursor:
      print(x[0])
    print("+----------------------------+\n")
    lock()

  if choice == 6:
    quit()


if getpass.getpass(prompt="pass: ") == "123456" :
  lock()




