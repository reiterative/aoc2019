import math

def fuel_required(mass):
    f = (mass / 3) - 2
    if f < 0:
        f = 0
    return math.floor(f)

cnt = 1
fuel_total = 0
with open('input-day1') as fp:
   line = fp.readline()
   while line:
       print("Line {}: {} ( {} )".format(cnt, line.strip(), fuel_total))
       m = int(line)
       fr = fuel_required(m)
       while fr > 0:
            fuel_total += fr
            fr = fuel_required(fr)

       line = fp.readline()
       cnt += 1

print ("Total fuel required: {}".format(int(fuel_total)))
fp.close()
