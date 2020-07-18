import pyodbc

class NWProducts:

    def __init__(self):
        self.server = 'databases.spartaglobal.academy'
        self.database = 'Northwind'
        self.username = 'SA'
        self.password = 'Passw0rd2018'
        self.connection_string = "DRIVER={SQL Server};"
        self.connection_string += f"SERVER={self.server};"
        self.connection_string += f"DATABASE={self.database};"
        self.connection_string += f"UID={self.username};"
        self.connection_string += f"PWD={self.password}"
        self.docker_northwind = pyodbc.connect(self.connection_string)
        self.cursor = self.docker_northwind.cursor()
        #cursor.execute("SELECT OrderID FROM [Order Details] GROUP BY OrderID;")
        #cursor.execute("SELECT * FROM Customers;")
        #row = cursor.fetchall()
        #print(row)

    def _sql_query(self, query):
        return self.cursor.execute(query)

    def average_unit_price(self):
        records = self._sql_query("SELECT * FROM Products;")
        sum = 0
        count = 0
        for row in records:
            sum += row.UnitPrice
            count += 1
        average = sum / count
        ave_unit_price = average
        return ave_unit_price

    def average_unit_price_sql(self):
        records = self._sql_query("SELECT * FROM Products;")
        row = records.fetchone()
        return row[0]

## Will only run if file called directly
## If imported this block will not run
# In another file: from please_work import NWProducts
# nw = MWProducts()  -  run it and see that this block won't run
if __name__ == "__main__":
    nw = NWProducts()
    print(nw.average_unit_price())
    print(nw.average_unit_price_sql())


## BLOCK queries
#
# query = '''
#         SELECT CategoryID, ANG(UnitPrice) AS UnitPrice
#         FROM Products
#         GROUP BY CategoryID
#         '''
# cursor.execute(query)
#
# for row in cursor:
#     print(row.CategoryID, row.UnitPrice)
