from printOutput import *
from readFromFile import *
from HW2_Student import *
import sys

def main():

	if (len(sys.argv) < 2):
		print("Please provide the input filepath as the argument")
		sys.exit()

	inputFile = sys.argv[1]

	hospitalCount, studentCount, hospPrefList, studentPrefList, hospOpenSlots = readFromFile(inputFile)

	residencyPairs = HW2_Student(hospitalCount, studentCount, hospPrefList, studentPrefList, hospOpenSlots)
	sortAndPrintMatchings(residencyPairs)


if __name__ == '__main__':
	main()