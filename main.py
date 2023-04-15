import pandas as pd
import requests, json

plaintextToMetricDict = {"Total Revenues":"rev_total_current"}
metricToEndpointDict = {"rev_total_current":"finance"}


# https://educationdata.urban.org/api/v1/college-university/ipeds/directory/2021/?unitid=121257&year=2021
# https://educationdata.urban.org/api/v1/schools/ccd/enrollment/2013/grade-3/?charter=1&fips=11


# https://educationdata.urban.org/api/v1/college-university/ipeds/finance/2016/?unitid=121345

def buildUrl(year,schoolID, endpoint, filters=None): #year is number, metric (endpoint) is str, filters is {field:value}
    URL = "https://educationdata.urban.org/api/v1/college-university/ipeds/{}/{}/?unitid={}".format(endpoint,str(year),schoolID)
    if filters:
        for key in filters.keys():
            URL+=("&"+key+"="+filters[key])
    print("Url",URL)
    return URL

def request(URL):
    return requests.get(URL, headers = {'User-agent': 'School Equity Visualizer'})

def processJSON(JSON,metrics):
    JSON = json.loads(JSON)
    print(JSON)
    pass

def processData(reponses,metrics):
    print(reponses)
    for yearDict in reponses.values():
        print(yearDict)
        for reponses in yearDict.values():
            print(reponses.json()["results"][0])


def graph(data):
    pass

def handleUserRequest(metrics, school, startYear,endYear): #metrics is [], school is str, years are numbers
    # schoolID = UnitIdDict[school] #{school: unitid}
    schoolID = "121345"
    reponses = {} # responses[metric][year] = JSON
    endpoints = set()
    for metric in metrics:
        endpoints.add(metricToEndpointDict[plaintextToMetricDict[metric]])
    for year in range(startYear,endYear+1): #non-inclusive?
        reponses[year] = {}
        for endpoint in endpoints:
            reponses[year][endpoint] = request(buildUrl(year,schoolID,endpoint))
    return processData(reponses,metrics)

print(handleUserRequest(["Total Revenues"],"whatever",2015,2016))


