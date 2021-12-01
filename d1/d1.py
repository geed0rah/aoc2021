file = open("data")
data = file.read().splitlines()

current_number = 0
first = True
increasingCount = 0
decreasingCount = 0
for number in data:
    if int(number.rstrip()) > current_number: 
        if not first:
            increasingCount = increasingCount + 1
    else:
        decreasingCount = decreasingCount + 1
    current_number = int(number)
    first = False
print("PART 1: increasing count: " + str(increasingCount))

increasingCount2 = 0
for i in range(len(data)-3):
    j = i + 1

    if (int(data[i]) + int(data[i+1]) + int(data[i+2])) < (int(data[j]) + int(data[j+1]) + int(data[j+2])):
        increasingCount2 = increasingCount2 + 1
print("PART 2: increasing count: " + str(increasingCount2))