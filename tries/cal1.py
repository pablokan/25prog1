import calendar
import locale

# Configurar la localización a español de España
#locale.setlocale(locale.LC_ALL, 'es_ES.UTF-8')


# Print the calendar for a specific month
print(calendar.month(2025, 10))

# Print the calendar for an entire year
print(calendar.calendar(2026))

# Check if a year is a leap year
is_leap = calendar.isleap(2024)
print(f"Is 2024 a leap year? {is_leap}")

# Get the day of the week for a specific date
weekday = calendar.weekday(2025, 9, 23)
print(f"September 23, 2025 was a day number: {weekday} (0=Monday, 6=Sunday)")