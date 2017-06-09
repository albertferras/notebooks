class DBConnection:
    def __init__(self, dsn):
        print('Connected to real database')
        self.dsn = dsn

    def cursor(self):
        return Cursor()

    def commit(self):
        print('Saved changes')

class Cursor:
    def execute(self, query):
        print("Executed query={}".format(query))

def connect(dsn):
    return DBConnection(dsn)