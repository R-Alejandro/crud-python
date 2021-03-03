import psycopg2

class dataBase:
    __dbname = "agendac"
    __user = "postgres"
    __pwd = "1234" #seguridad 100% :v

    @classmethod
    def conexion(cls):
        return psycopg2.connect(database=cls.__dbname,user=cls.__user,password=cls.__pwd)
