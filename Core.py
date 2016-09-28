#Author: Andy O'Connell <aoconnel@bu.edu> <andrewoconnell89@gmail.com>
#
#	--------------------------   R-Format   --------------------------
#	o----------------------------------------------------------------o
#	| opcode  |    rs   |    rt    |   rd   | shift (shamt) | funct  |
#	|---------|---------|----------|--------|---------------|--------|	
#	| 6 bits  |  5 bits |	5 bits | 5 bits |     5 bits    | 6 bits |
#	o----------------------------------------------------------------o


#	--------------  I-Format  ----------------
#	o----------------------------------------o
#	| opcode |    rs   |    rt    |    IMM   |
#	|--------|---------|----------|----------|
#	| 6 bits |  5 bits |  5 bits  | 16 bits  |
#	o----------------------------------------o

	
#	==================================   OPCODES   ==============================
#	o---------------------------------------------------------------------------o
#	|  mNEMONIC |          MEANING			|   TYPE	|	OPCODE	|	FUNCT	|
#	|===========================================================================|
#	|	add		|	ADD						|	R		|	0x00	|	0x20	|
#	|	sub		|	Subtract				|	R		|	0x00	|	0x22	|
#	|	and		|	Bit AND					|	R		|	0x00	|	0x24	|	
#	|	or		|	Bit OR					|	R		|	0x00	|	0x25	|
#	|	slt		|	Set to 1 if Less than	|	R		|	0x00	|	0x2A	|
#	|	sw		|	Store Word				|	I		|	0x2B	|	N/A		|
#	|	beq		|	Branch if Equal			|	I		|	0x04	|	N/A		|
#	|	bne		|	Brance if Not Equal		|	I		|	0x05	|	N/A		|
#	o---------------------------------------------------------------------------o

#	0 1 2 3 4 5 6 7 8 9 A B C D E F


class Disassembler(object):

	#Constructor
	def __init__(self,instruction):
		self.instruction = instruction
		self.opcode = None
		self.rs = None
		self.rt = None
		self.rd = None
		self.shift = None
		self.funct = None
		self.on_create()
		

	def on_create(self):
		#isolate the OPCODE
		# 1111 1100 0000 0000 0000 0000 0000 0000
		#   F    C   0    0    0    0    0    0
		opcode_MASK = 0xfc000000
		self.opcode = self.instruction & opcode_MASK
		print("{0:b}".format(self.opcode))
