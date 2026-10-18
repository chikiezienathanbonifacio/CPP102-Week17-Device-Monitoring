# Simulated Device Monitoring and Alert System

**Student Name:** Bonifacio, Chikiezie Nathan B.  
**Student Number:** 2601327  
**Section:** 1CpE-B  
**Course:** CPP102 – Programming Logic and Design

## Project Description
This Python program monitors simulated device-temperature readings. It classifies each reading as NORMAL, WARNING, or CRITICAL and generates a summary of the readings. It also allows the user to add valid readings while rejecting invalid input.

## Features
- View all stored temperature readings
- Add whole-number readings from 0 to 100
- Classify readings using the required temperature rules
- Calculate total, average, minimum, and maximum
- Count each category and calculate its percentage
- Determine the overall monitoring status
- Reject empty, non-numeric, out-of-range, and invalid menu input

## Requirements
- Python 3
- No external packages are required

## How to Run
1. Download or clone this repository.
2. Open a terminal in the repository folder.
3. Run: `python device_monitor.py`
4. On some systems, use: `python3 device_monitor.py`

## Sample Output
The initial readings are `28, 31, 35, 37, 29`.

```text
MONITORING SUMMARY
------------------
Number of readings : 5
Total of readings : 160
Average temperature : 32.00 °C
Minimum temperature : 28 °C
Maximum temperature : 37 °C

NORMAL : 2 (40.00%)
WARNING : 2 (40.00%)
CRITICAL : 1 (20.00%)

Overall Status: ATTENTION REQUIRED
```

## Test Cases
The planned test cases are listed in `test_cases.md`. Run each test in your Python environment and update the Actual Result and Pass/Fail columns to match what you observe.

## Known Limitations
- Readings are stored only while the program is running.
- The program uses simulated readings and does not connect to real sensors or devices.

## Reflection
This project combines lists, loops, selection statements, functions, and input validation in one program. One important part was making sure the boundary values 30 °C and 35 °C are both classified as WARNING. I also learned to calculate the summary using loops instead of the built-in `sum()`, `min()`, and `max()` functions. In the future, I could improve the program by saving readings between sessions or connecting it to a real sensor.
