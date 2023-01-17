import pyodbc
import pandas as pd
import re

#### Task 1: Create a Connection to the SQL Database
conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                      'Server=OMAT-SQL1.VM.PSC\SQLEXPRESS;'
                      'Database=Stevie_AdventureWorks;'
                      'TrustedConnection=no;'
                      'UID=stevie;'
                      'PWD=He1!ow0rldSSMSci;'
                      )
# cursor=conn.cursor()

query='select * from Person.EmailAddress'
ea=pd.read_sql(query, conn)

query='select * from Person.Password'
p=pd.read_sql(query, conn)

query='select * from Sales.CreditCard'
cc = pd.read_sql(query, conn)

#### Task 2: Left Join Email Address and Password Tables
person=ea.merge(p, how='left', on='BusinessEntityID')
person.head()
len(person)

#### Task 3: Email Addresses that begin with the letter P
person['EmailAddress']=person['EmailAddress'].astype(str)
person[person.EmailAddress.str.contains('^p')]

#### Task 4: Emails that contain the name 'dylan'
person[person.EmailAddress.str.contains(r'(?:.*)(dylan)(?:.*)')]

#### Task 5: Display Customers who have credit cards that expire in 2007
cc.head()
cc[cc['ExpYear']==2007]

#### Task 6: Dummy Encode the ExpYear Column
dummy=pd.get_dummies(cc['ExpYear'])
dummy=dummy.add_prefix('exp_')
cc=pd.concat([cc, dummy], axis=1)
cc.head()
#### Task 7: Create ExpMonthCategorical Column
import calendar

cc['ExpMonthCategorical'] = cc['ExpMonth'].apply(lambda x: calendar.month_name[x])

cc.head()
# Additional Task
query = 'select CustomerID, count(distinct SalesOrderID) as NumTransactions, TotalDue from Sales.SalesOrderHeader group by CustomerID, TotalDue order by TotalDue DESC, NumTransactions DESC;'
h=pd.read_sql(query, conn)
h.head()
query='select * from Sales.SalesOrderHeader'
h=pd.read_sql(query, conn)

query='select * from Sales.SalesOrderDetail'
d=pd.read_sql(query, conn)

query='select * from Production.Product'
prod = pd.read_sql(query, conn)
sales = h.merge(d, on='SalesOrderID')
customer = sales.merge(prod, on='ProductID')
customer.columns
df=customer[['CustomerID', 'SalesOrderID', 'Name', 'LineTotal', 'OrderQty']].sort_values(by='CustomerID')
df=df.sort_values(by='OrderQty', ascending=False).groupby('CustomerID').head(3)
print(df.head(25))
# cursor.close()
conn.close()