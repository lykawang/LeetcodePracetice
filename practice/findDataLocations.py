def findDataLocations(locations, movedFrom, movedTo):
    # Write your code here
    i = 0
    while i < len(movedFrom):
        locations[locations.index(movedFrom[i])] = movedTo[i]
        i += 1
    return sorted(locations)


locations = [1,5,2,6]
movedFrom = [1,4,5,7]
movedTo = [4,7,1,3]
print(findDataLocations(locations,movedFrom,movedTo))