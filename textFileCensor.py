def sed(findString, replaceString, readFile, writeFile):

	rFile = open(readFile, "r").read() #open the files
	wFile = open(writeFile, "w")
	
	for word in rFile.split():
		if (word != findString):
			wFile.write(word)
			wFile.write(" ")
			print(word)
		else:
			wFile.write(replaceString)
			wFile.write(" ")
			print(replaceString)

sed("evil","CENSORED","text.txt","outputFile.txt")
