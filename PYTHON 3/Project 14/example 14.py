# Uncomment this when you reach the "Use the Force" section
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1


# Write your code below: 


#TASK 1 AND 2
def f_to_c (f_temp):
  c_temp = (f_temp - 32) * 5/9
  return c_temp

f100_in_celcius = f_to_c(100)

print(f100_in_celcius)

print("---------")

#TASK 2 AND 3 
def c_to_f (c_temp):
  f_temp = ((c_temp * 9/5) + 32)
  return f_temp

c0_in_fahrenheit = c_to_f(0)

print(c0_in_fahrenheit)

print("==========")

#TASK 3 AND 4 

def get_force (mass, acceleration):
  print(mass*acceleration)

  return (mass*acceleration)


get_force(10, 10)

print("==========")

def get_force2 (mass2, acceleration2):
  return (mass2*acceleration2)

print(get_force2(80, 10))

print("==========")

def get_force3 (mass3, acceleration3):
  return (mass3*acceleration3)

train_force = get_force3(train_mass, train_acceleration)

print(train_force)

print("==========")

print("The GE train supplies", train_force ,"Newtons of force.")

print("==========")

def get_energy (mass, c=3*10**8):
  return (mass *(c**2))

bomb_energy = ((get_energy(bomb_mass)))
print(bomb_energy)

print("==========")

print("A 1kg bomb supplies", bomb_energy, "Joules.")

print("==========")

def get_work (mass5, acceleration5, distance5):
  force = get_force(mass5, acceleration5)
  return force * distance5 

print(get_work(1, 1, 1))

print("==========")

def get_work6 (train_mass, train_acceleration, train_distance):
  train_work = get_force(train_mass, train_acceleration)
  return train_work * train_distance

print(get_work(1, 1, 1))

print("==========")

print("he GE train does ", train_force ," Joules of work over ", train_distance, "meters.")





   

