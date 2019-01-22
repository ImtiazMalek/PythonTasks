class Personality:
    def __init__(self,name,personality,is_sitting):
        self.name=name
        self.personality=personality
        self.is_sitting=is_sitting
    def sit_down(self):
        self.is_sitting=True
        print('This is %s'%self.name+',\nShe is sitting.')
    def stand_up(self):
        self.is_sitting=False
        print('This is %s' % self.name + ',\nShe is standing.')