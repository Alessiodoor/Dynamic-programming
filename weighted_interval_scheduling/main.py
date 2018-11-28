import sys
import random
from Weighted_interval_scheduling import weighted_scheduling

def createAc(n):
    activities = [{"start": 1, "end": 3, "value": 10}]
    for i in range(1, int(n)):
        start = random.randint(0, 200)
        activities.append({"start": start,
                            "end": (random.randint(activities[i-1]["end"],
                                                   activities[i-1]["end"] + 5) + start),
                           "value": random.randint(1, 30)})
    return activities

if len(sys.argv) > 1:
    activities = createAc(sys.argv[1])
    algo = weighted_scheduling(activities)
    algo.print_act(activities)
    print("Best combination")
    algo.print_act(algo.optAct())
else: print("Insert number of activities.")