import math
import random

def GetRandomValue(variance):
  return GetRandomValueSqrtVariance(math.sqrt(variance))

def GetRandomValueSqrtVariance(variance_sqrt):
  return random.normalvariate(0, variance_sqrt)
