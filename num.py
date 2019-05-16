import world
import mongo
def main():
	Display_main()
	while True:
        
		choice = input("choice")
		if choice =="x":
			break
		elif (choice=="1"):
			city=world.get_city()
            #print(city)
			for allcity in city:
				print(allcity["ID"],"|",allcity["Name"],"|",allcity["CountryCode"],"|",allcity["District"],"|",allcity["Population"])
				
				###############2###################
		elif (choice=="2"):
			print("Cities by Population")
			print("--------------")
			while True:
				#try:
			
				condition=input("Enter in <, > or =:")
				if condition== "<" or condition== ">" or condition== "=":
					break
				else:
					print("Enter in <, > or =:")
			
			while True:
				#try:
			
				population=input("Enter the Populations:")
				if population.isdigit()== True:
					#print("pass")
					break
				else:
					print("Enter the Populations:")
					#population=input("Enter the Populations:")
			pop=world.get_popultion(condition,population)
			for popu in pop:
				print(popu["ID"],"|",popu["Name"],"|",popu["CountryCode"],"|",popu["District"],"|",popu["Population"])

###############7###################

		elif (choice=="7"):
			print("Cities by Population")
			print("--------------")
			while True:
				#try:
			
				condition=input("Enter in <, > or =:")
				if condition== "<" or condition== ">" or condition== "=":
					break
				else:
					print("Enter in <, > or =:")
			
			while True:
				#try:
			
				population=input("Enter the Populations:")
				if population.isdigit()== True:
					#print("pass")
					break
				else:
					print("Enter the Populations:")
					#population=input("Enter the Populations:")
			pop=world.get_popultion(condition,population)
			for popu in pop:
				print(popu["ID"],"|",popu["Name"],"|",popu["CountryCode"],"|",popu["District"],"|",popu["Population"])
			
		###############3###################
		
		elif (choice=="3"):
			print("Add new city")
			print("--------------")
			cityname=input("Enter city name:")
			countrycode=input("Enter the country code:")
			District=input("Enter the DistrictName:")
			Population=int(input("Enter the populations:"))
			#try:
            
			world.get_newcity(cityname,countrycode,District,Population)
			Display_main()
            #except Exception as error:
                #print("Error ",error)
				
		elif (choice=="4"):
			print("Show cars by Engine Size")
			print("--------------")
			engine=float(input("Engine Size:"))
			#engine=str(round(engine, 2))
			#try:
            
			test=mongo.getengsize(engine)
			#for eg in test:
				#print(eg["_id"],"|",eg["reg"],"|",eg["engineSize"])
			Display_main()
			#except Exception as error:
				#print("Error ",error)
				
		elif (choice=="5"):
			print("Add new car")
			print("--------------")
			id=input("_ids:")
			reg=input("Enter reg:")
			engine=float(input("Engine Size:"))
			#engine=str(round(engine, 2))
			#try:
            
			test=mongo.getcar(id,reg,engine)
			
			Display_main()
			
				
				###############6###################
		elif (choice=="6"):
			print("Countries by name")
			print("--------------")
			Name= input("Enter the CountryName:")
			choise6=world.get_countryname(Name)
			print(choise6)
			for allcoun in choise6:
				print(allcoun["Name"],"|",allcoun["CountryCode"],"|",allcoun["District"],"|",allcoun["Population"])
				
		
			


		

def Display_main():
    print("World DB")
    print("---------")
    print("MENUE")
    print("=====")
    print("1-View 15 Cities")
    print("2-View Cities by Population")
    print("3-Add New City")
    print("4-Find Car by Engine Size")
    print("5-Add New Car")
    print("6-View Countries by name")
    print("7-View Countries by populations")
    print("x-Exit applications")
if __name__ == "__main__":
    
    main()