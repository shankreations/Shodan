import shodan

API_KEY = "YOUR API HERE"

api=shodan.Shodan(API_KEY)

try:
	results = api.search('apache')
	print("Total results found: \t" + str(results["total"]))
	for result in results['matches']:
		print("IP:==========\t" + result["ip_str"])
		print("=========="+result['data'])
		print("")
except shodan.APIError as e:
	print("Error is "+e)
