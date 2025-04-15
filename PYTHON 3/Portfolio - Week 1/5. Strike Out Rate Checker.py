while True:
    try:
      strikeouts = int(input("Enter the number of strikeouts: "))
      batters_faced = int(input("Enter the number of batters faced: "))

      # Calculate the strikeout rate

      strikeout_rate = (strikeouts / batters_faced) * 100

      print(f"The pitcher's strikeout rate is: {strikeout_rate:.2f}%")

      if strikeout_rate < 20:
          print("Below average strikeout rate.")
      elif strikeout_rate <= 25:
          print("Average strikeout rate.")
      else:
          print("Above average strikeout rate.")

      continue_prompt = input("Do you want to check another another strikeout rate? (yes/no): ").strip().lower()
      if continue_prompt != "yes":
          print("Thanks for using the Strikeouot Rate Checker!")
          break 
      
    except ValueError:
        print("Please enter valid numbers only.")
    except ZeroDivisionError:
        print("Batters cannot be zero.")
