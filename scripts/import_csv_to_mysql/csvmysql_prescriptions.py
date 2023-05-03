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
    with pd.read_csv('../PRESCRIPTIONS.csv', chunksize=chunksize) as reader:
        counter = 0
        for chunk in reader:
            #cnx = mysql.connector.connect(user='monty', password='letmein', host='54.173.121.41', database='mimicdb_plain', port=3306)
            cnx = mysql.connector.connect(user='monty', password='letmein', host='localhost', database='mimicdb', port=3399)
            cursor = cnx.cursor()
            for row in chunk.iterrows():
                list = row[1].values
                counter += 1
                tuplevar = tuple(list)[0:20]
                with open('log.txt','a') as f:
                    f.write(str(counter)+";")
                print(str(counter))
                print(tuplevar)
                row_id = replaceNanValueForNull(tuplevar[0])
                subject_id = replaceNanValueForNull(tuplevar[1])
                hadm_id = replaceNanValueForNull(tuplevar[2])
                icustay_id = replaceNanValueForNull(tuplevar[3])
                startDate = tuplevar[4]
                endDate = tuplevar[4]
                drug_type = replaceEmptyStringForNull(tuplevar[6])
                drug = replaceEmptyStringForNull(tuplevar[7])
                drug_name_poe = replaceEmptyStringForNull(tuplevar[8])
                drug_name_generic = replaceEmptyStringForNull(tuplevar[9])
                formulary_drug_cd = replaceEmptyStringForNull(tuplevar[10])
                gsn = replaceEmptyStringForNull(tuplevar[11])
                ndc = replaceEmptyStringForNull(tuplevar[12])
                prod_strength = replaceEmptyStringForNull(tuplevar[13])
                dose_val_rx = replaceEmptyStringForNull(tuplevar[14])
                
                alltuple = (row_id,subject_id, hadm_id, icustay_id,startDate,endDate,drug_type,drug,drug_name_poe,drug_name_generic,formulary_drug_cd,gsn,ndc,prod_strength,dose_val_rx)
                print(alltuple)
                if counter >=0 :
                    query = "INSERT INTO PRESCRIPTIONS VALUES(%s,%s,%s,%s,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','','','','')" % alltuple
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
