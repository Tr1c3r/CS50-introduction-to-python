from datetime import date, datetime
import sys
import re
import inflect

class Spell:
    @staticmethod
    def spell(self):
        p = inflect.engine()
        self_spelled = p.number_to_words(self, andword="").capitalize()
        return self_spelled

class Birthday:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
        self.today = date.today()

    @classmethod
    def get_birthday(cls):
        birthday = input("What's your birthday? (YYYY-MM-DD): ")
        if matches := re.search(r"^(\d{4})-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])$", birthday):
            return date.fromisoformat(birthday)
        else:
            sys.exit('Not a valid format')

    def minutes_lived(self):
        current_date = self.today
        birthday_date = date(self.year, self.month, self.day)
        difference = current_date - birthday_date
        total_minutes = difference.days * 24 * 60
        return Spell().spell(total_minutes)


def main():
    user_birthday = Birthday.get_birthday()
    user_lifetime = Birthday(user_birthday.year, user_birthday.month, user_birthday.day).minutes_lived()
    print(f'{user_lifetime} minutes')

if __name__ == "__main__":
    main()
