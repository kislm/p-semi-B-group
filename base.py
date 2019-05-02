import json
import urllib.request

Geolocation_key = "AIzaSyBpXnSW_D-3lUUWdP24_HavgNwDMO0o0lI" #apiキー
url = "https://www.googleapis.com/geolocation/v1/geolocate?key="+ Geolocation_key
obj = {
}
json_data = json.dumps(obj).encode("utf-8")

req = urllib.request.Request(url=url,data=json_data,headers={'Content-type':'application/json'})
response = urllib.request.urlopen(req)
content = json.loads(response.read().decode('utf-8'))
lat = content['location']['lat']    #緯度
lng = content['location']['lng']    #経度
radius = content['accuracy']        #正確さ（半径）

dict = {}
dict["lat"] = str(lat)
dict["lng"] = str(lng)
dict["radius"] = str(radius)

#print(content)
#print(lat)
#print(lng)
#print(radius)
#print(dict.get("lat"))
#print(dict.get("lng"))
