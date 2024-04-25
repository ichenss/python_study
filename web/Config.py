import web

DB_HOST = '192.168.200.128'
DB_PORT = 3306
DB_USER = 'root'
DB_PW = '123123'
DB_NAME = 'user'

gdb = web.database(
    dbn='mysql',
    host=DB_HOST,
    port=DB_PORT,
    user=DB_USER,
    PW=DB_PW,
    db=DB_NAME
)
