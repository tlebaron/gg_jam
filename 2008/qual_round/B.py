import sys
assert len(sys.argv) == 2, "three arguments needed: name of the script, input file"
i = open(str(sys.argv[1]))
o = open("out_"+str(sys.argv[1]),"w")

nb_tests = int(i.readline())

for test in range(0, nb_tests):
    startA = 0
    startB = 0
    #trips[0] are from A to B, [1] form B to A, [2] all
    #each is a list of [departure hour, dep min, arrival hour, arr min]
    trips = [[],[],[]]
    #instead of testing all minutes, just record interesting time
    time = []
    turn_time = int(i.readline())
    [nb_trips_AB, nb_trips_BA] = [int(element) for element in i.readline().split(" ")]

    for index, trips_number in enumerate([nb_trips_AB, nb_trips_BA]):
	for trips_list_onway in range(0,trips_number):
	    [departure, arrival] = i.readline().split(" ")
	    trip = [int(departure.split(":")[0])*60+int(departure.split(":")[1]), int(arrival.split(":")[0])*60+int(arrival.split(":")[1])]

	    # just add turn time to record ready time instead of arrival time, useless
	    trip[1] = trip[1] + turn_time

	    trips[index].append(trip)
	    trips[2].append(trip)

	    if trip[0] not in time:
		time.append(trip[0])
	    if trip[1] not in time:
		time.append(trip[1])

    trips[2].sort()
    time.sort()

    d_A = False
    d_B = False
    a_A = False
    a_B = False

    for t in time:

	#start with arrivals
	for Atrips in trips[1]:
	    if t == ### looks weird, sure there is a better method...

    

    for trip in trips[2]:
	if trip in trips[0]:
	    departure = "A"
	else:
	    departure = "B"
	

    print test, turn_time, [nb_trips_AB, nb_trips_BA], trips[2], time

    o.write("Case #{0}: {1}\n".format(test+1, -1))

i.close()
o.close()
