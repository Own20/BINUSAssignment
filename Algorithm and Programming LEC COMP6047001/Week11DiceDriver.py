from Week11MyDice import Dice
import pygal

die = Dice()

results = []
for r in range(100):
    result = die.roll()
    results.append(result)

frequencies = []
for f in range(1, die.numSides+1):
    frequency = results.count(f)
    frequencies.append(frequency)

print(results)
print(frequencies)

hist = pygal.Bar()
hist.title = ""
hist.x_labels = ["1", "2", "3", "4", "5", "6"]
hist.y_labels = "Result"
hist.y_title = "Frequency Result"