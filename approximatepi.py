import random
#Used for graphing
import matplotlib.pyplot as plt

#Program to approximate pi using nothing but two different uniform distributions.

N = 10000
I = 0


outcirclex = []
outcircley = []
incirclex = []
incircley = []

for i in range(N):
    #initialize point balue
    x = random.random()
    y = random.random()
    point = (x,y)
    #Check if the item hits the dartboard or not.
    if((.5-x)**2 + (.5 - y)** 2) < .25:
        I += 1
        incirclex.append(x)
        incircley.append(y)
    else:
        outcirclex.append(x)
        outcircley.append(y)

#Calculate pi.
pi = 4 * I/N
print(pi)
for i in range(len(incirclex)):
    plt.plot(incirclex[i],incircley[i], 'rx')
for i in range(len(outcircley)):
    plt.plot(outcirclex[i],outcircley[i], 'bo')
plt.show()

