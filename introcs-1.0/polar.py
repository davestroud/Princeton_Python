# -----------------------------------------------------------------------
# polar.py
# -----------------------------------------------------------------------

import stdio
import sys
import math

# Accept floats x and y as command-line arguments. Convert Cartesian
# coordinates (x, y) to polar coordinates (r, theta), and write r and
# theta to standard output.

x = float(sys.argv[1])
y = float(sys.argv[2])

r = math.sqrt(x*x + y*y)
theta = math.atan2(y, x)

stdio.writeln('r        = ' + str(r))
stdio.writeln('theta    = ' + str(theta))

# -----------------------------------------------------------------------

# python polar.py 0.0 0.0
# r     = 0.0
# theta = 0.0

# python polar.py 0.0 1.0
# r     = 1.0
# theta = 1.5707963267948966

# python polar.py 1.0 0.0
# r     = 1.0
# theta = 0.0

# python polar.py 1.0 1.0
# r     = 1.4142135623730951
# theta = 0.7853981633974483

# python polar.py 0.0 -1.0
# r     = 1.0
# theta = -1.5707963267948966

# python polar.py -1.0 0.0
# r     = 1.0
# theta = 3.141592653589793

# python polar.py -1.0 -1.0
# r     = 1.4142135623730951
# theta = -2.356194490192345
