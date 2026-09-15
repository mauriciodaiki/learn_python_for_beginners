# 🐍 Learn Python for Beginners — Boot.dev

Welcome to my repository for the **Learn Python for Beginners** course, the first step in the [Boot.dev Backend Developer Path](https://www.boot.dev). This repository serves as a record of my progression, code solutions, unit testing setups, and notes as I build core backend programming foundations in Python.

---

## 📌 About the Course

The course covers essential Python programming concepts required for building real-world backend systems:

- [x] **Ch 1.** Introduction
- [x] **Ch 2.** Variables
- [x] **Ch 3.** Functions
- [x] **Ch 4.** Scope
- [x] **Ch 5.** Testing & Debugging
- [x] **Ch 6.** Computing
- [x] **Ch 7.** Comparisons
- [x] **Ch 8.** Loops
- [x] **Ch 9.** Lists
- [x] **Ch 10.** Dictionaries
- [x] **Ch 11.** Sets
- [x] **Ch 12.** Errors
- [ ] **Ch 13.** Type Hints
- [ ] **Ch 14.** Practice
- [ ] **Ch 15.** Quiz

---

## ⚙️ Local Development & Testing Setup

To mirror the automated testing environment used by Boot.dev on my local machine:

- **Unit Testing:** Exercises feature paired `main.py` (solution) and `main_test.py` (unit runner) files.
- **Running Tests Locally:** Tests are run from the terminal using relative execution paths:
  ```bash
  python3 main_test.py

---

## Requirements

- Python 3
- VS Code
- VS Code Python extension

## Setup

Clone the repository:

    git clone <repository-url>
    cd learn_python_for_beginners

Create the virtual environment:

    python3 -m venv .venv

Install dependencies:

    .venv/bin/python -m pip install -r requirements.txt

## Running tests

The repository provides two VS Code tasks:

- `Boot.dev: Run` — runs the regular tests.
- `Boot.dev: Submit` — runs all tests, including tests marked `submit`.

They can also be selected from:

    Terminal → Run Task...

### Recommended VS Code shortcuts

    Ctrl+Enter        → Boot.dev: Run
    Ctrl+Shift+Enter  → Boot.dev: Submit

These shortcuts must be configured in the user's VS Code
`keybindings.json`.

## Pytest markers

Tests marked with:

    @pytest.mark.submit

are excluded from `Boot.dev: Run` and included in
`Boot.dev: Submit`.