import mysql.connector
import sys 

try:
    #cnx = mysql.connector.connect(user='monty', password='letmein', host='54.173.121.41', database='mimicdb_plain', port=3306)
    cnx = mysql.connector.connect(user='monty', password='letmein', host='34.239.153.139', database='mimicdb', port=3399)
    cursor = cnx.cursor()
    cursor.execute("SELECT `item`.`label`, `chartevents`.`storetime`, `chartevents`.`value`, `chartevents`.`valueuom` FROM `CHARTEVENTS1` AS `chartevents` LEFT JOIN `D_ITEMS` AS `item` ON `chartevents`.`itemid` = `item`.`itemid` WHERE `chartevents`.`subject_id` = 23 ORDER BY `chartevents`.`charttime` LIMIT 20")
    myresult = cursor.fetchall()

    for x in myresult:
        print(x)
    cursor.close()
    cnx.close() 
except Exception as error:
    print(error)
    print(sys.exc_info())
