import sys
import random
import math

SAMPLE = pow(10,6)

assert len(sys.argv) == 2, "three arguments needed: name of the script, input file"
i = open(str(sys.argv[1]))
o = open("out_"+str(sys.argv[1]),"w")

nb_tests = int(i.readline())



def touches_ring(R, t, f, xf, yf):
    # if the distance between the origin and (xf, yf) is more than R-t-f, then it touches the ring
    return (pow(xf, 2)+pow(yf,2)) > pow((R-t-f),2)

def touches_string(r, g, f, xf, yf):
    # look at the remainder of xf and yf by g+2r, which is the period of both x and y
    x = abs(xf)%(g+2*r)
    y = abs(yf)%(g+2*r)
    return x<(f+r) or x>(g+2*r-f) or y<(f+r) or y>(g+2*r-f) 

def per_av_racq(R, t, f):
    return (math.pi*(R-t-f)*(R-t-f))/(math.pi*R*R)

def per_av_string(t,r,g,R,f, test, nb_tests):
    inner_r = R-t-f
    inner_cycle = math.pi*pow(inner_r, 2)

    # cut the innercycle quarter in 10^6 * 10^6 cases, check the bottom left corner of the case if on a string
    touch = 0
    count = 0
    for i in range(0, SAMPLE): #row
	for j in range(0, SAMPLE): #column
	    sys.stderr.write("\r{1}/{2} : {0}%".format(100*float(i*SAMPLE+j)/pow(SAMPLE,2), test+1, nb_tests))
	    y = inner_r*float(i+0.5)/SAMPLE
	    x = inner_r*float(j+0.5)/SAMPLE
	    # in out of the inner_cycle, jump to next row
	    if (pow(x,2)+pow(y,2))>pow(inner_r,2):
		break
	    count += 1
	    if touches_string(r, g, f, x, y):
		touch += 1

    

    return math.pi*inner_r*inner_r*(1-float(touch)/count)

def generate_rand_f(R):
    [x,y] = [R,R]
    while (pow(x,2)+pow(y,2))>pow(R,2):
	[x,y] = [(R)*random.random(), (R)*random.random()]
    return [x,y]

def touches_racq(x, y, params):
    R = params[1]
    t = params[2]
    f = params[0]
    return x>(R-t-f) or y>(R-t-f)

def touches_string(x, y, params):
    f = params[0]
    r = params[3]
    g = params[4]
    r_x = x%(g+2*r)
    r_y = y%(g+2*r)
    return r_x<(r+f) or r_x>(g+2*r-f) or r_y<(r+f) or r_y>(g+2*r-f)

def does_touch(x,y,params):
    return touches_string(x, y, params) or touches_racq(x, y, params)

for test in range(0, nb_tests):

#f, R, t, r, g
    params = [float(x) for x in i.readline().split(" ")]

    touches = 0
    for counter in range(0, SAMPLE):
        sys.stderr.write("\r{0}/{1} done at {2}%".format(test+1, nb_tests, 100*float(counter)/SAMPLE))
	[x,y] = generate_rand_f(params[1])
	if does_touch(x, y, params):
	    touches += 1
    perc_touch = float(touches)/SAMPLE

    o.write("Case #{0}: {1}\n".format(test+1, perc_touch))

i.close()
o.close()

