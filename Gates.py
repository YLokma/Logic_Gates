def and_gate(input_1, input_2):
    """This is a function to represent the AND gate.

    Args:
        input_1 ([int]): [this is an input to determine the output of AND gate]
        input_2 ([int]): [this is an input to determine the output of AND gate]
    """ """"""
    if input_1 * input_2 == 1:
        return 1
    elif input_1 * input_2 == 0:
        return 0

def not_gate(input_1):
    """This is a function to represent the NOT gate

    Args:
        input_1 ([Int]): [this is an input to determine the output of NOT gate]
    """
    if input_1 == 0:
        return 1
    elif input_1 == 1:
        return 0

def or_gate(input_1, input_2):
    """This is a function to represent the AND gate.

    Args:
        input_1 ([int]): [this is an input to determine the output of OR gate]
        input_2 ([int]): [this is an input to determine the output of OR gate]
    """ """"""
    if input_1 + input_2 >= 1:
        return 1
    elif input_1 + input_2 == 0:
        return 0

def nand_gate(input_1, input_2):
    """This is a function to represent the AND gate.

    Args:
     input_1 ([int]): [this is an input to determine the output of NAND gate]
     input_2 ([int]): [this is an input to determine the output of NAND gate]
    """
    if input_1 * input_2 == 1:
        return 0
    elif input_1 * input_2 == 0:
        return 1

def nor_gate(input_1, input_2):
    """This is a function to represent the AND gate.

    Args:
     input_1 ([int]): [this is an input to determine the output of NOR gate]
     input_2 ([int]): [this is an input to determine the output of NOR gate]
    """
    if input_1 + input_2 >= 1:
        return 0
    elif input_1 + input_2 == 0:
        return 1

def xor_gate(input_1, input_2):
    """This is a function to represent the AND gate.

    Args:
        input_1 ([int]): [this is an input to determine the output of OR gate]
        input_2 ([int]): [this is an input to determine the output of OR gate]
    """ """"""
    if input_1 + input_2 == 1:
        return 1
    else:
        return 0

Gates = [not_gate,and_gate,or_gate,nand_gate,nor_gate,xor_gate]