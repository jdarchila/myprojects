#What to Do:
#1.	Ask for:
#o	player_name
#o	hits
#o	at_bats
#2.	Calculate:
 
#batting_avg = hits / at_bats
#3.	Print:
#Aaron Judge: .313 AVG (hits: 42, AB: 134)

while True:
    while True:
        try:
            # Ask for player name, hits, and at bats
            player_name = input("Enter player name: ")
            hits = int(input("Enter number of hits: "))
            at_bats = int(input("Enter number of at bats: "))
            
            # Validate inputs
            if hits < 0 or at_bats <= 0 or hits > at_bats:
                raise ValueError("Hits must be non-negative and at_bats must be positive and greater or equal to hits.")
            
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")

    batting_avg = hits / at_bats
    print(player_name + " batting average is: " + str(round(batting_avg, 3)))

    # Ask if the user wants to continue
    continue_prompt = input("Do you want to enter another player? (yes/no): ").strip().lower()
    if continue_prompt != "yes":
        print("Thanks for using the batting average calculator!")
        break
