cases = int(raw_input())

for dumby in xrange(cases):
    check = 0  # this will be 1 if type 1, 2 if type 2
    s = raw_input()

    # first we split the string
    X, Y, m, n = "", "", "", ""
    for p in s:
        try:
            t = int(p)
            if Y == "":
                m += p
            else:
                n += p
        except:
            if m == "":
                X += p
            else:
                Y += p
    
    # if Y == "", then it's type 1, otherwise it's type 2
    if Y == "":
        Xn = [ord(c) - 96 for c in X.lower()]
        col = 0
        for i in xrange(len(Xn)):
            col += (26**(i))*Xn[-(i+1)]
        print "R" + m + "C" + str(col)
    else:
        X = ""
        n = int(n)
        while n > 26:
            t = n % 26
            if t == 0:
                t = 26
            X += chr(t + 96).upper()  
            n = (n - t)/26  
        X += chr(n + 96).upper()
        print X[::-1] + m
