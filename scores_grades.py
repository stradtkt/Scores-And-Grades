import random

def grade(people):
  print("Scores and Grades")
  for x in range(0, people):
    score = random.randint(60, 101)
    if score >= 60 and score <= 69:
      print("Student: #{}: Score: {}; Your grade is a D".format(x, score))
    elif score >= 70 and score <= 79:
      print("Student: #{}: Score: {}; Your grade is a C".format(x, score))
    elif score >= 80 and score <= 89:
      print("Student: #{}: Score: {}; Your grade is a B".format(x, score))
    elif score >= 90 and score <= 100:
      print("Student: #{}: Score: {}; Your grade is a A".format(x, score))
    else:
      print("You failed")
  print("End of program. Bye!")

grade(10)