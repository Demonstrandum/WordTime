import time

def wordHour(n):
    return {
         1: "one",
         2: "two",
         3: "three",
         4: "four",
         5: "five",
         6: "six",
         7: "seven",
         8: "eight",
         9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
    }.get(n, str(n))

def fuzzyTime():
    hours = int(time.strftime("%I"))
    minutes = int(time.strftime("%M"))

    prefix = "none"
    suffix = "none"

    # wish python had switch/case statements
    if minutes >= 55:
        suffix = "o'clock"
    elif minutes >= 50:
        prefix = "ten to"
        hours += 1 # Becouse it's *to* the next hour
    elif minutes >= 45 and minutes > 40:
        prefix = "quarter to"
        hours += 1
    elif minutes >= 30 and minutes > 25:
        prefix = "half-past"
    elif minutes >= 20 and minutes > 15:
        prefix = "twenty past"
    elif minutes >= 15 and minutes > 10:
        prefix = "quarter past"
    elif minutes >= 10 and minutes >  5:
        prefix = "ten past"
    elif minutes >= 5 and minutes > 3:
        prefix = "five to"
        hours += 1
    else:
        suffix = "o'clock" #...?


    hours = wordHour(hours)

    if suffix == "none":
        words = prefix + " " + str(hours)
    else:
        words = str(hours) + " " + suffix

    if time.strftime("%p") == "PM":
        words += ", in the afternoon."
    else:
        words += ", in the morning."

    return "It's " + words
