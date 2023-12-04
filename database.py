# import sqlalchemy
# print(sqlalchemy.__version__)
# import os
from sqlalchemy import create_engine, text

# import ssl
# print(ssl.OPENSSL_VERSION) 

# database = 'fararadatawarehouse'
# hostname = 'aws.connect.psdb.cloud'
# username = 'i8eui9t5t23dkw5va23d'
# password = 'pscale_pw_NCbmbbYj7wxwlxfNRQWv00xWWjjmBehti3G1gTtsk55'

# From sqlalchemy documentation
# mysql+pymysql://<username>:<password>@<host>/<dbname>[?<options>]
db_connection_string = "mysql+pymysql://wh1x4lqjob1xuh5upzsr:pscale_pw_5HhQMULzDzBZRI2LdRwWkIicybXkSjGUwk6v5eJtsNq@aws.connect.psdb.cloud/fararadatawarehouse?charset=utf8mb4"

engine = create_engine(
    db_connection_string,
    connect_args={
       "ssl": {
           "ssl_cert": "/etc/ssl/cert.pem"                               
        }
    }
)



with engine.connect() as conn:
    result = conn.execute(text("SELECT * from test"))

    # result_dicts = []
    # for row in result.all():
    #     result_dicts.append(dict(row))
    result_dicts = []
    for row in result.all():
        result_dicts.append(dict(row._mapping))

    print(result_dicts)
    # print("type(result):", type(result))
    # result_all = result.all()
    # print("type(result.all())", type(result_all))
    # first_result = result_all[0]
    # column_names = result.keys()
    # first_result_dict = dict(zip(column_names, first_result))
    # print(first_result_dict)
        # print("type(first_result_dict):", type(first_result_dict))
