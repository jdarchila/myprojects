#Next, we will create a function which calculates the percentage of games won. In order to do this, we will need to know how many total games there were and divide the number of wins by the total number of games. For this function, there will be two input parameters, the number of wins and the number of losses. We also need to make sure that we return the result as a percentage (in the range of 0 to 100). In order to create this method we need the following steps:

#Define the function header with two parameters, wins and losses
#Calculate the total number of games using the number of wins and losses
#Get the ratio of winning using the number of wins out of the total number of games.
#Convert the ratio to a percentage
#Return the percentage

#Create a function called win_percentage() that takes two parameters named wins and losses.

#This function should return out the total percentage of games won by a team based on these two numbers.

def win_percentage(wins, losses):
  return (wins / (wins + losses)) * 100

print(win_percentage(5, 5))
# should print 50
print(win_percentage(10, 0))
# should print 100


