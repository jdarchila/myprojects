while True:
    try:

      runs_scored = int(input("Enter the number of runs scored: "))
      runs_allowed = int(input("Enter the number of runs allowed: "))

      diff = runs_scored - runs_allowed 

      if diff > 0:
          print("Dominant performance.")
      elif diff == 0:
          print("Even performance.")
      else:
          print("Poor performance.")

      continue_prompt = input("Do you want to check another differential? (yes/no): ").strip().lower()
      if continue_prompt != "yes":
          print("Thanks for using the Differential Evaluator!")
          break

    except ValueError:
        print("Please enter valid numbers only.")
    except ZeroDivisionError:
        print("Runs allowed cannot be zero.")

