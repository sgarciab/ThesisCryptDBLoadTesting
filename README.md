# ThesisCryptDBLoadTesting

Start the API:
```
uvicorn api:app --reload
```

run k6
```
k6 run  --vus 100 --duration 60s .\script.js
```

RUN THESE COMMANDS TO RUN CRYPTDB

export CRYPTDB_PASS=letmein
export CRYPTDB_USER=monty

change configuration (ip server) in mysql-proxy.cnf
run cdbserver.sh


`pwd`/mysql-src/build/client/mysql -umonty -pletmein -h 127.0.0.1 -P3399 --database=mimicdb  < /home/ubuntu/mimic/Dump20210709/
`pwd`/mysql-src/build/client/mysql -umonty -pletmein -h 3.236.211.63 -P3306


show graphs:
 c:\users\xtreme\appdata\local\programs\python\python39\python.exe .\graph.py
