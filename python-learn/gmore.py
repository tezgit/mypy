gnum = 23

# This function uses global variable s


def f():
    global gnum
    gnum += 1
    s = "pippo"
    print(s)
    print(gnum)


# Global scope
s = 1
f()
