# Part 1

from math import sin, cos, radians

class Ferry:
    
    def __init__(self):
        self.x = self.y = self.orientation = 0
        
    def command(self, c):
        cmd, arg = c[:1], c[1:]
        arg = int(arg)
        
        if cmd == "N":
            self.y += arg
        elif cmd == "S":
            self.y -= arg
        elif cmd == "E":
            self.x += arg
        elif cmd == "W":
            self.x -= arg
        elif cmd == "R":
            self.orientation -= arg
        elif cmd == "L":
            self.orientation += arg
        elif cmd == "F":
            self.x += int(cos(radians(self.orientation))) * arg
            self.y += int(sin(radians(self.orientation))) * arg
            
    def manhattan(self):
        return abs(self.x) + abs(self.y)


f = Ferry()

for line in open('12/input.txt'):
    f.command(line)

print(f.manhattan())



# Part 2

class WaypointFerry:
        
    def __init__(self):
        self.x = self.y = self.orientation = 0
        self.wpx = 10
        self.wpy = 1
    
    def _rotate_waypoint(self, theta):
        if theta == 90:
            self.wpx, self.wpy = self.wpy, -self.wpx
        elif theta == 270:
            self.wpx, self.wpy = -self.wpy, self.wpx
        elif theta == 180:
            self.wpx, self.wpy = -self.wpx, -self.wpy
    
    def _approach_waypoint(self, r):
        self.x += r * self.wpx
        self.y += r * self.wpy
    
    def command(self, c):
        cmd, arg = c[:1], c[1:]
        arg = int(arg)
        
        if cmd == "N":
            self.wpy += arg
        elif cmd == "S":
            self.wpy -= arg
        elif cmd == "E":
            self.wpx += arg
        elif cmd == "W":
            self.wpx -= arg
        elif cmd == "R":
            self._rotate_waypoint(arg)
        elif cmd == "L":
            self._rotate_waypoint(-arg + 360)
        elif cmd == "F":
            self._approach_waypoint(arg)
            
    def manhattan(self):
        return abs(self.x) + abs(self.y)

w = WaypointFerry()

for line in open('12/input.txt'):
    w.command(line)

print(w.manhattan())