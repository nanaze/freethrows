import randval
import math
import sys

def _CalculateGrannyMC(variance):
  successful = 0
  attempted = 0

  while True:
    x = randval.GetRandomValue(variance)
    if abs(x) <= 1:
      successful += 1
    attempted += 1

    print 'success rate', successful / float(attempted)

def main():
  assert len(sys.argv) >= 2, 'variance must be given as first arg'
  
  arg = sys.argv[1]
  _CalculateGrannyMC(float(arg))

    
if __name__ == '__main__':
  main()
