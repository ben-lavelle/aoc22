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
    return (  6 * int(you==beats[opp])
            + 3 * int(you==draws[opp])
            + yours[you])

scores = starmap(judge_rps, rps_strategy)

print(f'For e.g. {rps_strategy[3]} you score {judge_rps(*rps_strategy[3])}')
print(f'Overall score: {sum(scores):,}!')





