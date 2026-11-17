print("========================================")
print("       CALENDAR VERIFICATION SYSTEM")
print("========================================")

year = int(input("Enter year: "))

if year <= 0:
    print("Error: Please enter a positive year.")
else:
    if year % 400 == 0:
        status = "LEAP YEAR"
        days = 366
        feb_days = 29
        reason = "Century year divisible by 400"

    elif year % 100 == 0:
        status = "COMMON YEAR"
        days = 365
        feb_days = 28
        reason = "Century year not divisible by 400"

    elif year % 4 == 0:
        status = "LEAP YEAR"
        days = 366
        feb_days = 29
        reason = "Divisible by 4 and not a century year"

    else:
        status = "COMMON YEAR"
        days = 365
        feb_days = 28
        reason = "Not divisible by 4"

    print("\n----------------------------------------")
    print(f"Year: {year}")
    print(f"Status: {status}")
    print(f"Days in Year: {days} days")
    print(f"Days in February: {feb_days} days")
    print(f"Reason: {reason}")
    print("----------------------------------------")
