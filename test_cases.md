# Test Cases – Simulated Device Monitoring and Alert System

**Tested by:** Bonifacio, Chikiezie Nathan B.  
**Date of testing:** __________________

> Run each test in your Python environment. Fill in Actual Result and Pass/Fail based on what you really observe; do not mark a test as passed until you have run it.

| Test Case | Input or Action | Expected Result | Actual Result | Pass/Fail |
|---|---|---|---|---|
| TC01 | Choose 1 | Five readings: 28, 31, 35, 37, 29 | To be recorded after running | — |
| TC02 | Choose 2, enter 33 | Reading added successfully | To be recorded after running | — |
| TC03 | Choose 2, enter `abc` | Rejected; list unchanged | To be recorded after running | — |
| TC04 | Choose 2, enter `-5` | Rejected; list unchanged | To be recorded after running | — |
| TC05 | Choose 2, enter `120` | Rejected; list unchanged | To be recorded after running | — |
| TC06 | Add 30, then choose 3 | `30 °C -> WARNING` | To be recorded after running | — |
| TC07 | Choose 3 and check 35 | `35 °C -> WARNING` | To be recorded after running | — |
| TC08 | Choose 4 with initial data | Total 160, average 32.00, minimum 28, maximum 37, status ATTENTION REQUIRED | To be recorded after running | — |
| TC09 | Enter menu choice `9` | Error message; menu appears again | To be recorded after running | — |
| TC10 | Choose 5 | Exit message; program ends | To be recorded after running | — |

## Bugs Found and Fixed
During testing, check the classification boundaries carefully. The rules require readings from 30 °C through 35 °C, inclusive, to be classified as WARNING. If a boundary value is classified incorrectly, correct the comparison condition and rerun the relevant tests.
