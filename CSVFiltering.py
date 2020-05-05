import csv

# Filters
bCities = False
bCountries = True

# Constants
citycol = 2
countrycol = 4

def countryFilter(passedList):
    if not bCountries:
        return True

    countryList = csv.reader(open(r"Countries.csv"), delimiter=',');
    for country in countryList:
        if country[0] == passedList[countrycol]:
            return True

    return False

# TODO: refactor to remove duplication
def citiesFilter(passedList):
    if not bCities:
        return True

    cityList = csv.reader(open(r"Cities.csv"), delimiter=',');
    for city in cityList:
        if city[0] == passedList[citycol]:
            return True

    return False

def main():
    reader = csv.reader(open(r"GameDevMap.csv"), delimiter=',');
    filtered = filter(lambda p: countryFilter(p) and citiesFilter(p),  reader)

    # print to window
    itemCount = 0
    for row in filtered:
        print(row)
        itemCount += 1
    print("There were " + str(itemCount) + " results.")

    #Write output to file
    reader = csv.reader(open(r"GameDevMap.csv"), delimiter=',');
    filtered = filter(lambda p: countryFilter(p) and citiesFilter(p),  reader)
    csv.writer(open(r"GameDevMapFiltered.csv",'w', newline="\n"), delimiter=',').writerows(filtered)

if __name__=="__main__":
    main()