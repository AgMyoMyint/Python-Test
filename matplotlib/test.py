import matplotlib.pyplot as plt
import time as t

times = []
mistakes = 0

print ("this program will help u type faster. You will hav eto type faster")
input ("press enter to continue")

while len(times) < 5:

    start = t.time()
    word = input("Type the word: " )
    end = t.time()
    time_elapsed = end - start
    times.append(time_elapsed)

    if (word.lower() != "programming") :
        mistakes += 1

print("You made " + str(mistakes) + " mistakes.")
print("NOw let see your evolution")

t.sleep(3)

x = [1,2,3,4,5]
y = times

plt.plot(x, y)

legend = ["1", "2", "3", "4", "5"]
plt.xticks(x, legend)
plt.ylabel('Time in seonds')
plt.xlabel('Attempts')
plt.title('Your typing evolution')
plt.show()