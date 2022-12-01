from assets.config import USER_SESSION_ID, _GA, _GID
from requests import get
import os

def gather_day(n: int, overwrite: bool=False) -> None:
    assert 1 <= int(n) <= 25, ValueError
    path = f'assets/{n:02}-input.txt'
    if os.path.exists(path) and not overwrite:
        print(f'{path} exists for day {n}. Skipping.')
        return
    response = get(f'https://adventofcode.com/2022/day/{n}/input',
                   cookies={'session': USER_SESSION_ID,
                            '_GA': _GA,
                            '_GID': _GID
                           }
               )
    if response.ok:
        with open(path, 'w') as f:
            f.write(response.text)
        print(f'Day {n} input downloaded to {path}.')
    else:
        print(f'Day {n} request failed.')

def input_day(n: int) -> str:
    assert 1 <= int(n) <= 25, ValueError 
    return f'assets/{n:02}-input.txt'
