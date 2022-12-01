from assets.loader import gather_day, input_day
from requests import get

gather_day(1)

with open(input_day(1), 'r') as f:
    calorie_log = [l for l in f.readlines()]

lead_elf = 0
this_elf = 0
silver_elf, bronze_elf = 0, 0
for c in calorie_log:
    try:
        this_elf += int(c)
        if this_elf > lead_elf:
            lead_elf, silver_elf, bronze_elf = this_elf, lead_elf, silver_elf
        elif this_elf > silver_elf:
            lead_elf, silver_elf, bronze_elf = lead_elf, this_elf, silver_elf
        elif this_elf > bronze_elf:
            lead_elf, silver_elf, bronze_elf = lead_elf, silver_elf, this_elf
    except ValueError:
        this_elf = 0
	
print(f'Top elf: {lead_elf:,} Calories')
print(f'Top three: {lead_elf+silver_elf+bronze_elf:,} Calories')



