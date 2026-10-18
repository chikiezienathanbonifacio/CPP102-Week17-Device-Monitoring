# Simulated Device Monitoring and Alert System

**Student Name:** San DiegoRovic  
**Student Number:** __________________  
**Section:** __________________  
**Course:** CPP102 – Programming Logic and Design

## Project Overview
This project is a console-based Python program for monitoring simulated device temperature readings. Each reading is assigned an alert category, and the program can display a summary of all stored readings.

## Temperature Rules
- Below 30 °C: NORMAL
- From 30 °C through 35 °C, inclusive: WARNING
- Above 35 °C: CRITICAL

New readings must be whole numbers between 0 and 100, inclusive.

## Program Features
1. View all readings
2. Add a validated reading
3. Classify each reading
4. Display total, average, minimum, maximum, category counts, and percentages
5. Exit the program

The total, minimum, and maximum are calculated with loops rather than the built-in `sum()`, `min()`, and `max()` functions.

## How to Run
1. Install Python 3.
2. Download this folder from the repository.
3. Open a terminal in this folder.
4. Run `python device_monitor.py` (or `python3 device_monitor.py`).

## Initial Data and Expected Summary
Initial readings: `28, 31, 35, 37, 29`

- Number of readings: 5
- Total: 160
- Average: 32.00 °C
- Minimum: 28 °C
- Maximum: 37 °C
- NORMAL: 2
- WARNING: 2
- CRITICAL: 1
- Overall status: ATTENTION REQUIRED

## Testing
Use `test_cases.md` to run and record the required tests. Record actual results only after executing the program.

## Limitations
Readings are simulated and are not saved after the program exits. The program does not connect to physical sensors.

## Reflection
This project practices Python functions, loops, conditional statements, lists, and input validation. Testing the boundary values is important because both 30 °C and 35 °C must be classified as WARNING. A future improvement could save readings to a file or receive data from a real sensor.
