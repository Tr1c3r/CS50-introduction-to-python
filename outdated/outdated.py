Months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date_input = input("Date: ")

    if '/' in date_input:
        try:
            # Date format like "month/day/year"
            month, day, year = map(int, date_input.split('/'))
            if 1 <= month <= 12 and 0 < day <= 31:
                formatted_date = f"{year:04d}-{month:02d}-{day:02d}"
                print(formatted_date)
                break
            else:
                pass
        except ValueError:
            pass
    elif ',' in date_input:
        try:
            # Date format like "month day, year"
            date_parts = date_input.split(' ')
            month_name = str.title(date_parts[0])
            day = int(date_parts[1][:-1])
            year = int(date_parts[2])
            if month_name in Months and 1 <= day <= 31:
                m = Months.index(month_name) + 1  # Month index starts from 1
                formatted_date2 = f"{year:04d}-{m:02d}-{day:02d}"
                print(formatted_date2)
                break
            else:
                pass
        except ValueError:
            pass
    else:
        # Invalid input, you may want to add a message or break the loop
        pass
