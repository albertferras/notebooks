from database import connect

def clean_db():
    conn = connect(dsn="user='123', password='xxx', host='hotels.prod.aws.com'")
    cursor = conn.cursor()
    cursor.execute('TRUNCATE clickouts')
    cursor.execute('TRUNCATE images')
    conn.commit()