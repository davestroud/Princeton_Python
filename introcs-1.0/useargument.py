import stdio
import sys

# Accept a name as a command-line argument.  Write a message containing
# that name to a standard output.

stdio.write('Hi, ')
stdio.write(sys.argv[1])
stdio.writeln('. How are you?')
