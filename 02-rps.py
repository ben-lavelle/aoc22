from assets.loader import gather_day, input_day
from itertools import starmap

gather_day(2)

with open(input_day(2), 'r') as f:
    rps_strategy = [(l[0], l[2]) for l in f.readlines() if len(l)>1]

eg = ('A', 'Y')

beats = {'A': 'Y', 'B': 'Z', 'C':'X'}
draws = {'A': 'X', 'B': 'Y', 'C':'Z'}
loses = {'A': 'Z', 'B': 'X', 'C':'Y'}

def judge_rps(opp, you)-> int:
    yours = {'X': 1  , 'Y': 2  , 'Z': 3 }
    return (  6 * int(you==beats[opp])
            + 3 * int(you==draws[opp])
            + yours[you])

scores = starmap(judge_rps, rps_strategy)

print(f'For e.g. {eg} you score {judge_rps(*eg)}')
print(f'Overall score: {sum(scores):,}!')

print('Adjusting strategy...')

def set_response(opp, outcome)-> tuple:
    fix_to = {'X': loses, 'Y': draws, 'Z': beats}
    return (opp, fix_to[outcome][opp])

print(f'For e.g. {eg} we transform {set_response(*eg)} '
      f'and get {judge_rps(*set_response(*eg))}.')

updated_scores = starmap(judge_rps, starmap(set_response, rps_strategy))
print(f'New score: {sum(updated_scores):,}!')






