from typing import Optional

from fastapi import FastAPI

import mysql.connector
import sys 

app = FastAPI()

@app.get("/api/patient/{id}/chartevent")
def get_patientevents_by_patientid(id: int):
    cnx = get_connection()
    cursor = cnx.cursor()
    mytuple = (id) 
    query = "SELECT `item`.`label`, `chartevents`.`storetime`, `chartevents`.`value`, `chartevents`.`valueuom` FROM `CHARTEVENTS1` AS `chartevents` LEFT JOIN `D_ITEMS` AS `item` ON `chartevents`.`itemid` = `item`.`itemid` WHERE `chartevents`.`subject_id` = %s ORDER BY `chartevents`.`charttime` LIMIT 50" % mytuple
    cursor.execute(query)
    r = convert_to_json(cursor)
    cursor.close()
    cnx.close()
    return r

@app.get("/api/patient/{id}/labevent")
def get_labevents_by_patientid(id: int):
    cnx = get_connection()
    cursor = cnx.cursor()
    mytuple = (id) 
    query = "SELECT `labitem`.`label`, `labevents`.`charttime`, `labevents`.`value`, `labevents`.`valueuom` FROM `LABEVENTS1` AS `labevents` INNER JOIN `D_LABITEMS` AS `labitem` ON `labevents`.`itemid` = `labitem`.`itemid` WHERE `labevents`.`subject_id` = %s ORDER BY `labevents`.`charttime` LIMIT 10" % mytuple
    cursor.execute(query)
    r = convert_to_json(cursor)
    cursor.close()
    cnx.close()
    return r

@app.get("/api/patient/{id}/prescription")
def get_prescription_by_patientid(id: int):
    cnx = get_connection()
    cursor = cnx.cursor()
    mytuple = (id) 
    query = "SELECT `prescriptions`.`row_id`, `prescriptions`.`dose_unit_rx`, `prescriptions`.`dose_val_rx`, `prescriptions`.`drug`, `prescriptions`.`drug_name_generic`, `prescriptions`.`drug_name_poe`, `prescriptions`.`drug_type`, `prescriptions`.`enddate`, `prescriptions`.`form_unit_disp`, `prescriptions`.`form_val_disp`, `prescriptions`.`formulary_drug_cd`, `prescriptions`.`gsn`, `prescriptions`.`hadm_id`, `prescriptions`.`icustay_id`, `prescriptions`.`ndc`, `prescriptions`.`prod_strength`, `prescriptions`.`route`, `prescriptions`.`startdate`, `prescriptions`.`subject_id` FROM `PRESCRIPTIONS` AS `prescriptions` WHERE `prescriptions`.`subject_id` = {id} LIMIT 10" % mytuple
    cursor.execute(query)
    r = convert_to_json(cursor)
    cursor.close()
    cnx.close()
    return r

def get_connection():
    # return  mysql.connector.connect(user='monty', password='letmein', host='54.173.121.41', database='mimicdb_plain', port=3306)
    return  mysql.connector.connect(user='monty', password='letmein', host='LB-CryptDB-bc47dea816a1c26b.elb.us-east-1.amazonaws.com', database='mimicdb', port=3399)

def convert_to_json(cursor):
    r = [dict((cursor.description[i][0], value) \
                    for i, value in enumerate(row)) for row in cursor.fetchall()]
    return r