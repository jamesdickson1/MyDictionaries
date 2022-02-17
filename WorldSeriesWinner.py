def main():

    infile = open("WorldSeriesWinners.txt","r")
    infile1 = open("WorldSeriesWinners.txt","r")

    numwins = {}
    yearwins = {}

    
    for line in infile:
        line = line.strip()
        if line in numwins:
            numwins[line] = numwins[line] + 1
        else:
            numwins[line] = 1


    yr = 1902

    for line in infile1:
        line = line.strip()
        if yr == 1903:
            yr += 2
            yearwins[yr] = line
        elif yr == 1993:
            yr += 2
            yearwins[yr] = line
        else:
            yr += 1
            yearwins[yr] = line

    
    input_year = int(input("Which year?"))

    yr = input_year
    result = yearwins[yr]
    wins = numwins[result]

    print("The team that won in " + str(yr) + " was " + result + ". They have " + str(wins) + " total wins.")


main()
    