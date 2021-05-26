f = open("test.csv", "w")
f.write("Opportunity_ID,Target\n")
for i in range (1567):
	f.write(str(10689+i)+",0\n")
f.close()