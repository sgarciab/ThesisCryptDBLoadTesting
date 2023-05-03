import mysql.connector
import pandas as pd
import math
import sys 

def replaceNanValueForNull(value):
    print('---replaceNanValueForNull')
    print(type(value))
    print(value)
    print('+++')
    if math.isnan(value):
        return 'NULL'
    return value

def replaceNanValueForNotNull(value):
    print('---replaceNanValueForNotNull')
    print(type(value))
    print(value)
    print('+++')
    if math.isnan(value):
        return 0
    return value     

def replaceEmptyStringForNull(value):
    print('---replaceEmptyStringForNull')
    print(type(value))
    print(value)
    print('+++')
    if not value:
        return 'NULL'
    return value   
try:
    chunksize = 10
    with pd.read_csv('../LABEVENTS.csv', chunksize=chunksize) as reader:
        counter = 0
        for chunk in reader:
            #cnx = mysql.connector.connect(user='monty', password='letmein', host='54.173.121.41', database='mimicdb_plain', port=3306)
            cnx = mysql.connector.connect(user='monty', password='letmein', host='localhost', database='mimicdb', port=3399)
            cursor = cnx.cursor()
            for row in chunk.iterrows():
                list = row[1].values
                counter += 1
                tuplevar = tuple(list)[0:10]
                with open('log.txt','a') as f:
                    f.write(str(counter)+";")
                print(str(counter))
                print(tuplevar)
                row_id = replaceNanValueForNull(tuplevar[0])
                subject_id = replaceNanValueForNull(tuplevar[1])
                hadm_id = replaceNanValueForNull(tuplevar[2])
                item_id = tuplevar[3]
                charttime = tuplevar[4]
                valuece = replaceEmptyStringForNull(tuplevar[5])
                valuenum = replaceNanValueForNull(tuplevar[6])
                valueuom = replaceEmptyStringForNull(tuplevar[7])
                alltuple = (row_id,subject_id, hadm_id,item_id,charttime,valuece,valuenum,valueuom)
                print(alltuple)
                if counter > 0:
                    query = "INSERT INTO LABEVENTS VALUES(%s,%s,%s,%s,'%s','%s',%s,'%s',NULL)" % alltuple
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
