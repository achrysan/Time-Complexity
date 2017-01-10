import sys
import time

from HW3_Student_Solution import HW3_Student_Solution


# These should not have to be customized from hw to hw.
student_return = []
student_time = 0

def read_file(in_file):
    f = open(in_file, 'r')
    n = int(f.readline())
    vec = []

    for x in range(0, n):
        vec.append(int(f.readline()))

    f.close()
    return vec

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please provide the input filepath as the argument")
        sys.exit


    input_file = sys.argv[1]


    print("=======================================================================================================")
    print("Reading Input: " + input_file)

    # Read the file
    in_vec = read_file(input_file)


    start_time = time.clock()

    # Run student code
    student_class = HW3_Student_Solution(in_vec)
    student_return = student_class.output_vector()

    end_time = time.clock()
    student_time = end_time-start_time

    print("Your solution:")
    print("=======================================================================================================")
    print("Size: " + str(len(student_return)))
    print("Final vector: " + str(student_return))
    print("=======================================================================================================")

    print("Total time taken= "+str(student_time)+" secs")


