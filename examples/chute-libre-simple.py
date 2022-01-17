# Chronophotography

# from https://eduscol.education.fr/1648/programmes-et-ressources-en-physique-chimie-voie-gt

# The purpose of this activity is to use a
# chronophotography of a falling marble.

# Numerical ability implemented:
# represent the successive positions of a system
# modeled by a point during an evolution
# one-dimensional or two-dimensional evolution using
# a programming language.

import numpy as np
import matplotlib.pyplot as plt

# On a chronophotograph (printed photo or
# video opened in a pointing software),
# the successive positions of the ball have been pointed out
# and recorded the successive positions in the table
# below.

ymes = np.array([-0, -0.7, -1.5, -2.3, -3.5, -4.5, -5.9, -7.7, -8.8,
                 -10.6, -12.3, -14.2, -16.4, -18.5, -21, -23.5])
                 
# Here, the experiment lasts 0.25 s and corresponds to
# 16 measurement points: it is thus necessary to generate 16
# instants between 0 and 0.25 s (duration of the experiment).
# A time base, i.e. a table of
# values, can be constructed automatically, using
# automatically, using the function `np.linspace`.
# The three arguments used are the start,
# the end, the number of steps.

t = np.linspace(0, 0.25, 16)

# The real ordinate is finally calculated from
# the ordinate measured on the chronophotograph.
# The scale of the photo being 2/100, numpy allows
# to multiply directly all the values of the table
# ymes by the scale and automate the conversion.
# The new values are collected in the
# table yreelle. The functions used afterwards
# are used to "personalize" the graph: labels
# for the x-axis and y-axis, grid, legend
# and title.

yreelle = ymes * 2/100

plt.figure()

plt.plot(t, yreelle, 'ro', label="y=f(t)")
plt.xlabel("time")
plt.ylabel("yreelle")
plt.grid()
plt.legend()
plt.title("free fall")

plt.show()