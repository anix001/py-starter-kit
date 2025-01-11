# Match-case (switch): an alternative of using many elif



def day_of_week(day):
    match day:
        case 1:
            return "Sunday"
        case 2:
            return "Monday"
        case _:
            return "Not valid day"