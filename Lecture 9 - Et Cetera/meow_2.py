import argparse
import sys

# Example 1
'''
if len(sys.argv) == 1:
    print("meow")

elif len(sys.argv) == 3 and sys.argv[1] == "-n":
    n = int(sys.argv[2])
    for _ in range(n):
        print("meow")

else:
    print("Usage: meows.py")
'''

# Example 2, using arparse
parser = argparse.ArgumentParser(description="Meow like a cat")
parser.add_argument("-n", default=1, help="Number of times to meow", type=int)
args = parser.parse_args()

for _ in range(int(args.n)):
    print("meow")