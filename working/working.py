import re
import sys


def main():
    print(convert(input("Hours: ")))

def convert(s):
    valid_hr_range = range(0, 13)
    valid_min_range = range(0, 60)

    matches = re.search(r'^0?(\d{1,2}):?(\d{1,2})?\s((?:AM|PM))\s+to\s0?(\d{1,2}):?(\d{1,2})?\s((?:AM|PM))$', s)

    if not matches:
        raise ValueError

    else:
        groups = len(matches.groups())
        if groups == 6:
            try:
                start_hr = int(matches.group(1))
                start_min = int(matches.group(2)) if matches.group(2) else 0
                start_period = matches.group(3)
                end_hr = int(matches.group(4))
                end_min = int(matches.group(5)) if matches.group(5) else 0
                end_period = matches.group(6)

                if start_hr == end_hr and start_period == end_period:
                    raise ValueError

                if start_hr not in valid_hr_range or end_hr not in valid_hr_range:
                    raise ValueError

                if start_min not in valid_min_range or end_min not in valid_min_range:
                    raise ValueError

                if start_hr == 12 and start_period == 'AM':
                    start_hr = 0

                if end_hr == 12 and end_period == 'AM':
                    end_hr = 0

                start_hr = start_hr + 12 if start_period == 'PM' and start_hr != 12 else start_hr
                end_hr = end_hr + 12 if end_period == 'PM' and end_hr != 12 else end_hr

                return f'{start_hr:02d}:{start_min:02d} to {end_hr:02d}:{end_min:02d}'

            except ValueError:
                sys.exit(ValueError)

        elif groups == 4:
            try:
                start_hr = int(matches.group(1))
                start_period = matches.group(2)
                end_hr = int(matches.group(3))
                end_period = matches.group(4)
                mins = 0

                if start_hr == end_hr and start_period == end_period:
                    raise ValueError

                if start_hr not in valid_hr_range or end_hr not in valid_hr_range:
                    raise ValueError

                if start_hr == 12 and start_period == 'AM':
                    start_hr = 0

                if end_hr == 12 and end_period == 'AM':
                    end_hr = 0

                start_hr = start_hr + 12 if start_period == 'PM' and start_hr != 12 else start_hr
                end_hr = end_hr + 12 if end_period == 'PM' and end_hr != 12 else end_hr

                return f'{start_hr:02d}:{mins:02d} to {end_hr:02d}:{mins:02d}'

            except ValueError:
                sys.exit(ValueError)

if __name__ == "__main__":
    main()
