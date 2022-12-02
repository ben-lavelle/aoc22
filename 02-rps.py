from assets.loader import gather_day, input_day
from itertools import starmap

gather_day(2)

with open(input_day(2), 'r') as f:
    rps_strategy = [(l[0], l[2]) for l in f.readlines() if len(l)>1]

print(rps_strategy[3])

def judge_rps(opp, you)-> int:
    beats = {'A': 'Y', 'B': 'Z', 'C':'X'}
    draws = {'A': 'X', 'B': 'Y', 'C':'Z'}
    yours = {'X': 1  , 'Y': 2  , 'Z': 3 }
    if you==beats[opp]:
        return 6 + yours[you]
    elif you==draws[opp]:
        return 3 + yours[you]
    else:
        return 0 + yours[you]

scores = starmap(judge_rps, rps_strategy)

print(f'For e.g. {rps_strategy[3]} you score {judge_rps(*rps_strategy[3])}')
print(f'Overall score: {sum(scores):,}!')





