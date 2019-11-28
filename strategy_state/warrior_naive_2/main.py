from characters import Knight,Archer
c1=Knight()
c2=Archer()
c3=Archer()


print('c1: ID',c1.id)
print ('c2: ID', c2.id)
print ('c3: ID', c3.id)

print('c1',c1.energy)
print ('c2', c2.energy)
print()

print ('c1 and c2 find a threasure')
c1.gain(5)
c2.gain(5)

print('c1',c1.energy) #73
print('c2',c2.energy) #66
print()


print ('c1 and c2 were hit!')
c1.loss(10)
c2.loss(10)

print('c1',c1.energy) #67
print('c2',c2.energy) #55

