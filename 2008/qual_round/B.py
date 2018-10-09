import sys
assert len(sys.argv) == 2, "three arguments needed: name of the script, input file"
i = open(str(sys.argv[1]))
o = open("out_"+str(sys.argv[1]),"w")

nb_tests = int(i.readline())

for test in range(0, nb_tests):
    startA = 0
    startB = 0
    #trips[0] are from A to B, [1] form B to A.
    #each is a list of [departure hour, dep min, arrival hour, arr min]
    trips = [[],[]]
    turn_time = int(i.readline())
    [nb_trips_AB, nb_trips_BA] = [int(element) for element in i.readline().split(" ")]
    
    for index, trips_number in enumerate([nb_trips_AB, nb_trips_BA]):
	for trips_list_onway in range(0,trips_number):
	    [departure, arrival] = i.readline().split(" ")
	    trips[index].append([int(departure.split(":")[0]), int(departure.split(":")[1]), int(arrival.split(":")[0]), int(arrival.split(":")[1])])
    
    print test, turn_time, [nb_trips_AB, nb_trips_BA], trips

    o.write("Case #{0}: {1}\n".format(test+1, -1))

i.close()
o.close()
