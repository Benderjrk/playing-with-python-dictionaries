sensors =  {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22}
num_cameras = {"backyard": 6, "garage": 2, "driveway": 1}

print(sensors)

translations = {"mountain": "orod", "bread": "bass", "friend": "mellon", "horse": "roch"}

children = {"von Trapp": ["Johannes", "Rosmarie", "Eleonore"], "Corleone":["Sonny", "Fredo", "Michael"]}

my_empty_dictionary = {}

animals_in_zoo = {}

animals_in_zoo["zebras"] = 8

animals_in_zoo["monkeys"] = 12

animals_in_zoo["dinosaurs"] = 0

print(animals_in_zoo)

user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}

user_ids.update({"theLooper": 138475, "stringQueen": 85739})

print(user_ids)

oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}

oscar_winners["Supporting Actress"] = "Viola Davis"
# print(oscar_winners)
oscar_winners["Best Picture"] = "Moonlight"
print(oscar_winners)

drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]
zipped_drinks = zip(drinks, caffeine)
drinks_to_caffeine = {key: value for key, value in zipped_drinks}

songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]

plays = {key:value for key,value in zip(songs, playcounts)}

print(plays)

plays["Purple Haze"] = 1

plays["Respect"] = 94

library = {"The Best Songs": plays, "Sunday Feelings" : {}}

print(library)

zodiac_elements = {"earth": ["Johannes", "Rosmarie", "Eleonore"],"Corleone": ["Sonny", "Fredo", "Michael"]}

print(zodiac_elements["earth"])

zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}

zodiac_elements["energy"] = "Not a Zodiac element"
print(zodiac_elements["energy"])

caffeine_level = {"espresso": 64, "chai": 40, "decaf": 0, "drip": 120}

caffeine_level['matcha'] = 30

try:
  print(caffeine_level['matcha'])
except KeyError:
  print("Unknown Caffeine Level")

user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}

tc_id =  user_ids.get("teraCoder")

print(tc_id)

stack_id = user_ids.get("superStackSmash", 100000)
print(stack_id)

available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}
health_points = 20

health_points = health_points + available_items.pop("stamina grains", 0)
health_points = health_points + available_items.pop("power stew", 0)

health_points = health_points + available_items.pop("mystic bread", 0)

print(available_items)
print(health_points)

user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

users = user_ids.keys()
lessons = num_exercises.keys()

print(users)
print(lessons)

num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

total_exercises = 0
for number in num_exercises.values():
  total_exercises += number
print(total_exercises)

pct_women_in_occupation = {"CEO": 28, "Engineering Manager": 9, "Pharmacist": 58, "Physician": 40, "Lawyer": 37, "Aerospace Engineer": 9}

for title, percent in pct_women_in_occupation.items():
  print("Women make up " + str(percent) + " percent of " + title + "s.")

tarot = { 1:	"The Magician", 2:	"The High Priestess", 3:	"The Empress", 4:	"The Emperor", 5:	"The Hierophant", 6:	"The Lovers", 7:	"The Chariot", 8:	"Strength", 9:	"The Hermit", 10:	"Wheel of Fortune", 11:	"Justice", 12:	"The Hanged Man", 13:	"Death", 14:	"Temperance", 15:	"The Devil", 16:	"The Tower", 17:	"The Star", 18:	"The Moon", 19:	"The Sun", 20:	"Judgement", 21:	"The World", 22: "The Fool"}

spread = {}

spread["past"] = tarot.pop(13)
spread["present"] = tarot.pop(22)

spread["future"] = tarot.pop(10)

for key, value in spread.items():
  print("Your " +key+ " is the " +value+ " card.")

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_points = {key:value for key, value in zip(letters, points)}
# print(letter_to_points)

letter_to_points[" "] = 0
# print(letter_to_points)

def score_word(word):
  point_total = 0
  for letter in word:
    letter_points = letter_to_points.get(letter.upper(), 0)
    point_total += letter_points
  return point_total

brownie_points = score_word("brownie")
# print(brownie_points)

player_to_words = {"player1": ["BLUE", "TENNIS", "EXIT"], "wordNerd": ["EARTH", "EYES", "MACHINE"], "Lexi Con": ["ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}

# print(player_to_words)

player_to_points = {}

for player, words in player_to_words.items():
  player_points = 0
  for word in words:
    points = score_word(word)
    player_points += points
  player_to_points[player] = player_points

print(player_to_points)
print('\n')

def update_point_totals():
  for player, words in player_to_words.items():
    player_points = 0
    for word in words:
      points = score_word(word)
      player_points += points
    player_to_points[player] = player_points

def play_word(player, word):
  words = player_to_words.get(player, [])
  if words != []:
    words.append(word)
  else: 
    player_to_words[player] = [word]


play_word("Justin", "Log")
play_word("player1", "Log")
update_point_totals()
print('lol', player_to_words)
print('\n')

print(player_to_points)

# Write your sum_values function here:
def sum_values(my_dictionary):
  total_value = 0
  for value in my_dictionary.values():
    total_value += value
  return total_value

# Uncomment these function calls to test your sum_values function:
print(sum_values({"milk":5, "eggs":2, "flour": 3}))
# should print 10
print(sum_values({10:1, 100:2, 1000:3}))
# should print 6

# Write your sum_even_keys function here:
def sum_even_keys(my_dictionary):
  total_evens_sum = 0
  #sum of values of even keys
  for key, value in my_dictionary.items():
    if key % 2 is 0:
      total_evens_sum += value
  return total_evens_sum
# Uncomment these function calls to test your  function:
print(sum_even_keys({1:5, 2:2, 3:3}))
# should print 2
print(sum_even_keys({10:1, 100:2, 1000:3}))
# should print 6

# Write your add_ten function here:
def add_ten(my_dictionary):
  for key in my_dictionary.keys():
    my_dictionary[key] += 10
  return my_dictionary

# Uncomment these function calls to test your  function:
print(add_ten({1:5, 2:2, 3:3}))
# should print {1:15, 2:12, 3:13}
print(add_ten({10:1, 100:2, 1000:3}))
# should print {10:11, 100:12, 1000:13}

# Write your values_that_are_keys function here:
def values_that_are_keys(my_dictionary):
  values_that_are_keys = []
  keys = my_dictionary.keys()
  values = my_dictionary.values()
  for value in values:
    if value in keys:
      values_that_are_keys.append(value)
  return values_that_are_keys
# Uncomment these function calls to test your  function:
print(values_that_are_keys({1:100, 2:1, 3:4, 4:10}))
# should print [1, 4]
print(values_that_are_keys({"a":"apple", "b":"a", "c":100}))
# should print ["a"]

# Write your max_key function here:
def max_key(my_dictionary):
  largest_key = float("-inf")
  largest_value = float("-inf")
  for key, value in my_dictionary.items():
    if value > largest_value:
      largest_value = value
      largest_key = key
  return largest_key

# Uncomment these function calls to test your  function:
print(max_key({1:100, 2:1, 3:4, 4:10}))
# should print 1
print(max_key({"a":100, "b":10, "c":1000}))
# should print "c"

# Write your word_length_dictionary function here:
def word_length_dictionary(words):
  #key value pairs 
  #key is the word
  word_lengths = []
  #value is the length of words
  for i in range(len(words)):
    word_lengths.append(len(words[i]))
  word_length_dictionary = {key:value for key, value in zip(words, word_lengths)}
  return word_length_dictionary
# Uncomment these function calls to test your  function:
print(word_length_dictionary(["apple", "dog", "cat"]))
# should print {"apple":5, "dog": 3, "cat":3}
print(word_length_dictionary(["a", ""]))
# should print {"a": 1, "": 0}

# Write your frequency_dictionary function here:
def frequency_dictionary(words):
  freq_dictionary = {}
  for word in words:
    if word in freq_dictionary.keys():
      freq_dictionary[word] += 1
    else:
      freq_dictionary[word] = 1
  return freq_dictionary
# Uncomment these function calls to test your  function:
print(frequency_dictionary(["apple", "apple", "cat", 1]))
# should print {"apple":2, "cat":1, 1:1}
print(frequency_dictionary([0,0,0,0,0]))
# should print {0:5}

# Write your unique_values function here:
def unique_values(my_dictionary):
  seen_values = []
  for value in my_dictionary.values():
    if value not in seen_values:
      seen_values.append(value)
  return len(seen_values)

# Uncomment these function calls to test your  function:
print(unique_values({0:3, 1:1, 4:1, 5:3}))
# should print 2
print(unique_values({0:3, 1:3, 4:3, 5:3}))
# should print 1

# Write your count_first_letter function here:
def count_first_letter(names):
  
  new_dict = {}
  for key, values in names.items():
    if key[0] in new_dict:
      new_dict[key[0]] += len(values)
    else:
      new_dict[key[0]] = len(values)
# return a new dictionary where each key = first letter last name
# value = # people whose last name begins with that letter.
  return new_dict

# Uncomment these function calls to test your  function:
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 4, "L": 3}
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Sannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 7}