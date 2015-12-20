#!/usr/local/bin/python
# Contribution to the forever lasting discussion on indentation!

# After Petrarca, Shakespeare, Milton, Drs. P and many, many others,
# a sonnet has 14 lines and a certain rhyme scheme.

# Jacques Bens presented in 1965 in Paris the pi-sonnet with
# 3,1,4,1 and 5 lines, but the ultimate pi-poem I found in
# Brown's Python Annotated Archives p. 12:

# Based on a algorithm of Lambert Meertens (remember those days of the
# B -> ABC-programming language!!!)


import sys

def main():
    k, a, b, a1, b1 = 2L, 4L, 1L, 12L, 4L
    while 1:
        p, q, k = k*k, 2L*k+1L, k+1L
        a, b, a1, b1 = a1, b1, p*a+q*a1, p*b+q*b1
        d, d1 = a/b, a1/b1
        while d == d1:
            output(d)
            a, a1 = 10L*(a%b), 10L*(a1%b1)
            d, d1 = a/b, a1/b1

def output(d):
    sys.stdout.write(`int(d)`)
    sys.stdout.flush()

main()

# Reading/writing Python source often gives me the impression of
# reading/writing a poem!
# Layout, indentation, rythm, I like the look and feel!

# What does this tiny program do? It is not a sonnet, even not a
# pi-sonnet, but it surely produces Pi!

# The poem ( sorry, the program) needs some explanation.
# As a mathematician I recognize the continued fraction, odd/even,
# squares and all that matters.
# But it is a miracle! A few lines of Python code producing
# a infinity of pi-digits!


# Jaap Spies
# Hogeschool Drenthe

# Keep Peace in Mind