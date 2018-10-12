import sys
import random

SAMPLE = pow(10,6)

assert len(sys.argv) == 2, "three arguments needed: name of the script, input file"
i = open(str(sys.argv[1]))
o = open("out_"+str(sys.argv[1]),"w")

nb_tests = int(i.readline())


def not_touches_ring(R, t, f, xf, yf):
    # if the distance between the origin and (xf, yf) is more than R-t-f, then it touches the ring
    return (pow(xf, 2)+pow(yf,2)) < pow((R-t-f),2)

def not_touches_string(r, g, f, xf, yf):
    # look at the remainder of xf and yf by g+2r, which is the period of both x and y
    x = abs(xf)%(g+2*r)
    y = abs(yf)%(g+2*r)
    return x>(f+r) and x<(g+2*r-f) and y>(f+r) and y<(g+2*r-f) 

def generate_rand_f(R, t):
    return [(R-t)*random.random(), (R-t)*random.random()]

for test in range(0, nb_tests):
    #0: size of the fly
    #1: outer radius of the racquet
    #2: racquet thickness
    #3: radius of string
    #4: distance between string
    params = [float(x) for x in i.readline().split(" ")]

    pos = 0
    for count in range (0, SAMPLE):
	[xf, yf] = generate_rand_f(params[1], params[2])
	if not_touches_ring(params[1], params[2], params[0], xf, yf) and not_touches_string(params[3], params[4], params[0], xf, yf):
	    pos += 1
	sys.stderr.write('\r {1}/{2} done at {0:%}'.format(float(count)/SAMPLE,test+1,nb_tests))

    

    o.write("Case #{0}: {1}\n".format(test+1, float(pos)/SAMPLE))

i.close()
o.close()
