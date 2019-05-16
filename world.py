import pymysql

conn=None

def connect():
    global conn
    conn=pymysql.connect(host="localhost",user="root",password="Jump18joy",db="world",cursorclass=pymysql.cursors.DictCursor)
	

def get_city():
    if (not conn):
        print("No Connection")
        connect();
    else:
        print("Already Connected")
    query="select* FROM city LIMIT 15"
    print(query)
	
    with conn:
        cursor=conn.cursor()
        cursor.execute(query)
        x=cursor.fetchall()
        return x
def get_newcity(cityname,countrycode,District,Population):
	if (not conn):
			print("No Connection")
			connect();
	else:
		print("Already Connected")
	sql="INSERT INTO City(Name,CountryCode,District,Population)VALUES(%s,%s,%s,%s)"
	print(sql)
		
	with conn:
		try:
			cursor=conn.cursor()
			x=cursor.execute(sql,(cityname,countrycode,District,Population))
			conn.commit()
		except pymysql.err.IntegrityError :
			print("CountryCode",countrycode,"doesnot exists")
			
def get_countryname(Name):
	if (not conn):
			print("No Connection")
			connect();
	else:
		print("Already Connected")
	condition = "'%"+Name+"%'"
	
	sql="select* FROM city where Name like " + condition
	print(sql)
		
	with conn:
		try:
			cursor=conn.cursor()
			cursor.execute(sql)
			x=cursor.fetchall()
			return x
		except Exception as error:
			print(error)
			
def get_popultion(condition,population):
	if(not conn):
		connect();
	else:
		print("Already Connected")
	sql="select* FROM city where Population" + condition + population
	print(sql)
	with conn:
		try:
			cursor=conn.cursor()
			cursor.execute(sql)
			x=cursor.fetchall()
			return x
		except Exception as error:
			print(error)
	
		
			

