import csv

reader = csv.reader(open(r"GameDevMap.csv"), delimiter=',');

citycol = 2
countycol = 4

country = input("Country: ")
city = input("City: ")

filtered = filter(lambda p: p, reader) # does nothing just examples the format
if country: 
    filtered = filter(lambda p: country == p[countycol], reader)
if city: 
    filtered = filter(lambda p: city == p[citycol], reader)

# print to window
itemCount = 0
for row in filtered:
    print(row)
    itemCount += 1

print("There were " + str(itemCount) + " results.")

#Write output to file
outfile = open(r"GameDevMapFiltered.csv",'w', newline="\n")
csv.writer(outfile, delimiter=',').writerows(filtered)