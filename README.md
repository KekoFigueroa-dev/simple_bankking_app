# Keko's Python Banking App 🏦

A simple command-line banking simulator originally built for  
**“The Art of Doing Python Projects”**, then enhanced with better input
validation and clearer messages.

The app lets a single user:
- Create an account with **Savings** and **Checking** balances.
- Make **deposits** and **withdrawals** on either account.
- Avoid overdrafts with basic balance checks.
- View updated account information after each transaction.

## How It Works

Main flow:
1. `get_info()` – collect name and initial deposits, build an account dict: {"Name": ..., "Savings": ..., "Checking": ...}

Loop while the user wants to continue:
   - `display_info(account)` – show current balances.
   - `make_transaction(account)` – choose account (Savings/Checking),
     choose action (Deposit/Withdrawal), and process it.
   - `continue_banking()` – ask if another transaction should be made.
3. At the end, show final account info and print a goodbye message.

Key helpers:
- `get_valid_float(prompt)` – safely reads a non-negative number from input.
- `make_deposit(account, account_type, amount)` – increases Savings or Checking.
- `make_withdrawal(account, account_type, amount)` – decreases balance only if
  it won’t go negative.

## Requirements

- Python 3.x  
- No external dependencies (standard library only).

## Run
(Replace `banking_app.py` with your actual filename.)

---

**Author:** Keko Figueroa