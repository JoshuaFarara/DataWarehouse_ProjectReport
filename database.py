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
db_connection_string = os.getenv("DB_CONNECTION_STRING")

engine = create_engine(
    db_connection_string,
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
    
def load_dim_gparank_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * from dim_gparank"))
        # footsteps = []
        # for row in result.all():
        #     footsteps.append(dict(row._mapping))
        gparank_footsteps = []
        for row in result.fetchall():
            gparank_footsteps.append(dict(row._mapping))
        # footsteps = [dict(row) for row in result.fetchall()]  # Fetch all rows and convert to list of dictionaries
        return gparank_footsteps

def load_dim_status_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * from dim_status"))
        # footsteps = []
        # for row in result.all():
        #     footsteps.append(dict(row._mapping))
        dim_status_footsteps = []
        for row in result.fetchall():
            dim_status_footsteps.append(dict(row._mapping))
        # footsteps = [dict(row) for row in result.fetchall()]  # Fetch all rows and convert to list of dictionaries
        return dim_status_footsteps
    
def load_dim_time_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * from dim_time"))
        # footsteps = []
        # for row in result.all():
        #     footsteps.append(dict(row._mapping))
        dim_time_footsteps = []
        for row in result.fetchall():
            dim_time_footsteps.append(dict(row._mapping))
        # footsteps = [dict(row) for row in result.fetchall()]  # Fetch all rows and convert to list of dictionaries
        return dim_time_footsteps
    
def get_column_names_from_table(table_name):
    with engine.connect() as conn:
        inspector = inspect(engine)
        columns = inspector.get_columns(table_name)
        column_names = [column['name'] for column in columns]
        return column_names
    
def get_table_names():
    inspector = inspect(engine)
    return inspector.get_table_names()
