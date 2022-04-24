from business.calendar import Calendar

Calendar.load_paths = ['./']
calendar = Calendar.load("2022")

print(calendar.is_business_day("2022-03-05"))
