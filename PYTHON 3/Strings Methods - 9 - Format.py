#The information for each poem is separated by commas, and within this information is the title of the poem, the author, and the date of publication.

#Start by splitting highlighted_poems at the commas and saving it to highlighted_poems_list.

highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

print(highlighted_poems)

print("")

highlighted_poems_list = highlighted_poems.split(",")

print(highlighted_poems_list)

print("")

highlighted_poems_stripped = []

for i in highlighted_poems_list:
  highlighted_poems_stripped.append(i.strip())
  
print(highlighted_poems_stripped )

print("")

#Iterate through highlighted_poems_stripped and split each string around the : characters and append the new lists into highlighted_poems_details.

highlighted_poems_details = []

for i in highlighted_poems_stripped:
  highlighted_poems_details.append(i.split(":"))
print(highlighted_poems_details)

print("")

#Iterate through highlighted_poems_details and for each list in the list append the appropriate elements into the lists titles, poets, and dates.

#For example, for the poem The Shadow (1915) by William Carlos Williams your code should be adding "The Shadow" to titles, "William Carlos Williams" to poets, and "1915" to dates.


titles = []
poets = []
dates = []

for i in highlighted_poems_details:
  titles.append(i[0])
  poets.append(i[1])
  dates.append(i[2])

print("")

print(titles)
print("")
print(poets)
print("")       
print(dates)
print("")     

print("")

#Finally, write a for loop that uses .format() to print out the following string for each poem:

for i in range(len(titles)): 
  print("The poem {} was published by {} in {}.".format(titles[i], poets[i], dates[i]))





