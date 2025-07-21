from fastapi import FastAPI
import pyodbc
import json
from pydantic import BaseModel

app = FastAPI()
database_config = {
    'server': '43.204.45.205,1560',
    'database' :  'HSRPOEM',
    'username' : 'R3480',
    'password' : 'Yashwant@13',
    'driver' : '{SQL Server}'
}

conn = pyodbc.connect(f"DRIVER={database_config['driver']};SERVER={database_config['server']};DATABASE={database_config['database']};UID={database_config['username']};PWD={database_config['password']};")


class Item(BaseModel):
    Name : str
    Description : str 
    Price : float




@app.get("/get_data")
def get_data():
    cursor = conn.cursor()
    cursor.execute("select * from items")
    rows = cursor.fetchall()
    columns = [column[0] for column in cursor.description]
    lst = [] # without inbuilt function
    for y in rows:
        dic = {}
        for j in range (len(columns)):
            dic[columns[j]] = y[j]
        lst.append(dic)

    x = json.dumps(lst, default=str)
    
    # rows = [dict(zip(columns, row)) for row in rows] # Inbuilt function
    # x = json.dumps(rows, default=str)
    cursor.close()
    return x


@app.post("/Create_data")
def create_data(items : Item):
    cursor = conn.cursor()
    lst = [items.Name, items.Description, items.Price]

    query = 'insert into items (Name, Description, Price) values (?,?,?)'

    cursor.execute(query,lst)
    conn.commit()

    cursor.close()
    return lst

@app.post("/update_data")
def update_data(items: Item):
    cursor = conn.cursor()
    lst  = [items.Description, items.Price, items.Name]

    query = 'update Items ' \
    'set Description = ?, Price = ? ' \
    'where Name = ?'

    cursor.execute(query, lst)
    conn.commit()
    cursor.close()
    return lst


@app.post("/delete_data")
def delete_data(items: Item):
    cursor = conn.cursor()
    lst = [items.Name, items.Description, items.Price]

    query = 'delete from Items where Name = ?'

    cursor.execute(query, lst)
    conn.commit()
    conn.close()
    return lst
