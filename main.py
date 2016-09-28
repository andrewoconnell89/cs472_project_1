from MipsDisassembler.Core import Disassembler

instructionList = [	0x022DA822,	0x8EF30018,
					0x12A70004, 0x02689820,
					0xAD930018,	0x02697824,
					0xAD8FFFF4,	0x018C6020,
					0x02A4A825,	0x158FFFF6,
					0x8E59FFF0	]
	
def main():
	dis = Disassembler( instructionList[0] )


if __name__ == '__main__':
	main()
