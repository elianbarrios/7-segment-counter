# 7-Segment Counter

A simple counter (0-9) implemented in MicroPython for Raspberry Pi Pico (or any board compatible with the `machine` module), displaying digits on a common-cathode 7-segment display.

## Components

- Raspberry Pi Pico (or other MicroPython board)
- Common-cathode 7-segment display
- 7 current-limiting resistors (optional, depending on the display)

## Wiring

The display is connected to the following GPIO pins:

| Pico Pin | Segment |
|----------|---------|
| 18       | a       |
| 19       | b       |
| 13       | c       |
| 15       | d       |
| 14       | e       |
| 16       | f       |
| 17       | g       |

The common cathode of the display connects to GND.

## How it works

1. **Pin setup**: the 7 GPIO pins are configured as outputs (`Pin.OUT`).
2. **Digit encoding**: each digit 0-9 is represented as a hexadecimal value where each bit maps to a segment (a-g). For example, `0x3F` turns on segments a, b, c, d, e, and f to form the digit `0`.
3. **`show(number)` function**: takes a digit, gets its hexadecimal code, and turns each segment on or off according to its corresponding bit.
4. **Main loop**: displays digits 0 through 9, waiting 1 second between each, in an infinite loop.

## Usage

1. Copy `main.py` to the board (e.g., with Thonny or `ampy`).
2. On boot or when running the script, the display will start counting from 0 to 9.

## Customization

- To change the counting speed, modify the `time.sleep(1)` value in the main loop.
- To extend the counter to two or more digits, additional multiplexing and pins would be required.
- The `numbershx` tuple can be extended to show letters or other characters (segments a-g).
