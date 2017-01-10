from HW6_StudentSolution import *
from readFromFile import *
import sys

def main():

	if (len(sys.argv) < 2):
		print("Please provide the input filepath as the argument")
		sys.exit()

	input_file = sys.argv[1]

	input = readFromFile(input_file)

	#Get answer
	output = HW6_StudentSolution(input)

	print(output)


if __name__ == '__main__':
	main()
