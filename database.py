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
db_connection_string = "mysql+pymysql://i8eui9t5t23dkw5va23d:pscale_pw_cBOfUYCQqyQ4w2vSW4wZyA79PF6faSvXUGaxQhD9va8@aws.connect.psdb.cloud/fararadatawarehouse?charset=utf8mb4"

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
#     print(result.all())
    # print("type(result):", type(result))
    # result_all = result.all()
    # print("type(result.all())", type(result_all))
    # print("result_all():", result_all) 