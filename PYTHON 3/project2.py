while True:
  while True:
    try:
      weight = float(input("What's the weight of your package? "))
      break # Break out of the loop if the input is valid
    except ValueError:
        print("Error: Please enter a valid number for the weight.")
  print("")


  cost_ground_shipping = " "

  #Cost Ground Shipping 

  if weight >= 10:
    cost_ground_shipping = (weight * 4.75) + 20 
  elif weight >= 6:
    cost_ground_shipping = (weight * 4) + 20
  elif weight >= 2:
    cost_ground_shipping = (weight * 3) + 20
  elif weight < 2:
    cost_ground_shipping = (weight * 1.50) + 20

  print ("Your total for Ground Shipping is $", cost_ground_shipping)

  #Cost Ground Shipping Premium

  cost_ground_shipping_premium = 125

  print ("Your total for Ground Premium is $", cost_ground_shipping_premium)

  #Cost Drone Shipping

  if weight >= 10:
    cost_drone_shipping = (weight * 14.25) 
  elif weight >= 6:
    cost_drone_shipping = (weight * 12) 
  elif weight >= 2:
    cost_drone_shipping = (weight * 9) 
  elif weight < 2:
    cost_drone_shipping = (weight * 4.50)

  print ("Your total for Drone Shipping is $", cost_drone_shipping)

  print("")

  # Determine the cheapest shipping option using min()
  best_cost = min(cost_ground_shipping, cost_ground_shipping_premium, cost_drone_shipping)

  if best_cost == cost_ground_shipping:
      print("The best option is Ground Shipping, it costs $", cost_ground_shipping)
  elif best_cost == cost_ground_shipping_premium:
      print("The best option is Ground Shipping Premium, it costs $", cost_ground_shipping_premium)
  else:
      print("The best option is Drone Shipping, it costs $", cost_drone_shipping)

  print("")

  # Ask if the user wants to calculate again
  again = input("Would you like to calculate shipping for another package? (y/n): ")
  if again.lower() != 'y':
    print("Goodbye!")
    break

