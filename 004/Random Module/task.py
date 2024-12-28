import random
import mmodule

# #random.randint()
#print(mmodule.pi * random.randint(1, 10))
# #random.random() with module
#print(random.random()*mmodule.pi)
# #random.uniform()
#random_float = random.uniform(1,10)
#print(random_float)

# Heads or Tails
if random.randint(0,1) == 0:
    print("heads")
else:
    print("tails")