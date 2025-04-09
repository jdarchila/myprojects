#Goal: Use input(), int(), str, if/else, string formatting**
#What to Do:
#1.	Ask for:
#o	home_team, away_team
#o	home_score, away_score
#2.	Print a formatted game result.
#3.	If scores are equal → “Extra innings!”
#Else print who won.
while True:
  while True:
      try:
          # Ask for home team, away team, home score, and away score
          home_team = input("Enter home team: ")
          away_team = input("Enter away team: ")
          home_score = int(input("Enter home score: "))
          away_score = int(input("Enter away score: "))
          
          # Validate inputs
          if home_score < 0 or away_score < 0:
              raise ValueError("Scores must be non-negative.")
          
          break
      except ValueError as e:
          print(f"Invalid input: {e}. Please try again.")

  if home_score == away_score:
      print("Extra innings!")
  if home_score > away_score:
          print(f"{home_team} wins!")
  if home_score < away_score:
          print(f"{away_team} wins!")

  # Ask if the user wants to continue
  continue_prompt = input("Do you want to continue? (yes/no): ").strip().lower()
  if continue_prompt != "yes":
      print("Thanks for using the Game Score Summary Card!")
      break


