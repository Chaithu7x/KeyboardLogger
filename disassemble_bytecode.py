import dis
import sys

def disassemble_bytecode_file(bytecode_file):
    with open(bytecode_file, 'rb') as file:
        bytecode = file.read()
        dis.dis(bytecode)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python disassemble_bytecode.py <bytecode_file>")
        sys.exit(1)

    bytecode_file = sys.argv[1]
    disassemble_bytecode_file("keyboard_logger.cpython-311.pyc")
