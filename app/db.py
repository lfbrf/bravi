import mysql.connector
DB_USERNAME = ""
DB_PASSWORD = ""

def create_initial_structure_if_not_exists_db():
    try:
        db = mysql.connector.connect(host="localhost",user=DB_USERNAME,password=DB_PASSWORD)
        cursor = db.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS bravi")
        cursor.execute("USE bravi ")
        cursor.execute("CREATE TABLE if not exists piece (id MEDIUMINT NOT NULL AUTO_INCREMENT, name VARCHAR(255), type VARCHAR(255), color VARCHAR(255), PRIMARY KEY (id))")
        cursor.execute("CREATE TABLE if not exists possibilities (id MEDIUMINT NOT NULL AUTO_INCREMENT, all_turns VARCHAR(510), PRIMARY KEY (id) , piece_id MEDIUMINT , FOREIGN KEY(piece_id) REFERENCES piece(id) )")
        cursor.close()
    except mysql.connector.Error as error:
        print("Failed to initiate database with tables {}".format(error))
    finally:
        if db.is_connected():
            db.close()
            cursor.close()          

def drop_database(): 
    try:       
        db = mysql.connector.connect(host="localhost",user=DB_USERNAME,password=DB_PASSWORD)
        cursor = db.cursor()
        cursor.execute("DROP DATABASE bravi")
        cursor.close()
    except mysql.connector.Error as error:
        print("Failed to drop drop database {}".format(error))    
    finally:
        if db.is_connected():
            db.close()
            cursor.close()          

def insert_into_possibilities(piece_id, all_turns):
    try:
        print(f"INSERT INTO possibilities(piece_id, all_turns) values({piece_id}, '{all_turns}')")
        db = mysql.connector.connect(host="localhost",user=DB_USERNAME,password=DB_PASSWORD)
        cursor = db.cursor()
        cursor.execute("USE bravi ")
        cursor.execute(f'INSERT INTO possibilities(piece_id, all_turns) values({piece_id}, "{all_turns}" )')   
        piece_id = cursor.lastrowid
        db.commit()
        cursor.close()
        return str(piece_id)
    except mysql.connector.Error as error:
        print("Failed to insert record into possibilities table {}".format(error))    
    finally:
        if db.is_connected():
            db.close()
            cursor.close()

def insert_into_piece(name, type, color):
    try:
        db = mysql.connector.connect(host="localhost",user=DB_USERNAME,password=DB_PASSWORD)
        cursor = db.cursor()
        cursor.execute("USE bravi ")
        cursor.execute(f"INSERT INTO piece(name, type, color) values('{name}', '{type}', '{color}')")   
        piece_id = cursor.lastrowid
        db.commit()
        cursor.close()
        return str(piece_id)
    except mysql.connector.Error as error:
        print("Failed to insert record into piece table {}".format(error))    
    finally:
        if db.is_connected():
            db.close()
            cursor.close()            

def select_piece_by(id):
    try:
        db = mysql.connector.connect(host="localhost",user=DB_USERNAME,password=DB_PASSWORD)
        sql_select_Query = f"select id, name, type, color from piece where id = {id}"
        cursor = db.cursor()
        cursor.execute("USE bravi ")
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        piece_info = {}
        for row in records:
            piece_info = {
                'id': row[0],
                'name': row[1],
                'type': row[2],
                'color': row[3]
            }
        return piece_info
    except mysql.connector.Error as e:
        print("Error reading data from MySQL table", e)
    finally:
        if db.is_connected():
            db.close()
            cursor.close()