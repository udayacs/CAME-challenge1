import requests
import time
import json
import mysql.connector as mysql

#Global variables*****************************************************************************    
m_personList = []

m_host = ""
m_user = ""
m_password = ""
m_db = ""
m_port = ""

#funtions***************************************************************************************
def getData():
    url = "https://microsoftedge.github.io/Demos/json-dummy-data/64KB.json"
    
    try:
        # A GET request to the API
        response = requests.get(url)

        global m_personList
        m_personList = json.loads(response.text)
        return True
    except Exception as ex:
        print(ex)
        return False


def loadConfig():
    config = ""
    with open("config.json", "+rt") as configFile:
        config = json.loads(configFile.read())
    #print(config)
    global m_host
    m_host = config["host"]
    global m_user
    m_user = config['user']
    global m_password
    m_password = config['password']
    global m_db
    m_db = config['db']
    global m_port
    m_port = config['port']


def insertToDB():
    try:
        with mysql.connect(host=m_host, user=m_user, password=m_password, port=m_port) as conn:
            #print(conn)
            with conn.cursor() as cur:
                db_sql = f"CREATE DATABASE IF NOT EXISTS {m_db}"
                cur.execute(db_sql)
                cur.execute(f"use {m_db}")

                tbl_sql = """CREATE TABLE IF NOT EXISTS persons (
                    id BIGINT PRIMARY KEY,
                    name VARCHAR(255),
                    language VARCHAR(64),
                    bio TEXT,
                    version VARCHAR(64)
                )"""
                cur.execute(tbl_sql)

                cur.execute("TRUNCATE TABLE persons")

            with conn.cursor(prepared = True) as insert:
                insert_sql = "INSERT INTO persons (id, name, language, bio, version) VALUES(%(id)s, %(name)s, %(language)s, %(bio)s, %(version)s)"
                #print(m_personList)
                insert.executemany(insert_sql, m_personList)
                conn.commit()
                print("Inserted ", insert.rowcount*(-1), " records into persons")

    except Exception as ex:
        print(ex)

#execution*********************************************************************************************************
waitCount = 3
while (not getData()) and (waitCount > 0):
    print(f"Error in getting data, retrying({4-waitCount})...")
    time.sleep(1.5)
    waitCount = waitCount - 1
loadConfig()
insertToDB()
 
