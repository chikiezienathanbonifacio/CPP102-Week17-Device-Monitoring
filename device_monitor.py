def get_initial_readings():
    """Return the starting list of simulated device temperatures."""
    return [28, 31, 35, 37, 29]


def is_whole_number(text):
    """Return True if text contains an optional leading minus sign and digits."""
    if len(text) == 0:
        return False
    start = 0
    if text[0] == "-":
        start = 1
    if start == len(text):
        return False
    for index in range(start, len(text)):
        if text[index] not in "0123456789":
            return False
    return True


def display_menu():
    """Display the main menu options."""
    print("\nSIMULATED DEVICE MONITORING SYSTEM")
    print("----------------------------------")
    print("[1] View Readings")
    print("[2] Add Reading")
    print("[3] Classify Readings")
    print("[4] Generate Summary")
    print("[5] Exit")


def display_readings(readings):
    """Display every stored temperature reading with its position."""
    print("\nCURRENT READINGS")
    print("----------------")
    for index in range(len(readings)):
        print(f"Reading {index + 1}: {readings[index]} °C")


def add_reading(readings, lowest=0, highest=100):
    """Validate one user entry and append it only when it is valid."""
    text = input("Enter new reading: ")
    if len(text) == 0:
        print("Invalid input. The reading cannot be empty.")
    elif not is_whole_number(text):
        print("Invalid input. Enter a whole number only.")
    else:
        reading = int(text)
        if reading < lowest or reading > highest:
            print(f"Invalid reading. Enter a value from {lowest} to {highest}.")
        else:
            readings.append(reading)
            print("Reading added successfully.")


def classify_reading(reading, warning_limit=30, critical_limit=35):
    """Return NORMAL, WARNING, or CRITICAL for one temperature."""
    if reading < warning_limit:
        return "NORMAL"
    elif reading <= critical_limit:
        return "WARNING"
    else:
        return "CRITICAL"


def display_classifications(readings):
    """Display the classification of every stored reading."""
    print("\nREADING CLASSIFICATION")
    print("----------------------")
    for reading in readings:
        print(f"{reading} °C -> {classify_reading(reading)}")


def compute_total(readings):
    """Return the total of all readings using a loop."""
    total = 0
    for reading in readings:
        total = total + reading
    return total


def compute_average(readings):
    """Return the average of the readings."""
    return compute_total(readings) / len(readings)


def find_minimum(readings):
    """Return the smallest reading using a loop."""
    minimum = readings[0]
    for reading in readings:
        if reading < minimum:
            minimum = reading
    return minimum


def find_maximum(readings):
    """Return the largest reading using a loop."""
    maximum = readings[0]
    for reading in readings:
        if reading > maximum:
            maximum = reading
    return maximum


def count_category(readings, category):
    """Count readings that match the requested classification."""
    count = 0
    for reading in readings:
        if classify_reading(reading) == category:
            count = count + 1
    return count


def determine_overall_status(warning_count, critical_count):
    """Return the overall monitoring status based on category counts."""
    if critical_count >= 1:
        return "ATTENTION REQUIRED"
    elif warning_count >= 1:
        return "MONITOR"
    else:
        return "NORMAL"


def display_summary(readings):
    """Calculate and display the numerical and classification summary."""
    number = len(readings)
    total = compute_total(readings)
    average = total / number
    minimum = find_minimum(readings)
    maximum = find_maximum(readings)

    normal_count = count_category(readings, "NORMAL")
    warning_count = count_category(readings, "WARNING")
    critical_count = count_category(readings, "CRITICAL")

    print("\nMONITORING SUMMARY")
    print("------------------")
    print(f"Number of readings : {number}")
    print(f"Total of readings : {total}")
    print(f"Average temperature : {average:.2f} °C")
    print(f"Minimum temperature : {minimum} °C")
    print(f"Maximum temperature : {maximum} °C")
    print()
    print(f"NORMAL : {normal_count} ({normal_count / number * 100:.2f}%)")
    print(f"WARNING : {warning_count} ({warning_count / number * 100:.2f}%)")
    print(f"CRITICAL : {critical_count} ({critical_count / number * 100:.2f}%)")
    print()
    print("Overall Status:", determine_overall_status(warning_count, critical_count))


def main():
    """Run the menu until the user chooses Exit."""
    readings = get_initial_readings()
    while True:
        display_menu()
        choice = input("Enter choice: ")
        if choice == "1":
            display_readings(readings)
        elif choice == "2":
            add_reading(readings)
        elif choice == "3":
            display_classifications(readings)
        elif choice == "4":
            display_summary(readings)
        elif choice == "5":
            print("Thank you for using the Device Monitoring System.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
