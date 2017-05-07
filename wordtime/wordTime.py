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

    minAdj = -2
    # wish python had switch/case statements
    if minutes >= 60 + minAdj:
        suffix = "o'clock"
        hours += 1
    elif minutes >= 55 + minAdj:
        prefix = "five to"
        hours += 1
    elif minutes >= 50 + minAdj:
        prefix = "ten to"
        hours += 1 # Becouse it's *to* the next hour
    elif minutes >= 45 + minAdj:
        prefix = "quarter to"
        hours += 1
    elif minutes >= 40 + minAdj:
        prefix = "twenty to"
        hours += 1
    elif minutes >= 35 + minAdj:
        prefix = "five past half-past"
    elif minutes >= 30 + minAdj:
        prefix = "half-past"
    elif minutes >= 25 + minAdj:
        prefix = "twenty-five past"
    elif minutes >= 20 + minAdj:
        prefix = "twenty past"
    elif minutes >= 15 + minAdj:
        prefix = "quarter past"
    elif minutes >= 10 + minAdj:
        prefix = "ten past"
    elif minutes >=  5 + minAdj:
        prefix = "five past"
    else:
        suffix = "o'clock" # If it's not more than or equal to 5 (+minAdj = 3) it must be less so it's close to 0 min, so just say "o'clock"

    if hours == 13: # When printing next hour at 12, 12 might become 13 to say it's 'to' the NEXT hour which means we need to fix it to become 1
        hours = 1

    hours = wordHour(hours)

    if suffix == "none":
        words = prefix + " " + hours
    else:
        words = hours + " " + suffix

    if time.strftime("%p") == "PM":
        words += ", in the afternoon."
    else:
        words += ", in the morning."

    return "It's " + words
