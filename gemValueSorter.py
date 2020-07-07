import csv

# read from csv file
# make groups of values >= 40
# max gem quality is 20
# when making groups use a variable to keep track of the difference between the current group's sum and 40
# add to groups by trying to match closest number to the difference
# whatever doesn't get sorted into a group is grouped in a final array and totaled to show how much until it hits 40
# output as txt file named valueGroups.txt

gemValueArr = []
#populate array to hold copies of all default gem values
for i in range(20):
    gemValueArr.append([])
    
gemGroups = []
gems = False

filename = 'gemValues.csv'
rows = []

#passing data from the csv file to rows for sorting
with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)

    for row in csvreader:
        rows.append(row)
    
    csvfile.close()

#sorting numbers from rows into gemValueArr for use
for row in rows:
    num = int(row[0])
    index = num - 1
    gemValueArr[index].append(num)

#check to see if there are any values in gemValueArr
def gemCheck(gemValueArr):
    groupCount = 0

    for group in gemValueArr:
        if group != []:
            groupCount += 1

    if groupCount > 0:
        return True
    else:
        return False

gems = gemCheck(gemValueArr)

toGroup = []

#figure out how to get difference seperated from inside of the loop or try a nested loop if that fails
while gems == True:
    difference = 40
    first = 19
    group = []
    hitZero = False

    #loop to create arrays to be appended to final array of groups
    while difference > 0:
        tempFirst = 0
        
        if first == (difference - 2):
            if gemValueArr[first + 1] != []:
                first += 1

        if hitZero == True:
            tempFirst = abs(first)

            if gemValueArr[tempFirst] != []:
                hold = gemValueArr[tempFirst].pop()
                difference -= hold
                group.append(hold)
        else:
            if gemValueArr[first] != []:
                hold = gemValueArr[first].pop()
                difference -= hold
                group.append(hold)
        
        #keeps the loop from locking down and decrements first so that lower numbers can be accessed
        first -= 1
        if first > difference:
            first = difference - 1
        if first < 0:
            hitZero = True

        gemsRemain = gemCheck(gemValueArr)
        
        if gemsRemain == False:
            difference = 0

    print(group)

    toGroup.append(group)
    print(toGroup)

    temp = 0
    for item in group:
        temp += item
    if temp < 40 or temp >40:
        print(temp)

    gems = gemCheck(gemValueArr)

with open("gemGroups.txt", "w+") as filehandle:
    for group in toGroup:
        filehandle.write("%s\n" % group)

    filehandle.close()
