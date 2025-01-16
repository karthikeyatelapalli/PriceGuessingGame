# Price Guessing Game

This Python program is a fun guessing game where players try to guess the price of a randomly generated item. Players compete to guess the exact price or come as close as possible without going over.

---

## **Features**
1. **Random Price Generation**:
   - Generates a random price between $1,000 and $5,000 using Python's `random` module.

2. **Player Input**:
   - Accepts bids from 4 players.
   - Stores the bids for comparison.

3. **Outcome Determination**:
   - Checks if all players overbid and prints a message.
   - Identifies if a player guessed the exact price and awards a bonus.
   - Determines the player closest to the actual price (without exceeding it) if no exact match is found.

4. **Dynamic Feedback**:
   - Provides clear messages for overbidding, exact matches, and the closest guess.

---

## **How to Run**

### **Requirements**
- Python 3.x
- No additional libraries are required.

### **Steps**
1. Save the program as `price_guessing_game.py`.
2. Open a terminal or command prompt.
3. Navigate to the folder containing the program.
4. Run the program:
   ```bash
   python3 price_guessing_game.py
