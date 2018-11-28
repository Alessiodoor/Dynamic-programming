class weighted_scheduling:
    activities = []

    def __init__(self, activities):
        self.activities = activities

    def opt(self):
        m = [self.activities[0]["value"]]
        for i in range(1, len(self.activities)):
            if self.p(i) == -1: k = 0
            else: k = m[self.p(i)]
            m.append(max(k + self.activities[i]["value"],
                       m[i-1]))
        return m

    def get_max_index(self, values):
        max = values[-1]
        length = len(values)
        index_max = length - 1
        for i in range(length - 2, 0, -1):
            if values[i] == max: index_max = i
        return index_max

    def optAct(self):
        activities = []
        opt_list = self.opt()
        index_max = self.get_max_index(opt_list)
        while index_max != -1:
            activities.append(self.activities[index_max])
            index_max = self.p(index_max)
        activities = reversed(activities)
        return activities

    def p(self, i):
        pi = -1
        for j in range(i):
            if self.matches(self.activities[j], self.activities[i]):
                pi = j
        return pi

    def print_act(self, act):
        for a in act:
            print("Value: " + str(a["value"]) +
                  ", start: " +  str(a["start"]) +
                  ", end: " + str(a["end"]))
        print()

    def matches(self, a1, a2):
        if(a1["end"] <= a2["start"]): return True
        else: return False