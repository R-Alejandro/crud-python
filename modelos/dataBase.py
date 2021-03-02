import psycopg2

class dataBase:
    __dbname = "agendac"
    __user = "postgres"
    __pwd = "1234" #seguridad 100% :v

    @classmethod
    def conexion(cls):
        return psycopg2.connect(database=cls.__dbname,user=cls.__user,password=cls.__pwd)


""" class dataBase:
    __dbname = "agendac"
    __user = "postgres"
    __pwd = "1234" #seguridad 100% :v
    __conexion = None #null

    def __init__(self, *args): #constructor
        self.con = psycopg2.connect(
            database = args[0],
            user = args[1],
            password = args[2]
        )
        #self.con = psycopg2.connect(database="agendac",user="postgres",password="1234")
    
    @classmethod
    def instancia(cls):  #metodo estatico para instanciar la misma clase varias veces
        if cls.__conexion == None: #cls.__dbname, cls.__user, cls.__pwd
            cls.__conexion = dataBase(cls.__dbname, cls.__user, cls.__pwd)
        return cls.__conexion #objeto de la clase
    
    def conexion(self):
        conexion = self.con
        return conexion """





