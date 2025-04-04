def username_generator(first_name, last_name):
  
  username = first_name [:3] + last_name [:4]
  
  if (len(first_name))<3 and (len(last_name))<3:
    username = first_name + last_name
  return username

print(username_generator("Bo", "Dj")) # BobDail

