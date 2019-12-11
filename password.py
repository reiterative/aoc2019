minval = 137683
maxval = 596253

def test_ascend(number):
    s = str(number)
    for i in range(1, len(s)):
        if int(s[i]) < int(s[i-1]):
            return False
        # /if
    # /for
    return True
# /def

def test_repeat(number):
    s = str(number)
    dup = 0
    match = False
    for i in range(1, len(s)):
        if int(s[i]) == int(s[i-1]):
            if dup == 0:
                match = True
                dup = int(s[i])
            elif dup == int(s[i]):
                match = False
            else:
                return True
                # /if
            # /if
        # /if
    # /for
    return match
# /def

password = []
for x in range(minval, maxval):
    if test_ascend(x) and test_repeat(x):
        print "Password = {}".format(str(x))
        password.append(x)
    # /if
# /for

print "{} password candidates found".format(len(password))
