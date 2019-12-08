
class Plotter:
    def __init__(self, instructions):
        self.instructions = instructions
        self.coordinates = []
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
            self.coordinates.append((self.x,self.y))
    # /def

    def move_horizontal(self, distance, step):
        for d in range(distance):
            self.x = self.x + step
            self.coordinates.append((self.x,self.y))
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
    for x1, y1 in routes[0].coordinates:
        for x2, y2 in routes[1].coordinates:
            if x1 == x2 and y1 == y2:
                crossing.append((x1,y1))
    print "Crossing points found:"
    for x, y in crossing:
        print "{},{}".format(x, y)
    fp.close()
# /with
