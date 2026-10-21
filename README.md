# Payload Encoder & Obfuscation Framework

A Python-based desktop application designed to demonstrate common text encoding, transformation, and obfuscation techniques through a user-friendly graphical interface.

## Features

- **Multiple Encoding Methods:** Base64, ROT13, XOR, hexadecimal, and Unicode.
- **String Transformations:** Random character insertion, character splitting, and string reversal.
- **Detection Testing:** Basic signature-based scanning for predefined suspicious keywords.
- **Method Comparison:** Compare how different transformations affect signature-based detection results.
- **Graphical User Interface:** A dark-themed Tkinter interface with input, output, and detection panels.
- **Copy Results:** Easily copy generated output for testing and analysis.

## Technologies Used

- Python 3
- Tkinter and ttk
- Base64
- String manipulation
- Randomization

## Purpose

This project is intended for cybersecurity education, Python development practice, and authorized laboratory testing. It demonstrates how encoding and simple obfuscation affect text patterns and why basic signature-based detection has limitations.

**Note:** Encoding is not encryption, and a negative result from the built-in signature checker does not mean that a payload is safe or undetectable by professional security tools.

## Getting Started

1. Install Python 3.
2. Save the project source code as `gui.py`.
3. Run the application:

   ```bash
   python gui.py
   ```

4. Enter sample text or load the demo.
5. Select an encoding method or run the detection test.
6. Review and compare the results.

## Disclaimer

This tool is intended for educational purposes and authorized security testing only. Use it responsibly and only in environments where you have permission to conduct testing.
