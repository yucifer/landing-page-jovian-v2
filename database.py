
from sqlalchemy import create_engine
from sqlalchemy import text
import os


# PASSWORD = os.getenv('DATABASE_PASSWORD')
# print(PASSWORD)
# USERNAME = os.environ['USER']

# print(PASSWORD)

db_connect_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(db_connect_string,  
    connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem",
        }
})

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
    for row in result.all():
      jobs.append(row._mapping)
    return jobs
load_jobs_from_db()