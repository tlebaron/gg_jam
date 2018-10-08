import sys
assert len(sys.argv) == 2, "three arguments needed: name of the script, input file"



num_tests = 0
queries = []
engines = []

i = open(str(sys.argv[1]))
o = open("out_"+str(sys.argv[1]),"w")
num_tests = int(i.readline())

for tests in range (0, num_tests):
    nb_switch = 0

    nb_engines = int(i.readline())
    engines_list = []
    for engine in range(0, nb_engines):
	engines_list.append(i.readline())
    #engines.append(engines_list)

    nb_queries = int(i.readline())
    queries_list = []
    for query in range(0, nb_queries):
	queries_list.append(i.readline())
    #queries.append(queries_list)


    available_engines = engines_list[:]
    for query in queries_list:
	if query in available_engines:
	    available_engines.remove(query)
	if len(available_engines) == 0:
	    nb_switch += 1
	    available_engines = engines_list[:]
    
    o.write("Case #{0}: {1}\n".format(tests+1, nb_switch))

i.close()
o.close()
