from characters import Warrior
c1=Warrior()
c2=Warrior()

print('c1',c1.energy)
print ('c2', c2.energy)
print()

print ('c1 find a threasure')
c1.gain(5)
print('c1',c1.energy)
print()

print ('c1 find a threasure')
c1.gain(5)
print('c1',c1.energy)


print ('c1 has been hit!')
c1.loss(10)
print('c1',c1.energy)


print ('c2 has been hit!')
c2.loss(10)
print('c2',c2.energy)

