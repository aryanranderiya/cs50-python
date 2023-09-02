from datetime import date
import re
import sys
import inflect


def main():
    convert_to_minutes(userinput(input("Date of Birth: ")))


def userinput(input):
    # YYYY-MM-DD formatting

    user_input = input.strip()

    if re.match(r"^\d\d\d\d-\d\d-\d\d$", user_input):
        return user_input
    else:
        sys.exit("Invalid date")


def convert_to_minutes(date_user_input):
    time_duration = date.today() - date.fromisoformat(date_user_input)
    convert_to_words(int(time_duration.total_seconds() / 60))


def convert_to_words(minutes):
    format(inflect.engine().number_to_words(minutes))


def format(word):
    word = word + " minutes"
    capitalized = word[0].upper() + word[1:]
    formatted = re.sub(r"\b\sand\s\b", " ", capitalized)
    print(formatted)


if __name__ == "__main__":
    main()
