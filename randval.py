import math
import random

def GetRandomValue(variance):
  return random.normalvariate(0, math.sqrt(variance))
