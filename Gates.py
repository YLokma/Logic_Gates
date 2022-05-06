def not_gate(wire1:list,wire2=[]):
    wire_out = []
    for i in range(len(wire1)):
        if wire1[i] == 1: wire_out.append(0)
        else: wire_out.append(1)
    return wire_out

def and_gate(wire1:list,wire2:list):
    wire_out = []
    for i in range(0,len(wire1)):
        wire_out.append(wire1[i]*wire2[i])
    return wire_out

def or_gate(wire1:list,wire2:list):
    wire_out = []
    for i in range(len(wire1)):
        wire_out.append(wire1[i]+wire2[i])
        if wire_out[i] > 0: wire_out[i] = 1
        else: wire_out[i] = 0
    return wire_out

def nand_gate(wire1:list,wire2:list):
    return not_gate(and_gate(wire1, wire2))

def nor_gate(wire1:list,wire2:list):
    return not_gate(or_gate(wire1, wire2))

def xor_gate(wire1:list,wire2:list):
    wire_out = []
    for i in range(len(wire1)):
        wire_out.append(wire1[i]+wire2[i])
        if wire_out[i] == 1: wire_out[i] = 1
        else: wire_out[i] = 0
    return wire_out

Gates = [not_gate,and_gate,or_gate,nand_gate,nor_gate,xor_gate]
