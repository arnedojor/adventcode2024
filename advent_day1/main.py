
# Get list of numbers
with open("input.txt") as file:
    numbers_list = file.read()

# Delete the blank space between the numbers, to leave only numbers on the list
numbers_list = numbers_list.split()

# Separate the list into 2 columns
left_numbers = []
right_numbers = []

for index in range(0,len(numbers_list)):
    if index % 2 == 0:
        # Even numbers correspond to the left column (start at 0)
        left_numbers.append(int(numbers_list[index]))
    else:
        # Odd numbers correspond to the right column
        right_numbers.append(int(numbers_list[index]))

# Sort the list from smallest to largest
left_numbers.sort()
right_numbers.sort()

# Compute the differences
distances = []

for index in range(0,len(left_numbers)):
    distance = abs(left_numbers[index]-right_numbers[index])
    distances.append(distance)

total_distance = sum(distances)

print(f"The total distance between the lists is {total_distance}")

# Compute the Similarity Score

similarity_score_list = []

for number in left_numbers:
    coincidence_list = [x for x in right_numbers if number == x]
    similarity_score_list.append(len(coincidence_list)*number)

similarity_score = sum(similarity_score_list)

print(f"The Similarity Score between the lists is {similarity_score}")





