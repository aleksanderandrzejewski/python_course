import numpy as np

#metoda 1

aList = [[ i+2*j for i in range (10)] for j in range(5)]
table = np.array( aList, dtype=float )

table2=np.zeros((3,3))

table3=np.ones_like(table2)

print "Zawartosci"
print table
print table2
print table3

print "wielkosci"
print len(table)
print table.shape[0], table.shape[1]

print "fragmenty"
print (aList[2])
print (aList[2])[4]

table = np.zeros(10)
print 'wycinki'
print table
table[:]=2
print table
table[3:]=7
print table
table[3:7:2]=8 #od 3 do 7 co 2
print table
table[[1,3,9]]=-1
print table
print table-5

print 'tablice boolowskie, maska'
mask = table>0
print mask
table[mask]=100
print table






