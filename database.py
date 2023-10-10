
from sqlalchemy import create_engine


db_connect_string = "mysql+pymysql://gtvprj8mblggmnq4yhgx:pscale_pw_K6T9h2PMEftqoEfCdvZH9o1IcT4dLS6c3qAMOYNBOBg@aws.connect.psdb.cloud/joviancareers?charset=utf8mb4"


engine = create_engine(db_connect_string,  
    connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem",
        }
})

