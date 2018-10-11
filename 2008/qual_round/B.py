import sys
assert len(sys.argv) == 2, "three arguments needed: name of the script, input file"
i = open(str(sys.argv[1]))
o = open("out_"+str(sys.argv[1]),"w")

nb_tests = int(i.readline())

def use_train(i, available, added):
    assert i == 1 or i == 0
    if available[i] == 0:
	print "train added at {0}".format(i)
	added[i] += 1
    else:
	available[i] -= 1

def print_time(t):
    print "{0}:{1}".format(t/60, t%60)

for test in range(0, nb_tests):
    nb_train_add = [0,0]
    nb_train_av = [0,0]
    #0: departure from A, 1: departure from B, 2: arrival to B, 3: arrival to A
    trips = [[],[],[],[]]
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

	    trips[index].append(trip[0])
	    trips[index+2].append(trip[1])

	    time.append(trip[0])
	    time.append(trip[1])

    time.sort()
    print trips

    for t in time:
	print_time(t)
	if t in trips[3]:
	    print "train arrive in A"
	    trips[3].remove(t)
	    nb_train_av[0] += 1
	    continue
	if t in trips[2]:
	    print "train arrive in B"
	    trips[2].remove(t)
	    nb_train_av[1] += 1
	    continue
	if t in trips[0]:
	    print "train start from A"
	    trips[0].remove(t)
	    use_train(0, nb_train_av, nb_train_add)
	    continue
	if t in trips[1]:
	    print "train start from B"
	    trips[1].remove(t)
	    use_train(1, nb_train_av, nb_train_add)
	    continue
	assert False

    o.write("Case #{0}: {1} {2}\n".format(test+1, nb_train_add[0], nb_train_add[1]))

i.close()
o.close()
