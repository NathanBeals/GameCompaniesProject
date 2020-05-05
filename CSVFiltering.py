import csv

# constants
citycol = 2
countrycol = 4

def countryFilter(passedList):
    countryList = csv.reader(open(r"Countries.csv"), delimiter=',');
    for country in countryList:
        if country[0] == passedList[countrycol]:
            return True

    return False

def main():
    reader = csv.reader(open(r"GameDevMap.csv"), delimiter=',');
    #countryList = csv.reader(open(r"Countries.csv"), delimiter=',');

# "United States" == p[countrycol]
    # for country in countryList:
    #     filtered = filter(lambda p: p, reader)
    filtered = filter(lambda p: 
       countryFilter(p), 
    reader)
        #result += filtered

    # print to window
    itemCount = 0
    for row in filtered:
        print(row)
        itemCount += 1

    print("There were " + str(itemCount) + " results.")

    #Write output to file
    outfile = open(r"GameDevMapFiltered.csv",'w', newline="\n")
    csv.writer(outfile, delimiter=',').writerows(filtered)

if __name__=="__main__":
    main()