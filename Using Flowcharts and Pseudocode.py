# Get input from the user for test score and class rank
testScoreString = input("Enter the student's test score: ")
classRankString = input("Enter the student's class rank: ")

# Convert the input strings to integers
testScore = int(testScoreString)
classRank = int(classRankString)

# Logic to determine acceptance based on test score and class rank
if testScore >= 90:
    if classRank >= 25:
        print("Accept")
    else:
        print("Reject")
elif testScore >= 80:
    if classRank >= 50:
        print("Accept")
    else:
        print("Reject")
elif testScore >= 70:
    if classRank >= 75:
        print("Accept")
    else:
        print("Reject")
else:
    print("Reject")
