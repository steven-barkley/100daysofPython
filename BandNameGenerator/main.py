### Pseudocode
# Print the statement "Welcome to the Band Name Generator."
# Print the statement "What's the name of the city you grew up in?" Await string input
# Print string input
# Print the statement "What's your pet's name?" Await string input
# Print string input
# Print the statement "Your band name could be {input1 + " " + input2}"

print("Welcome to the Band Name Generator")
answer1 = input("What's the name of the city you grew up in?")
print(" " + answer1)
answer2 = input("What's your pet's name?")
print(" " + answer2)
print("Your band name could be % s" % (answer1 + " " + answer2))