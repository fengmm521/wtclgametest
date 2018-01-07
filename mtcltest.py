#-*- coding: utf-8 -*-

import os
import random


# print random.random()

# print random.uniform(1, 10)
#欧式和法式轮盘,1~37,有37个数
onumbers = {1:[0,'g'],2:[26,'b'],3:[3,'r'],4:[35,'b'],5:[12,'r'],6:[28,'b'],7:[7,'r'],8:[29,'b'],9:[18,'r'],10:[22,'b'],11:[9,'r'],12:[31,'b'],13:[14,'r'],14:[20,'b'],15:[1,'r'],16:[33,'b'],17:[16,'r'],18:[24,'b'],19:[5,'r'],20:[10,'b'],21:[23,'r'],22:[8,'b'],23:[30,'r'],24:[11,'b'],25:[36,'r'],26:[13,'b'],27:[27,'r'],28:[6,'b'],29:[34,'r'],30:[17,'b'],31:[25,'r'],32:[2,'b'],33:[21,'r'],34:[4,'b'],35:[19,'r'],36:[15,'b'],37:[32,'r']}


playertimes = 1000

startscore = 30000


scroe = startscore

gamecolor = 'b'

startlist = [1,2,3]

limit = 300

onethrow = 5

rcount = 0
bcount = 0

wincount = 0
losscount = 0

limittmpc = 0

list1 = 0

greecount = 0

for i in range(playertimes):

    scoretmp = scroe

    while len(startlist) > 1:

        if scroe > (startlist[0] + startlist[-1]) * onethrow and (startlist[0] + startlist[-1]) <= limit:

            tmp = random.randint(1, 37)
            value = onumbers[tmp][0]
            color = onumbers[tmp][1]

            throwcount = startlist[0] + startlist[-1]

            if color == 'b':
                bcount += 1
            elif color == 'r':
                rcount += 1

            if color == gamecolor:
                startlist.remove(startlist[-1])
                startlist.remove(startlist[0])
                scroe += (throwcount * onethrow)

                print '1',startlist
            elif color == 'g':
                scroe -= (throwcount * onethrow)
                startlist.append(throwcount)

                greecount += 1
                print 'g',startlist
            else:
                scroe -= (throwcount * onethrow)
                startlist.append(throwcount)

                print '2',startlist
        else:
            if scroe < (startlist[0] + startlist[-1]) * onethrow:
                print 'scroe is too smale..........'
            if (startlist[0] + startlist[-1]) > limit:
                print 'is limit 300................'
                limittmpc += 1
                print startlist
                startlist = []
            break
        if len(startlist) == 1:
            print '+++++',startlist
            list1 += 1

        if len(startlist) <= 1:
            print '-----',startlist

        if scoretmp > scroe:
            break

    if scoretmp < scroe:
        wincount += 1
    elif scoretmp > scroe:
        losscount += 1
        print 'lossscore',scoretmp - scroe

    if len(startlist) <= 1:
        startlist = [1,2,3]
        tmpx = random.randint(0, 1)
        print 's',startlist
        
p = float(losscount)/float(wincount)

print 'wincount=        ',wincount
print 'losscount=       ',losscount
print 'loss/win=        ',p
print '(loss/win)*37=   ',p*37
print '1.0/37=          ',1.0/37.0
print 'limitcount=      ',limittmpc
print 'list1=           ',list1
print 'greecount=       ',greecount

print scroe,scroe - startscore




# nlist = range(0,37)

# for k in onumbers.keys():
#     if onumbers[k][0] in nlist:
#         nlist.remove(onumbers[k][0])
#     else:
#         print 'erro,',k

# print nlist



# #美式轮盘
# mnumbers = {1:[0,'g'],2:[28,'b'],3:[9,'r'],4:[26,'b'],5:[30,'r'],6:[11,'b'],7:[7,'r'],8:[20,'b'],9:[32,'r'],10:[17,'b'],11:[5,'r'],12:[22,'b'],13:[34,'r'],14:[15,'b'],15:[3,'r'],16:[24,'b'],17:[36,'r'],18:[13,'b'],19:[1,'r'],20:[-1,'g'],21:[27,'r'],22:[10,'b'],23:[25,'r'],24:[29,'b'],25:[12,'r'],26:[8,'b'],27:[19,'r'],28:[31,'b'],29:[18,'r'],30:[6,'b'],31:[21,'r'],32:[33,'b'],33:[16,'r'],34:[4,'b'],35:[23,'r'],36:[35,'b'],37:[14,'r'],38:[2,'b']}

# nlist = range(-1,37)

# for k in mnumbers.keys():
#     if mnumbers[k][0] in nlist:
#         nlist.remove(mnumbers[k][0])
#     else:
#         print 'erro,',k

# print nlist

