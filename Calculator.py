import calendar

print("📅 MY PYTHON CALENDAR")

year = int(input("Enter year: "))
month = int(input("Enter month (1-12): "))

print()
print(calendar.month(year, month))

Example

📅 MY PYTHON CALENDAR

Enter year: 2026
Enter month (1-12): 9

   September 2026
Mo Tu We Th Fr Sa Su
   1  2  3  4  5  6
7  8  9 10 11 12 13
14 15 16 17 18 19 20
21 22 23 24 25 26 27
28 29 30

Run it with:

python calendar.py

This uses Python's built-in "calendar" module, so no installation is needed.
