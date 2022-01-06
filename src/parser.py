class Parser:

    def __init__(self):
        self.heading = 0

    def parse(self, sequence, angle):
        # parse the sequence by converting the sequence of Ls and Rs to a sequence of heading angles for the turtle head
        calculated = []

        def truncate_angle(angle):
            # prevent the angle from being > 360 or < 0
            while angle > 360:
                angle -= 360
            while angle < 0:
                angle += 360
            return angle

        for move in sequence:
            if move == "L":
                self.heading -= angle
            elif move == "R":
                self.heading += angle

            calculated.append(truncate_angle(self.heading))

        return calculated