import mysql.connector
import pandas as pd

chunksize = 100
with pd.read_csv('../CHARTEVENTS.csv', chunksize=chunksize) as reader:
    counter = 0
    for chunk in reader:
        cnx = mysql.connector.connect(user='monty', password='letmein', host='localhost', database='mimicdb', port=3399)
        cursor = cnx.cursor()
        for row in chunk.iterrows():
            list = row[1].values
            counter += 1
            tuplevar = tuple(list)[0:13]
            with open('log.txt','a') as f:
                f.write(str(counter)+";")
            print(str(counter))
            print(tuplevar)
            row_id = tuplevar[0]
            subject_id = tuplevar[1]
            hadm_id = tuplevar[2]
            icustay_id = tuplevar[3]
            item_id = tuplevar[4]
            charttime = tuplevar[5]
            storetime = tuplevar[6]
            cgid = tuplevar[7]
            valuece = tuplevar[8]
            valuenum = tuplevar[9]
            valueuom = tuplevar[10]
            warning = tuplevar[11]
            error = tuplevar[12]
            resultstatus = tuplevar[13]
            stopped = tuplevar[14]
            alltuple = ()
            cursor.execute("INSERT INTO CHARTEVENTS VALUES(%s,%s,%s,%s,%s,'%s','%s',%s,'%s',%s,'%s',%s,%s,NULL,NULL)" % tuplevar)
        cnx.commit()
        cursor.close()
        cnx.close() 
