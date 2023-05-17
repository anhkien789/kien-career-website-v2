import os
from sqlalchemy import create_engine
from sqlalchemy import text

db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))

    jobs = []
    for row in result.all():
      jobs.append(row._mapping)

    #convert to dict
    jobs_dict = []
    for row in jobs:
      jobs_dict.append(dict(row))
    return jobs_dict
