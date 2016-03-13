import randval
import math

def _CalculateProbabilityMC(variance, count):
  successful = 0
  attempted = 0

  variance_sqrt = math.sqrt(variance)
  
  for i in xrange(count):
    x, y = (
      randval.GetRandomValueSqrtVariance(variance_sqrt),
      randval.GetRandomValueSqrtVariance(variance_sqrt))
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
