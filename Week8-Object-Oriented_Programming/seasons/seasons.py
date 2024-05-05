from datetime import date
import inflect
import sys

def main():
    try:
        text = input("Date of birth: ").strip()
        minutes = convert(text)
        if minutes == ValueError:
            sys.exit("InvalidDate")
        print(f"{minutes} minutes")
    except ValueError:
        sys.exit("InvalidDate")

def convert(x):
    try:
        born = date.fromisoformat(x)
        p = inflect.engine()
        days = date.today() - born
        minutes = int(days.total_seconds() / 60)
        minutes_words = p.number_to_words(minutes)
        return (minutes_words.replace(" and "," ")).capitalize()
    except ValueError:
        return ValueError


if __name__ == "__main__":
    main()
