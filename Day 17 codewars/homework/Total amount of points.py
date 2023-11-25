# Our football team has finished the championship.

# Our team's match results are recorded in a collection of strings. 
# Each match is represented by a string in the format "x:y", where x 
# is our team's score and y is our opponents score.

# For example: ["3:1", "2:2", "0:1", ...]

# Points are awarded for each match as follows:

# if x > y: 3 points (win)
# if x < y: 0 points (loss)
# if x = y: 1 point (tie)
# We need to write a function that takes this collection and returns 
# the number of points our team (x) got in the championship by the 
# rules given above.

def points(games):
    result = 0                  # we create a variable which is zero
    for i in games:             # დავატრიალეთ for ციკლი
        if i[0] > i[2]:         # ყოველ იტერაციაზე როცა მენულე ელემენტი მეტი იქნება მეორე ელემენტზე
            result += 3         # result-ს დაემატოს 3
        if i[0] == i[2]:        # როცა მენულე ელემენტი გაუტოლდება მეორე ელემენტზე
            result += 1         # result-ს დაემატოს 1
        if i[0] < i[2]:         # როცა მენულე ელემენტი ნაკლები იქნება მეორე ელემენტზე
            result += 0         # result-ს დაემატოს 0
    return result

print(points(['3:0','1:1','4:3','2:0','3:0','0:1']))
# print(games[0][2])



# if games[0][0] > games[2][2]: