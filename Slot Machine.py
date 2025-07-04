import random

MAX_LINES= 3
MAX_BET= 100
MIN_BET= 1

ROWS= 3
COLS= 3

symbol_count= {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8,
}

symbol_value= {
    "A": 2,
    "B": 4,
    "C": 3,
    "D": 2,
}

def check_winnings(colums, lines, bet, values):
    winnings= 0
    winning_lines = []
    for line in range(lines):
        symbol= colums[0][line]
        for column in colums:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet   
            winning_lines.append(line + 1) 
            
    return winnings, winning_lines       
                          

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, count in symbols.items():  # ✅ fixed: use 'symbols', not 'symbol'
        for _ in range(count):
            all_symbols.append(symbol)
    
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    
    return columns
  

def print_slot_machine(columns):
    for row in range(len(columns[0])):  # for each row (e.g., 0 to 2)
        for i, column in enumerate(columns):  # for each column
            if i != len(columns) - 1:
                print(column[row], end=" | ")  # ✅ correct: print item at (row, col)
            else:
                print(column[row], end="")  # no trailing pipe for last column
        print()  # new line after each row
  
        

def deposit():
    while True:
        amount= input("What would you like to deposit? $")
        if amount. isdigit():
            amount= int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater that zero")
        else:
            print("Please enter a number")
    return amount


def get_number_of_lines():
    while True:
        lines= input("Enter the lines to bet on(1-" + str(MAX_LINES) + ")? ")
        if lines. isdigit():
            lines= int(lines)
            if 1<= lines <= MAX_LINES:
                break
            else:
                print("Enter a number")
        else:
            print("Please enter a number")
    return lines

def get_bet():
    while True:
        amount= input("What would you like to bet on each line? ")
        if amount. isdigit():
            amount= int(amount)
            if MIN_BET<= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} and ${MAX_BET}.")
        else:
            print("Please enter a number")
    return amount

def spin(balance):
    lines= get_number_of_lines()
    while True:
        bet= get_bet()
        total_bet= bet * lines
        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is {balance}$")
        else:
            break
    
    print(f"You are betting ${bet} on the {lines} lines. The total bet is equal to  {total_bet}$")
    
    slots= get_slot_machine_spin(ROWS, COLS, symbol_count)  
    print_slot_machine(slots)  
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    if winning_lines:
        print("You won on lines:", ", ".join(str(line) for line in winning_lines))
    else:
        print("No winning lines this spin.")
    return winnings - total_bet

    

def main():
    balance= deposit() 
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play(q to quit).")
        if answer == "q":
            break
        balance += spin(balance)
    
    print(f"You left with ${balance}")                    
main()       