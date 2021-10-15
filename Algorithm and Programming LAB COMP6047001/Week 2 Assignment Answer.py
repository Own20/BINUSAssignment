testcases = [1, 2, 7, 9, 11, 1386, 99, 198, 14, 63, 22]

for i in testcases:
    out = ''
    if(i % 11 == 0):
        out = out+'a'
    if(i % 9 == 0):
        out = out+'b'
    if(i % 7 == 0):
        out = out+'c'
    if(i % 2 == 0):
        out = out+'d'
    if(out == ''):
        out = 'e'
    print(out)