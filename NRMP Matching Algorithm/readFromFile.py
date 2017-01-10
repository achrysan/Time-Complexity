def readFromFile(inputFile):

	with open(inputFile, 'r') as file:

		hospPrefLists = {}
		studentPrefLists = {}
		hospOpenSlots = {}

		hospCount = int(file.readline())
		studentCount = int(file.readline())

		for hospital in range(1, hospCount + 1):

			splitLine = file.readline().split()
			intValues = list(map(int, splitLine))

			hospOpenSlots[hospital] = intValues[0]
			hospPrefLists[hospital] = intValues[1:]

		for student in range(1, studentCount + 1):

			splitLine = file.readline().split()
			intValues = list(map(int, splitLine))

			studentPrefLists[student] = intValues

		return (hospCount, studentCount, hospPrefLists, studentPrefLists, hospOpenSlots)




# For debugging purposes
def main():
	readFromFile('input1.txt')

if __name__ == '__main__':
	main()
