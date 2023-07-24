# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: summarize the earthquake data

import json


# for this challenge, we're going to summarize the earthquake data as follows:
# 1: How many quakes are there in total?
# 2: How many quakes were felt by at least 100 people?
# 3: Print the name of the place whose quake was felt by the most people, with the # of reports
# 4: Print the top 10 most significant events, with the significance value of each

# open the data file and load the JSON
with open("../../30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

# 1: How many quakes are there in total?
print("Total Quakes: ", data["metadata"]["count"])
# print(f"Total Quakes: {data["metadata"]["count"]}")

# 2: How many quakes were felt by at least 100 people?
print("Total quakes felt by at least 100 people: ", sum(quake["properties"]["felt"] is not None and quake["properties"]["felt"] >= 100
          for quake in data["features"]))

# 3: Print the name of the place whose quake was felt by the most people, with the # of reports
def getfelt(dataitem):
    feelings = dataitem["properties"]["felt"]
    if (feelings is None):
        feelings = 0
    return float(feelings)

data["features"].sort(key=getfelt, reverse=True)
for i in range (0,1):
   print("Most felt reports: ", data["features"][i]["properties"]["mag"],",",data["features"][i]["properties"]["place"], ", reports: ",data["features"][i]["properties"]["felt"]) 
#mostfeltquake= max(data["features"], key=getfelt)
#print(f"Most felt reports: {mostfeltquake["properties"]["title"]}, reports {mostfeltquake["properties"]["felt"]}")


# 4: Print the top 10 most significant events, with the significance value of each
def getsig(dataitem):
    signif = dataitem["properties"]["sig"]
    if (signif is None):
        signif = 0
    return float(signif)

data["features"].sort(key=getsig, reverse=True)
print("The 10 most significant events were:")
for i in range (0,10):
   b = i + 1
   print(b,"Event: ", data["features"][i]["properties"]["mag"]," - ",data["features"][i]["properties"]["place"], ", Significance: ",data["features"][i]["properties"]["sig"])
