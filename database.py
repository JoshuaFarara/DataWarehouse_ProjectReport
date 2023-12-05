from dotenv import load_dotenv

# import sqlalchemy
# print(sqlalchemy.__version__)
import os
# import inspect
from sqlalchemy import create_engine, text, engine, inspect

# import ssl
# print(ssl.OPENSSL_VERSION) 

# database = 'fararadatawarehouse'
# hostname = 'aws.connect.psdb.cloud'
# username = 'i8eui9t5t23dkw5va23d'
# password = 'pscale_pw_NCbmbbYj7wxwlxfNRQWv00xWWjjmBehti3G1gTtsk55'

# From sqlalchemy documentation
# mysql+pymysql://<username>:<password>@<host>/<dbname>[?<options>]
load_dotenv()
DB_CONNECTION_STRING = os.getenv("DB_CONNECTION_STRING")

engine = create_engine(
    DB_CONNECTION_STRING,
    connect_args={
       "ssl": {
           "ssl_cert": "/etc/ssl/cert.pem"                               
        }
    }
)



# with engine.connect() as conn:
#     result = conn.execute(text("SELECT * from test"))

#     # result_dicts = []
#     # for row in result.all():
#     #     result_dicts.append(dict(row))
#     result_dicts = []
#     for row in result.all():
#         result_dicts.append(dict(row._mapping))

#     print(result_dicts)
    
def load_dim_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * from test"))
        # footsteps = []
        # for row in result.all():
        #     footsteps.append(dict(row._mapping))
        footsteps = []
        for row in result.fetchall():
            footsteps.append(dict(row._mapping))
        # footsteps = [dict(row) for row in result.fetchall()]  # Fetch all rows and convert to list of dictionaries
        return footsteps
    
def load_dim_degree_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * from dim_degrees"))
        # footsteps = []
        # for row in result.all():
        #     footsteps.append(dict(row._mapping))
        degree_footsteps = []
        for row in result.fetchall():
            degree_footsteps.append(dict(row._mapping))
        # footsteps = [dict(row) for row in result.fetchall()]  # Fetch all rows and convert to list of dictionaries
        return degree_footsteps
    
def load_dim_gparanks_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * from dim_gparanks"))
        # footsteps = []
        # for row in result.all():
        #     footsteps.append(dict(row._mapping))
        gparanks_footsteps = []
        for row in result.fetchall():
            gparanks_footsteps.append(dict(row._mapping))
        # footsteps = [dict(row) for row in result.fetchall()]  # Fetch all rows and convert to list of dictionaries
        return gparanks_footsteps
    
def get_table_names():
    inspector = inspect(engine)
    return inspector.get_table_names()
