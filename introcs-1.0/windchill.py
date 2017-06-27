# -----------------------------------------------------------------------
# windchill.py
# -----------------------------------------------------------------------

import stdio
import sys

""" Accept as command-line arguments a temperature t (in Fahrenheit)
 and a wind speed v (in miles per hour). Compute the wind chill
 using the formula from the National Weather Service.
 Write w to standard output.

 Reference:  http://www.nws.noaa.gov/om/windchill/index.shtml """

t = float(sys.argv[1])
v = float(sys.argv[2])

w = 35.74 + 0.6215*t + (0.4275*t - 35.75) * (v ** 0.16)

stdio.writeln('Temperature = ' + str(t))
stdio.writeln('Wind speed  = ' + str(v))
stdio.writeln('Wind chill  = ' + str(w))

# -----------------------------------------------------------------------

# python windchill.py 32 10
# Temperature = 32.0
# Wind speed  = 10.0
# Wind chill  = 23.72714425963738
