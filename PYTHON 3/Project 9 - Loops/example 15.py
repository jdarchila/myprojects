# Write your code below: 

def calculate_expenses (plane_ticket_price, car_rental_rate, hotel_rate, trip_time):
  car_rental_total = car_rental_rate * trip_time
  hotel_total = hotel_rate * trip_time - 10 
  trip_total = car_rental_total + hotel_total + plane_ticket_price

  return trip_total, hotel_total, car_rental_total

# Step 5: call your function

trip, hotel, car = calculate_expenses (200, 100, 100, 5)

print("This is for the trip ", trip)
print("This is for the hotel ", hotel)
print("This is for the car ", car)
