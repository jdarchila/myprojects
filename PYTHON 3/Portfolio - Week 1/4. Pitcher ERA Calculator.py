earned_runs = int(input("Enter the number of earned runs: "))
innings_pitched = float(input("Enter the number of innings pitched: "))


# Calculate the ERA
era = (earned_runs * 9) / innings_pitched

print(f"The pitcher's ERA is: {era:.2f}")

