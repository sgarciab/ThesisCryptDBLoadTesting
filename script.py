import os

# PASSWORD
# FZzHfwDPeCK2s4Az
# F3^)$y3AGRC`]786eyJ[H}s6"2_p_MEr
for x in range(0, 836):
    formattedNumber = '{:03d}'.format(x)
    command = f'C:\\Users\\Xtreme\\Downloads\\mysql-5.7.30-winx64\\mysql-5.7.30-winx64\\bin\\mysql.exe --defaults-file="C:\\Users\Xtreme\Documents\TesisCryptDB\loadtesting\mysql.cnf"  --protocol=tcp --host=3.83.187.71 --user=monty --port=3399 --default-character-set=utf8 --comments --database=mimiciiiv14  < "C:\\Users\\Xtreme\\Documents\\dumps\\Dump20210618\\mimiciiiv14_CHARTEVENTS_split\\mimiciiiv14_CHARTEVENTS_{formattedNumber}.sql"'
    print("Executing")
    print(command)
    stream = os.popen(command)
    output = stream.read()
    print("EXECUTED "+str(x))