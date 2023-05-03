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
    with pd.read_csv('../D_ITEMS.csv', chunksize=chunksize) as reader:
        counter = 0
        for chunk in reader:
            cnx = mysql.connector.connect(user='monty', password='letmein', host='54.175.184.83', database='mimicdb_plain', port=3306)
            #cnx = mysql.connector.connect(user='monty', password='letmein', host='localhost', database='mimicdb', port=3399)
            cursor = cnx.cursor()
            for row in chunk.iterrows():
                list = row[1].values
                counter += 1
                tuplevar = tuple(list)[0:10]
                with open('log_items_plano.txt','a') as f:
                    f.write(str(counter)+";")
                print(str(counter))
                print(tuplevar)
                row_id = replaceNanValueForNull(tuplevar[0])
                item_id = tuplevar[1]
                label = replaceEmptyStringForNull(tuplevar[2])
                abbreviation = replaceEmptyStringForNull(tuplevar[3])
                dbsource = replaceEmptyStringForNull(tuplevar[4])
                linksto = replaceEmptyStringForNull(tuplevar[5])
                category = replaceEmptyStringForNull(tuplevar[6])
                unitname = replaceEmptyStringForNull(tuplevar[7])
                paramtype = replaceEmptyStringForNull(tuplevar[8])
                conceptid = replaceEmptyStringForNull(tuplevar[9])
                
                alltuple = (row_id,item_id, label, abbreviation,dbsource,linksto,category,unitname,paramtype)
                print(alltuple)
                if counter >=0 :
                    query = "INSERT INTO D_ITEMS VALUES(%s,%s,'%s','%s','%s','%s','%s','%s','%s',0)" % alltuple
                    print(query)
                    try:
                        cursor.execute(query)
                    except Exception as error:
                        with open('log_items_plano.txt','a') as f:
                            f.write(str(error)+";")
                        print(error)
                        print(sys.exc_info())
            cnx.commit()
            cursor.close()
            cnx.close() 
except Exception as error:
    with open('log_items_plano.txt','a') as f:
        f.write(str(error)+";")
    print(error)
    print(sys.exc_info())
