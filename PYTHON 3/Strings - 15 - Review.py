#Inside password_generator, create a for loop that iterates through the indices of user_name by going from 0 to len(user_name).

#The loop should create the password by shifting all the letters of user_name one to the right. To do so, add the letter at the previous index of user_name to password with each pass of the loop.

#After the for loop but still within the definition of password_generator, return the password.


def password_generator(user_name):
  
    password = ""
    for i in range(0, len(user_name)):
        password += user_name[i-1]
    return password
  
print(password_generator("ReikoMatsuki"))
