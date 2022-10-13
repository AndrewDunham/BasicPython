def palindrome_checker(inputString: int):
	reversedLetters = []
	
	for letter in reversed(inputString):
		reversedLetters.append(letter)
	reversedString = "".join(reversedLetters)
	
	if inputString == reversedString:
		print(inputString+ ": is a palindrome")
	else: 
		print(inputString+ ": is not a palindrome")

if __name__ == "__main__":
	stringList = ["tat", "john", "Andrew", "wonder", "poop", "yellow", "taco"]
	for string in stringList:
		palindrome_checker(string)
