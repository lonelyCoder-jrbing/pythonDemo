import pymysql

db = pymysql.connect("127.0.0.1","root","root","test" ) # 打开数据库连接
cursor = db.cursor()
# curser = pymysql.cursors.Cursor
cursor.execute(query="SELECT VERSION()")                    # 使用 execute() 方法执行 SQL 查询
data = cursor.fetchone()                              # 使用 fetchone() 方法获取单条数据
print ("Database version : %s " % data)
db.close()
