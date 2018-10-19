import sys
assert len(sys.argv) == 2, "three arguments needed: name of the script, input file"
i = open(str(sys.argv[1]))
o = open("out_"+str(sys.argv[1]),"w")

nb_tests = int(i.readline())

for test in range(0, nb_tests):

    size = i.readline()
    x_list = i.readline().split(" ")
    y_list = i.readline().split(" ")

    x_list.sort()
    y_list.sort(reverse = True)

    product = 0
    for x, y in zip(x_list, y_list):
	product += int(x)*int(y)


    o.write("Case #{0}: {1}\n".format(test+1, product))

i.close()
o.close()
