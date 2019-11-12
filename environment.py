#Hanoi tower environment
import argparse
class Environment:

    def __init__(self, n_disks = 3, n_pegs = 3,objective = 2):
        self.pegs = []
        self.n_disks = n_disks
        self.objective = objective
        for i in range(n_pegs):
            self.pegs.append([-1])
        for i in range(n_disks,0,-1):
            self.pegs[0].append(i)
        

    def move_disk(self,start,end):
        if start < 0 or start >= len(self.pegs):
            print("Illegal index, start is out of range")
        elif end < 0 or end >= len(self.pegs):
            print("Illegal index, end is out of range")
        elif self.pegs[start][-1] == -1:
            print("Illegal move! This peg doens't have disk")
        elif self.pegs[end][-1] != -1 and  self.pegs[start][-1] > self.pegs[end][-1]:
            print("Illegal move! Your size of disk is larger than size of top disk from target peg")
        else:
            d = self.pegs[start].pop()
            self.pegs[end].append(d)

    def reach_goal(self):
        if len(self.pegs[self.objective]) != self.n_disks+1:
            return False
        for i in range(1,self.n_disks+1):
            if self.pegs[self.objective][i] != (self.n_disks-i+1):
                return False
        return True

parser = argparse.ArgumentParser()
parser.add_argument('--mode', type=int , default=0 )

opt = parser.parse_args()
print(opt)

tower = Environment()
if opt.mode == 0:
    print(tower.pegs)
    tower.move_disk(-1,2)
    tower.move_disk(0,-2)
    tower.move_disk(0,2)
    tower.move_disk(0,2)
    tower.move_disk(0,1)
    print(tower.reach_goal())
    tower.move_disk(2,1)
    tower.move_disk(0,2)
    tower.move_disk(0,2)
    tower.move_disk(1,0)
    tower.move_disk(1,2)
    tower.move_disk(0,2)
    tower.move_disk(0,2)
    print(tower.reach_goal())
    print(tower.pegs)
else:
    while(True):
        print(tower.pegs)
        a, b = map(int, input("Please input source peg and destination peg (Ex: 0,2): ").split(','))
        tower.move_disk(a,b)
        if tower.reach_goal() == True:
            print(tower.pegs)
            print("Congratulation!!")
            break
