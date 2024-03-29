import mysql.connector
import pandas as pd
import math
import sys 

def replaceNanValueForNull(value):
    if math.isnan(value):
        return 'NULL'
    return value

def replaceNanValueForNotNull(value):
    if math.isnan(value):
        return 0
    return value     

def replaceEmptyStringForNull(value):
    if not value:
        return 'NULL'
    return value   
try:
    chunksize = 10
    with pd.read_csv('../CHARTEVENTS.csv', chunksize=chunksize) as reader:
        counter = 0
        for chunk in reader:
            cnx = mysql.connector.connect(user='monty', password='letmein', host='54.173.121.41', database='mimicdb_plain', port=3399)
            cursor = cnx.cursor()
            for row in chunk.iterrows():
                list = row[1].values
                counter += 1
                tuplevar = tuple(list)[0:13]
                with open('log.txt','a') as f:
                    f.write(str(counter)+";")
                print(str(counter))
                print(tuplevar)
                row_id = replaceNanValueForNull(tuplevar[0])
                subject_id = replaceNanValueForNull(tuplevar[1])
                hadm_id = replaceNanValueForNull(tuplevar[2])
                icustay_id = replaceNanValueForNull(tuplevar[3])
                item_id = tuplevar[4]
                charttime = tuplevar[5]
                storetime = replaceEmptyStringForNull(tuplevar[6])
                cgid = replaceNanValueForNull(tuplevar[7])
                valuece = replaceNanValueForNotNull(tuplevar[8])
                valuenum = replaceNanValueForNull(tuplevar[9])
                valueuom = replaceEmptyStringForNull(tuplevar[10])
                warning = replaceNanValueForNull(tuplevar[11])
                error = replaceNanValueForNull(tuplevar[12])
                alltuple = (row_id,subject_id, hadm_id, icustay_id,item_id,charttime,storetime,cgid,valuece,valuenum,valueuom,warning,error)
                print(alltuple)
                if counter < 2070910:
                    query = "INSERT INTO CHARTEVENTS VALUES(%s,%s,%s,%s,%s,'%s','%s',%s,'%s',%s,'%s',%s,%s,NULL,NULL)" % alltuple
                    print(query)
                    try:
                        cursor.execute(query)
                    except Exception as error:
                        with open('log.txt','a') as f:
                            f.write(str(error)+";")
                        print(error)
                        print(sys.exc_info())
            cnx.commit()
            cursor.close()
            cnx.close() 
except Exception as error:
    with open('log.txt','a') as f:
        f.write(str(error)+";")
    print(error)
    print(sys.exc_info())
