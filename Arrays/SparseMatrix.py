
# Three Parallel Lists
SparsMatrix = [[], [], []]
    
# Checking The Entered Length (If it's number or not)
while True:
    try:
        MaxLength = int(input("Please Insert The Matrix Length... "))
        break
    except ValueError:
        print("Please Try Writing a Number...")

# Check Each Input, Store Only NON-ZERO Values.
keepGoing = True
for i in range(MaxLength):
    if not keepGoing:
        break

    for j in range(MaxLength):
        raw = input("Enter The Number (Letter to Exit...) ")

        # Handle non-integer Input (Exit Khodemon)
        try:
            userInput = int(raw)
        except ValueError:
            keepGoing = False
            break

        # Store only NON-ZERO entries
        if userInput != 0:
            SparsMatrix[0].append(i)
            SparsMatrix[1].append(j)
            SparsMatrix[2].append(userInput)

# Printing Out The Saved Numbers Inside Sparse-Matrix
num_entries = len(SparsMatrix[0])   # How Many Non-Zero Entries we Stored

print("i    j    Data")
for k in range(num_entries):
    print(f"{SparsMatrix[0][k]}    {SparsMatrix[1][k]}    {SparsMatrix[2][k]}")
