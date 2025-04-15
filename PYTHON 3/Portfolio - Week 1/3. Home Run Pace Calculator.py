while True:
    try:
        home_runs_so_far = int(input("How many home runs do you have so far? "))
        games_played = int(input("How many games have you played? "))
        season_length = int(input("How many games are in the season? "))

        projected_hr = (home_runs_so_far / games_played) * season_length

        print(f"Projected home runs for the season: {projected_hr:.2f}")

        continue_prompt = input("Do you want to continue? (yes/no): ").strip().lower()
        if continue_prompt != "yes":
            print("Thanks for using the Game Score Summary Card!")
            break

    except ValueError:
        print("Please enter valid numbers only.")
    except ZeroDivisionError:
        print("Games played cannot be zero.")
