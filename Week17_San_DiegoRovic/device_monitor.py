"""Simulated Device Monitoring and Alert System.
CPP102 - Laboratory Experience 17
Student: San DiegoRovic
"""

def initial_readings():
    """Create the required starting temperature readings."""
    return [28, 31, 35, 37, 29]


def valid_integer(value):
    """Check whether the entered text represents a whole number."""
    if not value:
        return False
    position = 1 if value[0] == "-" else 0
    if position == len(value):
        return False
    for character in value[position:]:
        if character not in "0123456789":
            return False
    return True


def classify_temperature(value):
    """Classify a temperature according to the lab rules."""
    if value < 30:
        return "NORMAL"
    if value <= 35:
        return "WARNING"
    return "CRITICAL"


def show_readings(readings):
    """Print the current readings."""
    print("\n--- Current Device Readings ---")
    if not readings:
        print("There are no readings yet.")
        return
    for number, value in enumerate(readings, start=1):
        print(f"{number}. {value} °C")


def add_temperature(readings):
    """Validate and append a temperature from 0 through 100."""
    entered = input("Enter temperature (0-100): ").strip()
    if not valid_integer(entered):
        print("Invalid entry: please enter a whole number.")
        return
    value = int(entered)
    if value < 0 or value > 100:
        print("Out of range: temperature must be from 0 to 100.")
        return
    readings.append(value)
    print("Temperature added.")


def show_classifications(readings):
    """Print the alert category for each reading."""
    print("\n--- Temperature Classifications ---")
    for value in readings:
        print(f"{value} °C: {classify_temperature(value)}")


def calculate_total(readings):
    """Calculate the total with a loop, not sum()."""
    total = 0
    for value in readings:
        total += value
    return total


def calculate_minimum(readings):
    """Find the minimum with a loop, not min()."""
    smallest = readings[0]
    for value in readings:
        if value < smallest:
            smallest = value
    return smallest


def calculate_maximum(readings):
    """Find the maximum with a loop, not max()."""
    largest = readings[0]
    for value in readings:
        if value > largest:
            largest = value
    return largest


def count_status(readings, status):
    """Count readings belonging to one category."""
    amount = 0
    for value in readings:
        if classify_temperature(value) == status:
            amount += 1
    return amount


def show_summary(readings):
    """Print numerical statistics and alert-category counts."""
    if not readings:
        print("No readings available for the summary.")
        return

    total = calculate_total(readings)
    low = calculate_minimum(readings)
    high = calculate_maximum(readings)
    average = total / len(readings)

    normal = count_status(readings, "NORMAL")
    warning = count_status(readings, "WARNING")
    critical = count_status(readings, "CRITICAL")

    print("\n--- Device Monitoring Summary ---")
    print(f"Number of readings: {len(readings)}")
    print(f"Total: {total}")
    print(f"Average: {average:.2f} °C")
    print(f"Minimum: {low} °C")
    print(f"Maximum: {high} °C")
    for label, count in (("NORMAL", normal), ("WARNING", warning), ("CRITICAL", critical)):
        percent = count / len(readings) * 100
        print(f"{label}: {count} ({percent:.2f}%)")

    if critical:
        overall = "ATTENTION REQUIRED"
    elif warning:
        overall = "MONITOR"
    else:
        overall = "NORMAL"
    print("Overall status:", overall)


def main():
    """Run the interactive monitoring menu."""
    readings = initial_readings()
    while True:
        print("\n=== SIMULATED DEVICE MONITOR ===")
        print("1. View readings")
        print("2. Add a reading")
        print("3. Classify readings")
        print("4. Generate summary")
        print("5. Exit")
        choice = input("Select 1-5: ").strip()

        if choice == "1":
            show_readings(readings)
        elif choice == "2":
            add_temperature(readings)
        elif choice == "3":
            show_classifications(readings)
        elif choice == "4":
            show_summary(readings)
        elif choice == "5":
            print("Monitoring session ended.")
            break
        else:
            print("Invalid menu selection. Choose a number from 1 to 5.")


if __name__ == "__main__":
    main()
