"""
0, 1, 2, 3, 4, 5, 6, 7, 8, 9
10, 11, 12, 13, 14, 15, ..., 19
20, 21, ..., 29
30
40
...
90
100, 101, 102

00:00:00
00:00:01
00:00:09
00:00:10
00:00:19
00:00:20
00:00:59
00:01:00

base 5
digits: 0, 1, 2, 3, 4
0, 1, 2, 3, 4
10, 11, 12, 13, 14
20
30
40, 41, 42, 43, 44
100

base 2
digits: 0, 1
0, 1
10, 11
100, 101, 110, 111
1000, 1001

base 16
digits: 0, ..., 10, a, b, c, d, e, f
0, ..., f
10, 1f
20, 2f
30, 3f
...
ff
100

base 5
*1
 43
 24
 __+
122

in every base,
10 * 10 = 100
100 * 100 = 10000

10 is the base
10000 - 10^4

10 in base 16 is base 16 in base 10
base 16
10 * 10 = 100
in base 10, it'll be
16 * 16 = 256

if I have 1000 in base 8
in base 10, the value would be 8^3

1001 in base 8
it would be 1000 + 1
8^3 + 8^0*1

2000
2*1000
2*8^3

in base 2
10101
10000 + 100 + 1
2^4 + 2^2 + 1

other way around
from base 10 -> base k

to base 8
8?
10

16?
20

64?
100

64?
8*2
10*2 in base 8

512 is 8*3 in base 10
which means
it's 10*3 in base 8

different digits is just the base by the power of the placement.
124 - 10^2 + 2*10^1 + 4*10^0

1234 convert to base 5 from base 10
1000 + 200 + 30 + 4
1*10^3 + 2*10^2 + 3*10^1 + 4*10^0
1*5^3 + 2*5^2 + 3*5^1 + 4*5^0
125 + 50 + 15 + 4
194

2345890 convert to base 10 from base 8
8^7 = 2097152
remainder = 248738
8^6*0
remainder = 248738
8^5*7 = 229376
remainder = 19362
8^4*4 = 16384
remainder = 2978
8^3*5 = 2560
remainder = 418
8^2*6 = 384
remainder = 34
8^1*4 = 32
remainder = 2
8^0*2 = 2
remainder = 0

10745642

1024 = 8^3*2 + 8^2*0 + 8^1*0 + 8^0*0 + 0
in base 8 = 2000

23001
10^4*2
10^3*3
10^2*0
10^1*0
10^0*1
"""
def from10(k, n):           #k is the base, n is the number to convert
    li = []
    digit = 0
    while k ** digit <= n:
        digit += 1
    digit -= 1              #i is now the digit
    
    while digit >= 0:
        val = 1
        while val * (k ** digit) <= n:
            val += 1
        val -= 1
        li.append(val)
        n = n - (val * (k ** digit))
        digit -= 1
    return li

print (from10(8, 2345890))