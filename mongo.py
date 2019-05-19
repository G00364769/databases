import pymongo
myclient = None

def connect():
	global myclient
	myclient=pymongo.MongoClient(host="localhost",port=27017)
	myclient.admin.command('ismaster')
	
#def insert():
    #mydb=myclient["project"]
    #docs=mydb["docs"]
    #query={"car.engineSize":1.3}
	##db.docs.find({"car.engineSize":1.3})
    #people=docs.find(query)
    #for p in people:
        #print(p)

	
def getengsize(engine):
	connect()
	if (not myclient):
		print("Not connected to db")
		#connect()
	else:
		print("Already Connected")
		try:
			
			mydb=myclient["project"]
			docs=mydb["docs"]
			#print(condition)
			query={"car.engineSize":engine}
			#db.docs.find({"car.engineSize":1.3})
			print(query)
			people=docs.find(query)
			for eg in people:
				 
				print('{0} | {1}| {2} | {3}'.format(eg["_id"],eg['car']["reg"],eg["car"]['engineSize'],eg['addresses']))
		except Exception as e:
			print("Error",e)
		
			
def getcar(id,reg,engine):
	#connect()
	if (not myclient):
		print("Not connected to db")
		connect()
	else:
		print("Already Connected")
		try:
			
			mydb=myclient["project"]
			docs=mydb["docs"]
			#condition = engine
			#print(condition)
			query={"_id":int(id), "car": { "reg":reg,"engineSize":float(engine)}}
			x = docs.insert_one(query)
			query = {"_id":int(id)}
			car = docs.find(query)
			
			for eg in car:
				print(eg)
		except Exception as e:
			print("Error",e)
