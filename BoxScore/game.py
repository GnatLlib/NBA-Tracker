class Game:
    # overview contains  "team", "q1", "q2", "q3", "q4", "total"

    t1_overview = {}
    t2_overview = {}

    def __str__(self):
        return str(self.t1_overview["team"]) + " " + str(self.t2_overview["team"])



