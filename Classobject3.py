from personality import *
from Student2 import *
p1=Personality('Alice','Aggressive',False)
p2=Personality('Becky','Talkative',True)
s1=Student("Jim","Business",3.1)
s2=Student("imtiaz","CSE",3.4)
p1.owned=s1
s1.info()
s2.info()
p1.sit_down()
p2.stand_up()
p1.stand_up()
p2.sit_down()
p1.owned.info()

