import stdio
import sys

# Return the nth harmonic number.
def harmonic(n):
    total = 0.0
    for i in range(1, n+1):
        total += 1.0 / float(i)
    return total

# Write to standard output the harmonic numbers specified as
# command-line arguments.

for j in range(1, len(sys.argv)):
    arg = int(sys.argv[j])
    value = harmonic(arg)
    stdio.writeln(value)
