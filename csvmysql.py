import mysql.connector
import pandas as pd

cnx = mysql.connector.connect(user='monty', password='letmein', host='3.234.222.228', database='mimicdb', port=3399)
cursor = cnx.cursor()


chunksize = 1000
with pd.read_csv('CHARTEVENTS.csv', chunksize=chunksize) as reader:
    for chunk in reader:
        for row in chunk.iterrows():
            list = row[1].values
            print(list)
            tuplevar = tuple(list)[0:13]
            print(tuplevar)
            cursor.execute("INSERT INTO CHARTEVENTS VALUES(%s,%s,%s,%s,%s,'%s','%s',%s,'%s',%s,'%s',%s,%s,NULL,NULL)" % tuplevar)
cursor.close()
cnx.close() 