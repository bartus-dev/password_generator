# Password Generator

A command-line Python tool that generates secure, random passwords with user-configurable character types.

## Description

This project generates a random password of a user-specified length, drawing from a customizable pool of characters. Users choose which character categories to include — lowercase letters, uppercase letters, digits, and symbols — before the password is generated. Randomness is provided by Python's `secrets` module, which is designed for cryptographic use cases like password and token generation, rather than the general-purpose (and predictable) `random` module.

## Features

- 🔐 **Cryptographically Secure Randomness** — Uses Python's `secrets` module instead of `random`, making generated passwords resistant to prediction
- ⚙️ **Configurable Character Categories** — Choose any combination of lowercase letters, uppercase letters, digits, and symbols
- ✅ **Input Validation** — Rejects non-numeric password lengths and lengths of zero or less, with clear error messages
- 🚫 **Minimum Selection Enforcement** — If no character category is selected, the user is prompted to choose again instead of generating an empty or broken password
- 🔁 **Reusable Yes/No Prompt** — A single helper function (`ask_yes_no`) handles all category prompts, avoiding repeated validation logic

## Technologies

- [Python 3.x](https://www.python.org/) — no external dependencies required
- Built-in Python modules:
  - `secrets` — cryptographically secure random character selection

## Installation and Setup Guide

Follow these steps to run the Password Generator on your own machine.

### 1. Clone or Download the Project

```bash
git clone https://github.com/bartus-dev/password_generator.git
cd your-repo-name
```

### 2. Verify Python Installation

Make sure Python 3 is installed on your system:

```bash
python --version
```

If it's not installed, download it from [python.org](https://www.python.org/downloads/).

### 3. Run the Application

No additional libraries are required. Simply run the script:

```bash
python generator.py
```

### 4. Follow the Prompts

You'll be asked whether to include each character category, then how long your password should be:

```
Lowercase letters? (y/n): y
Added:  lowercase letters
Uppercase letters? (y/n): y
Added:  uppercase letters
Digits? (y/n): n
Skipped:  digits
Symbols? (y/n): n
Skipped:  symbols
Choose length of your password: 12

Your password: XkPjqrLmZaBv
```

## Usage Notes

- You must select at least one character category — if you decline all four, you'll be asked to choose again.
- Password length must be a positive whole number.
- The final character pool is built from whichever categories you select, so a password using only "digits" will contain digits exclusively (and similarly for other single-category choices).

## Possible Future Improvements

- Add a simple password strength rating (e.g. Weak/Medium/Strong) based on length and variety
- Allow generating multiple passwords in one run without restarting the script
- Add command-line arguments (`argparse`) as an alternative to interactive prompts
- Exclude ambiguous characters (e.g. `0`/`O`, `1`/`l`) as an optional setting
- Add unit tests for password length and character pool composition

## License

This project is open-source and available for personal or educational use. Feel free to modify and expand it.