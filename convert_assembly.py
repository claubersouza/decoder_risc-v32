from asyncio import LifoQueue
import os
import riscv_cte as rc
import riscv_func as rf
from riscv_opcode import *
from collections import deque

def verificaçao(filename):
    extension = os.path.splitext(filename)
    return extension

def convert_binary_to_hexadecimal(binary_string):
    """
    Converts a binary string to its hexadecimal representation.

    Args:
    binary_string (str): The binary string to be converted.

    Returns:
    str: The hexadecimal representation of the input binary string.

    This function takes a binary string as input, converts it to its corresponding
    hexadecimal representation, and returns the result as a string in uppercase.
    """
    hex_string = hex(int(binary_string, 2))[2:].upper()
    return hex_string

def getOpcode(instruction):
    """
    Retrieves the opcode of the given instruction.

    Args:
    instruction (str): The hexadecimal representation of the instruction.

    Returns:
    str: The opcode of the instruction.

    This function takes a hexadecimal representation of an instruction as input,
    converts it to an integer, and then retrieves the opcode using the decode_instruction
    function. It returns the opcode as a string.
    """
    int(instruction, 16)
    return decode_instruction(instruction)

def getAssembly(binary):
    """
    Converts a binary string to its corresponding assembly instruction.

    Args:
    binary (str): The binary string representing the instruction.

    Returns:
    ['AUIPC', ' 0x5', ' 0x17']

    This function takes a binary string, converts it to its hexadecimal representation,
    retrieves the opcode, and then parses the instruction to obtain its assembly format
    and components. It then modifies the assembly components and prints the format and
    modified assembly components.
    """


def getAssembly(binary):

    instruction = convert_binary_to_hexadecimal(binary)
    opcode = getOpcode("0x" + str(instruction))
    instruction = int('0x'+instruction,16)
    
    inst_type = rf.instruction_type(instruction & rc.FUNCT3_MASK)
    format, assembly = rf.instruction_parsing(inst_type,instruction)
    assembly = assembly.replace('[','')
    assembly = assembly.replace(']','')
    assembly = assembly.split(',')
    assembly = list(assembly)
    assembly.reverse()
    assembly[0] = str(opcode)
    if inst_type == 'I':
        append_file(assembly[0] + assembly[1] + assembly[2] +  assembly[3] + " " + assembly[4] + "-- "+ binary + " " + format )
    elif inst_type == 'U': 
        append_file(assembly[0] + " " + assembly[1]+ " " + assembly[2]  + "-- "+ binary + " " + format )
    elif inst_type == 'R':
        append_file(assembly[0] + assembly[1] + assembly[2] +  assembly[3] + " " + assembly[4] + "-- "+ binary + " " + format )
def append_file(word):
    with open("out.asm", 'a') as file:
        file.writelines(word+"\n")
    file.close()


def leitura_arquivo(filename):
    with open(filename, 'r') as file:
        for line in file.readlines():
            if line != '00000000000000000000000000000000\n' and line != '00100000010001010100001101010100\n' and line != '00001001100000100011101101101110\n' and line != '00001101010000110010011011011001\n' and line != '00010011000001000111011011011100\n':
                getAssembly(line.replace("\n",""))
      

def remove_file(filename):
    os.remove(filename)

def create_file_new(filename):
    file = open(filename, 'w')
    file.close()

def lista_arquivos():
    """
    Lists the files with a .img extension in the current directory and prompts the user to choose an image.

    This function retrieves a list of files with a .img extension in the current directory, prints the list with index numbers, and prompts the user to choose an image by entering the corresponding index number. It also attempts to read the contents of the files, but there is an issue with the indexing logic.

    Args:
    None

    Returns:
    None
    """
    files = os.listdir(".")
    files = [f for f in files if f.endswith(".img")]
    count = 0
    for file in files:
        print(str(count) + " - " +file)
        count = count +1
        count 
        leitura_arquivo(files[count])       
        

    
    file_name = input("Escolha a imagem:")
    # for filename in files:
    #     print(filename)



if __name__ == "__main__":
    remove_file("out.asm")
    create_file_new("out.asm")
    leitura_arquivo("crc.img")

