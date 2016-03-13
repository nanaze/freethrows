import random
import math

def _GetRandomValue(variance):
  return random.normalvariate(0, math.sqrt(variance))

def _GetRandomPoint(variance):
  return _GetRandomValue(variance), _GetRandomValue(variance);

def _CalculateProbabilityMC(variance, count):
  successful = 0
  attempted = 0

  for i in xrange(count):
    x, y = _GetRandomPoint(variance)
    if abs(x) <= 1 and abs(y) <= 1:
      successful += 1
    attempted += 1

  return successful / float(attempted)

def main():

  low, high = 0, 1
  while True:
    variance = (low + high) / 2.0
    print 'testing' , variance
    prob =  _CalculateProbabilityMC(variance, 1000000)
    print 'probability ', prob
    
    if prob > 0.75:
      low = variance
    else:
      high = variance
    
if __name__ == '__main__':
  main()
