import random
#przyblizone pi
def estimate_pi(n):
     
     numberOfPointsInCircle = 0
     numberOfPointsInTotal = 0
     for i in range(n):
          x = random.uniform(0,1)
          y = random.uniform(0,1)
          distance = x**2 + y**2
          if distance <= 1:
               numberOfPointsInCircle += 1

          numberOfPointsInTotal += 1

     return 4*numberOfPointsInCircle/numberOfPointsInTotal
