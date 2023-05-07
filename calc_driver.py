from src import Calculator
from typing import List
import os
import sys
import struct

def open_dir(file_list, arg):
    if not os.path.isdir(arg):
        return
    else:
        with os.scandir(arg) as entries:
            for entry in entries:
                if os.path.isdir(entry):
                    open_dir(file_list, entry)
                else:
                    file_list.append(os.path.realpath(entry))
    return file_list

def get_file_header(file):
    file_header = file.read(27)
    file_header_decoded = struct.unpack("<IQQBIH", file_header)
    return list(file_header_decoded)

def find_problem_set(file_header: list):
    return file_header[2]

def modify_file_header(file_header: list):
    file_header[3] = 0x01
    
def pack_header(file_header):
    return struct.pack("<IQQBIH", file_header[0], file_header[1], file_header[2], file_header[3] , file_header[4], file_header[5])

def process_file(arg: str, calc):
    operators = {0x01: calc.add, 0x02: calc.subtract, 0x03: calc.multiply, 0x04: calc.divide, 0x05: calc.mod}
    path = "/".join([sys.argv[2], arg.split("/")[-1]])
    solved = open(path, "wb")
    with open(arg, "rb") as binary:
        file_header = get_file_header(binary)
        current_problem = 1
        modify_file_header(file_header)
        solved.write(pack_header(file_header))
        while find_problem_set(file_header) >= current_problem:
            equation = binary.read(32)
            equation_unpacked = struct.unpack("<IxqBq10x", equation)
            equation_id = equation_unpacked[0]
            num_a = equation_unpacked[1]
            operand = equation_unpacked[2]
            num_b = equation_unpacked[3]
            current_problem += 1
            solution = operators[operand](num_a, num_b)
            problem = struct.pack("<IBBq", equation_id, 1, 1, int(solution))
            solved.write(problem)
        solved.close()


def main(args):
    calc = Calculator()

    if len(args) != 3:
        raise ValueError("<Execuatable> <Unsolved file> <solved file>")
    files = list()
    open_dir(files, args[1])

    for file in files:
        size = os.path.getsize(file)
        process_file(file, calc)



if __name__ == "__main__":
    main(sys.argv)