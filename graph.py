
from typing import Sequence
from pandas import read_csv
import pandas as pd
from matplotlib import pyplot
from pandas.core.frame import DataFrame

def draw(file,number):
    dataframe1 = read_csv(file, header=0)

    http_req_durationfilter =  dataframe1['metric_name']=='http_req_duration'


    durationdf = dataframe1[http_req_durationfilter]


    urlfilter = durationdf['url']=='http://localhost:8000/api/patient/7884/chartevent'

    durationdf = durationdf[urlfilter]


    urlfilter = durationdf['expected_response']==True

    durationdf = durationdf[urlfilter]

    durationdf = durationdf.head(number)


    ts = pd.Series(durationdf['metric_value'])
    ax = ts.plot(xlabel='peticion número',ylabel="tiempo de respuesta (ms)")
    ax.legend(['1 nodo de CryptDB','2 nodos de CryptDB','sin CryptDB'])



draw('results/k6_cryptdb3_node_1_users_100.csv',30)
draw('results/k6_cryptdb2_node_2_users_100.csv',30)
draw('results/k6_plain_node_1_users_100.csv',30)

draw('results/k6_cryptdb0_node_1_users_50.csv',30)
draw('results/k6_cryptdb0_node_2_users_50.csv',30)
draw('results/k6_plain_node_1_users_50.csv',30)


draw('results/k6_cryptdb0_node_1_users_10.csv',30)
draw('results/k6_cryptdb0_node_2_users_10.csv',30)
draw('results/k6_plain_node_1_users_10.csv',30)

# c5.2xlarge  v2
draw('results/k6_cryptdb3_node_1_users_100.csv',30)
draw('results/k6_cryptdb2_node_2_users_100.csv',30)
draw('results/k6_plain_node_1_users_100.csv',30)



pyplot.show()