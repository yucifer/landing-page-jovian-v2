
from sqlalchemy import create_engine
import os


PASSWORD = os.environ['PASSWORD']
USERNAME = os.environ['USERNAME']

db_connect_string = "mysql+pymysql://"+ USERNAME + ":" + PASSWORD + "@aws.connect.psdb.cloud/joviancareers?charset=utf8mb4"


engine = create_engine(db_connect_string,  
    connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem",
        }
})

