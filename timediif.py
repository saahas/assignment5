from datetime import datetime

print("""Enter timestamp in the following format: day dd mon yyyy hh:mm:ss +xxxx \n
        day is weekday as abbreviated name
        dd is the day of the month
        mon is month as abbreviated name
        yyyy is the entire year
        mm is minute
        ss is second
        +xxxx is UTC offset in the form of +hhmm or -hhmm""")

try:
    T1 = datetime.strptime(input("enter timestamp1: "),"%a %d %b %Y %H:%M:%S %z")
    T2 = datetime.strptime(input("enter timestamp2: "),"%a %d %b %Y %H:%M:%S %z")
    print(abs((T2-T1).total_seconds()))

except ValueError:
    print("timestamp has to be in the format described")