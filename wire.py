
class Plotter:
    def __init__(self, instructions):
        self.instructions = instructions
        self.coordinates = []
        self.count = 0
        self.x = 0
        self.y = 0
        for i in instructions:
            direction = i[0:1]
            distance = int(i[1:])
            if direction == 'D':
                self.move_vertical(distance, -1)
            elif direction == 'U':
                self.move_vertical(distance, 1)
            elif direction == 'L':
                self.move_horizontal(distance, -1)
            elif direction == 'R':
                self.move_horizontal(distance, 1)
            else:
                print "Unrecognised direction: {}".format(direction)
            # /if
        # /for
    # /def

    def move_vertical(self, distance, step):
        for d in range(distance):
            self.y = self.y + step
            self.count = self.count + 1
            self.coordinates.append((self.x,self.y, self.count))
    # /def

    def move_horizontal(self, distance, step):
        for d in range(distance):
            self.x = self.x + step
            self.count = self.count + 1
            self.coordinates.append((self.x,self.y, self.count))
        # /for
    # /def
# /class

# main method
with open('input-day3') as fp:
    line = fp.readline()
    routes = []
    while line:
        source = line.split(',')
        p = Plotter(source)
        routes.append(p)
        line = fp.readline()
    # /while

    print "{} routes plotted".format(len(routes))
    crossing = []
    print "First route has {} coordinates".format(len(routes[0].coordinates))
    print "Second route has {} coordinates".format(len(routes[1].coordinates))
    for x1, y1, count1 in routes[0].coordinates:
        for x2, y2, count2 in routes[1].coordinates:
            if x1 == x2 and y1 == y2:
                total = int(count1) + int(count2)
                crossing.append((x1,y1, total))
    print "Crossing points found: {}".format(len(crossing))
    lowest = 999999
    lowest_x = 0
    lowest_y = 0
    for x, y, total in crossing:
        if lowest > total:
            lowest = total
            lowest_x = x
            lowest_y = y
    print "Closest crossing point: x={} y={} ({})".format(lowest_x, lowest_y, lowest)
    fp.close()
    print ""
# /with
