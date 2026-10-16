# Lab 5: Static Code Analysis

## Objective

The aim of this lab was to check the quality, security, and formatting of the given Python program using Pylint, Bandit, and Flake8.

## Project Description

The Dairy Milk Collection Ledger is a Python program that records milk deliveries, calculates daily milk collection, identifies the top farmer, finds low-fat milk entries, and prints collection slip messages.

## Issues Fixed

- Replaced dynamically formatted SQL with parameterized queries to avoid SQL injection risks.
- Replaced MD5 hashing with SHA-256 for generating farmer tokens.
- Removed `os.system()` and used Python's `print()` instead.
- Added docstrings to explain the module and functions.
- Changed function names to Python's `snake_case` convention.
- Removed unused imports.
- Fixed long lines and other formatting issues.
- Corrected the comparison with `None`.
- Improved variable names and database connection handling.

## Tools Used

- **Pylint:** Checked code quality and naming conventions.
- **Bandit:** Checked for common security issues.
- **Flake8:** Checked Python formatting and style.

## Final Results

| Tool | Result |
|---|---|
| Pylint | 10.00/10 |
| Bandit | No issues identified |
| Flake8 | No formatting issues reported |

## Files in This Folder

- `dairy_collection.py` — Updated Python program.
- `issues.md` — Issues identified and the fixes applied.
- `pylint_report_before.txt` and `pylint_report_after.txt` — Pylint reports.
- `bandit_report_before.txt` and `bandit_report_after.txt` — Bandit reports.
- `flake8_report_before.txt` and `flake8_report_after.txt` — Flake8 reports.
- `.gitignore` — Excludes the virtual environment and Python cache files.

## Verification

After fixing the issues, all three static analysis tools were run again. The final reports were checked to confirm that the security and formatting issues were resolved and that the Pylint score was above 9.5.
