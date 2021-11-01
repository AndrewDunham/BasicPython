file = open(inputFile,"r")
    #Read each line and split them into the type and details
    lines = file.readlines()
    for line in lines:
        #Get the line type and details of each line
        lineType = line.split(':')[0]
        lineDetails = line.split(':')[1]
        lineDetails = lineDetails.rstrip()
