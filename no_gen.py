import random
import mysql.connector

# for i in range(10):
#     a=random.randint(10,99)
#     b=random.randint(100,999)
#     c=random.randint(1000,9999)
#     print(str(a)+'-'+str(b)+'-'+str(c))

mydb = mysql.connector.connect(host="Shikhars-MacBook-Pro.local",user="shikhar",password="1234ball",database="db")
cursor=mydb.cursor()
cursor.execute('select idContinentals from Continentals')
result=cursor.fetchall()
print(result)
index=random.randint(0,19)
print(result[index][0])
