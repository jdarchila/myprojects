import random

fortunes = ["You will have a great day!", "Something unexpected will happen soon.", "Good news is on its way.", "An opportunity will present itself.", "A pleasant surprise awaits you."]

fortune_index = random.randint(0, len(fortunes) - 1)
print(fortunes[fortune_index])
