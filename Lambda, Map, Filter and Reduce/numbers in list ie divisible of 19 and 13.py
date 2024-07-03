originallist=[19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
l=list(filter(lambda d :(d%19==0 or d%13==0),originallist))
print(l)