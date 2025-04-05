songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]

plays = {songs:playcounts for songs, playcounts in zip(songs, playcounts)}

print(plays)

#After printing plays, add a new entry to it. The entry should be for the song "Purple Haze" and the playcount is 1.

plays["Purple Haze"] = 1

print(plays)

#This user has caught Aretha Franklin fever and listened to “Respect” 5 more times. Update the value for "Respect" to be 94 in the plays dictionary.

plays["Respect"] = 94 

print(plays)

library = {"The Best Songs": plays, "Sunday Feelings": {}}

print(library)