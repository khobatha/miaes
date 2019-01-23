#! /usr/bin/python3
import subprocess
from copy import copy
from migen import *
from migen.fhdl import verilog
from migen.fhdl.verilog import convert

##### string converters ####
# change plaintext to a matrix
def textconverter(text):
	size = len(text) # size of plaintext

	#to hold the plaintext matrix
	newText = [] 

	# copy text into newText
	for i in range(size):
		newText.append(text[i])
	
	return newText

# change key text to a matrix
def keyconverter(key):
	size = len(key) # size of key
	assert size == 16

	#to hold the key matrix
	newkey = [] 

	# copy key into newkey
	for i in range(size):
		newkey.append(key[i])
	
	return newkey
    
def hexCharToInt(ch):
        if ch=='0' or ch=='1' or ch=='2' or ch=='3' or ch=='4' or ch=='5' or ch=='6' or ch=='7' or ch=='8' or ch=='9':
            return int(ch)
        elif ch=='a' or ch=='b' or ch=='c' or ch=='d' or ch=='e' or ch=='f': 
            return int(ch,16)
        else:
            return 0
##############################

class AES(Module): # top level AES core
	def __init__(self):
		self.ptext = [Signal(8, name="ptext{}".format(x)) for x in range(16)]# plain text input to the AES Encryptor
		self.key = [Signal(8, name="key{}".format(x)) for x in range(16)]# cipher key input to the AES Encryptor
		self.ctext=[Signal(8, name="ctext{}".format(x)) for x in range(16)]# cipher text output from the AES Encryptor
		self.recovered=[Signal(8, name="rec{}".format(x)) for x in range(16)]# recovered text output from the AES Decryptor

		self.temp=[Signal(8, name="temp{}".format(x)) for x in range(16)]# temporary matrix in progress, input to AES Decryptor
	
		self.io = set(self.ctext) | set(self.ptext) | set(self.recovered) | set(self.key)# specify ctext, ptext and key as IO ports of this Module
		
		self.enc=AES_Enc()

		# duplicate ctext on temp matrix
		for x in range(16):
			self.comb += self.temp[x].eq(self.ctext[x])
			
		#self.dec=AES_Dec()	
		"""
		j = Instance("AES_Dec",
			i_master_clk=ClockSignal(),
			i_master_rst=ResetSignal(),

			# 16 bytes message - input to the AES_Dec Module
			i_ctext0=self.temp[0],
			i_ctext1=self.temp[1],
			i_ctext2=self.temp[2],
			i_ctext3=self.temp[3],
			i_ctext4=self.temp[4],
			i_ctext5=self.temp[5],
			i_ctext6=self.temp[6],
			i_ctext7=self.temp[7],
			i_ctext8=self.temp[8],
			i_ctext9=self.temp[9],
			i_ctext10=self.temp[10],
			i_ctext11=self.temp[11],
			i_ctext12=self.temp[12],
			i_ctext13=self.temp[13],
			i_ctext14=self.temp[14],
			i_ctext15=self.temp[15],
                     
			# 16 bytes key - input to the AES_Dec Module
			i_key0=self.key[0],
			i_key1=self.key[1],
			i_key2=self.key[2],
			i_key3=self.key[3],
			i_key4=self.key[4],
			i_key5=self.key[5],
			i_key6=self.key[6],
			i_key7=self.key[7],
			i_key8=self.key[8],
			i_key9=self.key[9],
			i_key10=self.key[10],
			i_key11=self.key[11],
			i_key12=self.key[12],
			i_key13=self.key[13],
			i_key14=self.key[14],
			i_key15=self.key[15],

			# 16 bytes ciphertext - output from the AES_Dec Module
			o_ptext0=self.recovered[0],
			o_ptext1=self.recovered[1],
			o_ptext2=self.recovered[2],
			o_ptext3=self.recovered[3],
			o_ptext4=self.recovered[4],
			o_ptext5=self.recovered[5],
			o_ptext6=self.recovered[6],
			o_ptext7=self.recovered[7],
			o_ptext8=self.recovered[8],
			o_ptext9=self.recovered[9],
			o_ptext10=self.recovered[10],
			o_ptext11=self.recovered[11],
			o_ptext12=self.recovered[12],
			o_ptext13=self.recovered[13],
			o_ptext14=self.recovered[14],
			o_ptext15=self.recovered[15]
                     
		)

		self.specials += i, j
		"""
		### specify the Module behavior below


class AES_Enc(Module): # AES Encryption core
	def __init__(self):
		self.ptext = [Signal(8, name="ptext{}".format(x)) for x in range(16)]# plain text input from the AES top level module
		self.key = [Signal(8, name="key{}".format(x)) for x in range(16)]# cipher key input to the AES core
		self.ctext=[Signal(8, name="ctext{}".format(x)) for x in range(16)]# cipher text output from the AES cipher

		self.temp=[Signal(8, name="temp{}".format(x)) for x in range(16)] # temporary matrices in progress
		self.temp1=[Signal(8, name="temp1{}".format(x)) for x in range(16)]
		self.temp2=[Signal(8, name="temp2{}".format(x)) for x in range(16)]
	
		self.io = set(self.ctext) | set(self.ptext) | set(self.key)# specify ctext, ptext and key as IO ports of this Module
		
		# instantiate sub modules here
		self.addkey=AddRoundKey()
		self.subbytes=SubBytes()
		self.shiftrow=ShiftRow()
		self.mixcolumn=MixColumn()
		
		# duplicate ctext on temp matrix
		for x in range(16):
			self.comb += self.temp[x].eq(self.ctext[x])
			
		# duplicate ctext on temp1 matrix
		for y in range(16):
			self.comb += self.temp1[y].eq(self.ctext[y])
			
		# duplicate ctext on temp2 matrix
		for z in range(16):
			self.comb += self.temp2[z].eq(self.ctext[z])
			
class AES_Dec(Module): # top level AES Decryption core
	def __init__(self):
		self.ctext=[Signal(8, name="ctext{}".format(x)) for x in range(16)]# cipher text input from AES top level module
		self.key = [Signal(8, name="key{}".format(x)) for x in range(16)]# cipher key input to the AES core
		self.ptext = [Signal(8, name="ptext{}".format(x)) for x in range(16)]# plain text output port from AES core
			
		self.temp=[Signal(8, name="temp{}".format(x)) for x in range(16)] # temporary matrices in progress
		self.temp1=[Signal(8, name="temp1{}".format(x)) for x in range(16)]
		self.temp2=[Signal(8, name="temp2{}".format(x)) for x in range(16)]

		self.io = set(self.ctext) | set(self.ptext) | set(self.key)# specify ctext, ptext and key as IO ports of this Module
		"""
        
		i = Instance("MixColumnInv",
			#i_master_clk=ClockSignal(),
			#i_master_rst=ResetSignal(),

			# 16 bytes ciphertext - input to the MixColumnInv Module
			i_sm0=self.ctext[0],
			i_sm1=self.ctext[1],
			i_sm2=self.ctext[2],
			i_sm3=self.ctext[3],
			i_sm4=self.ctext[4],
			i_sm5=self.ctext[5],
			i_sm6=self.ctext[6],
			i_sm7=self.ctext[7],
			i_sm8=self.ctext[8],
			i_sm9=self.ctext[9],
			i_sm10=self.ctext[10],
			i_sm11=self.ctext[11],
			i_sm12=self.ctext[12],
			i_sm13=self.ctext[13],
			i_sm14=self.ctext[14],
			i_sm15=self.ctext[15],

			# 16 bytes ciphertext - output from the MixColumnInv Module
			o_recovered0=self.ptext[0],
			o_recovered1=self.ptext[1],
			o_recovered2=self.ptext[2],
			o_recovered3=self.ptext[3],
			o_recovered4=self.ptext[4],
			o_recovered5=self.ptext[5],
			o_recovered6=self.ptext[6],
			o_recovered7=self.ptext[7],
			o_recovered8=self.ptext[8],
			o_recovered9=self.ptext[9],
			o_recovered10=self.ptext[10],
			o_recovered11=self.ptext[11],
			o_recovered12=self.ptext[12],
			o_recovered13=self.ptext[13],
			o_recovered14=self.ptext[14],
			o_recovered15=self.ptext[15]
                     
		)
		"""

		# duplicate ptext on temp matrix
		for x in range(16):
			self.comb += self.temp[x].eq(self.ptext[x])
		"""	

		j = Instance("ShiftRowInv",
			#i_master_clk=ClockSignal(),
			#i_master_rst=ResetSignal(),

			# 16 bytes message - input to the ShiftRowInv Module
			i_sm0=self.temp[0],
			i_sm1=self.temp[1],
			i_sm2=self.temp[2],
			i_sm3=self.temp[3],
			i_sm4=self.temp[4],
			i_sm5=self.temp[5],
			i_sm6=self.temp[6],
			i_sm7=self.temp[7],
			i_sm8=self.temp[8],
			i_sm9=self.temp[9],
			i_sm10=self.temp[10],
			i_sm11=self.temp[11],
			i_sm12=self.temp[12],
			i_sm13=self.temp[13],
			i_sm14=self.temp[14],
			i_sm15=self.temp[15],
                     
			# 16 bytes recovered - output from the ShiftRowInv Module
			o_recovered0=self.ptext[0],
			o_recovered1=self.ptext[1],
			o_recovered2=self.ptext[2],
			o_recovered3=self.ptext[3],
			o_recovered4=self.ptext[4],
			o_recovered5=self.ptext[5],
			o_recovered6=self.ptext[6],
			o_recovered7=self.ptext[7],
			o_recovered8=self.ptext[8],
			o_recovered9=self.ptext[9],
			o_recovered10=self.ptext[10],
			o_recovered11=self.ptext[11],
			o_recovered12=self.ptext[12],
			o_recovered13=self.ptext[13],
			o_recovered14=self.ptext[14],
			o_recovered15=self.ptext[15]
                     
		)
		"""

		# duplicate ptext on temp1 matrix
		for y in range(16):
			self.comb += self.temp1[y].eq(self.ptext[y])
		"""	

		k = Instance("SubBytesInv",
			#i_master_clk=ClockSignal(),
			#i_master_rst=ResetSignal(),

			# 16 bytes message - input to the SubBytesInv Module
			i_sm0=self.temp1[0],
			i_sm1=self.temp1[1],
			i_sm2=self.temp1[2],
			i_sm3=self.temp1[3],
			i_sm4=self.temp1[4],
			i_sm5=self.temp1[5],
			i_sm6=self.temp1[6],
			i_sm7=self.temp1[7],
			i_sm8=self.temp1[8],
			i_sm9=self.temp1[9],
			i_sm10=self.temp1[10],
			i_sm11=self.temp1[11],
			i_sm12=self.temp1[12],
			i_sm13=self.temp1[13],
			i_sm14=self.temp1[14],
			i_sm15=self.temp1[15],
                     
			# 16 bytes ciphertext - output from the SubBytesInv Module
			o_recovered0=self.ptext[0],
			o_recovered1=self.ptext[1],
			o_recovered2=self.ptext[2],
			o_recovered3=self.ptext[3],
			o_recovered4=self.ptext[4],
			o_recovered5=self.ptext[5],
			o_recovered6=self.ptext[6],
			o_recovered7=self.ptext[7],
			o_recovered8=self.ptext[8],
			o_recovered9=self.ptext[9],
			o_recovered10=self.ptext[10],
			o_recovered11=self.ptext[11],
			o_recovered12=self.ptext[12],
			o_recovered13=self.ptext[13],
			o_recovered14=self.ptext[14],
			o_recovered15=self.ptext[15]
                     
		)
		"""

		# duplicate ptext on temp2 matrix
		for z in range(16):
			self.comb += self.temp2[y].eq(self.ptext[y])
		"""	

		l = Instance("AddRoundKey",
			#i_master_clk=ClockSignal(),
			#i_master_rst=ResetSignal(),

			# 16 bytes message - input to the AddRoundKey Module
			i_sm0=self.temp2[0],
			i_sm1=self.temp2[1],
			i_sm2=self.temp2[2],
			i_sm3=self.temp2[3],
			i_sm4=self.temp2[4],
			i_sm5=self.temp2[5],
			i_sm6=self.temp2[6],
			i_sm7=self.temp2[7],
			i_sm8=self.temp2[8],
			i_sm9=self.temp2[9],
			i_sm10=self.temp2[10],
			i_sm11=self.temp2[11],
			i_sm12=self.temp2[12],
			i_sm13=self.temp2[13],
			i_sm14=self.temp2[14],
			i_sm15=self.temp2[15],
                     
			# 16 bytes key - input to the AddRoundKey Module
			i_key0=self.key[0],
			i_key1=self.key[1],
			i_key2=self.key[2],
			i_key3=self.key[3],
			i_key4=self.key[4],
			i_key5=self.key[5],
			i_key6=self.key[6],
			i_key7=self.key[7],
			i_key8=self.key[8],
			i_key9=self.key[9],
			i_key10=self.key[10],
			i_key11=self.key[11],
			i_key12=self.key[12],
			i_key13=self.key[13],
			i_key14=self.key[14],
			i_key15=self.key[15],

			# 16 bytes ptext - output from the AddRoundKey Module
			o_ctext0=self.ptext[0],
			o_ctext1=self.ptext[1],
			o_ctext2=self.ptext[2],
			o_ctext3=self.ptext[3],
			o_ctext4=self.ptext[4],
			o_ctext5=self.ptext[5],
			o_ctext6=self.ptext[6],
			o_ctext7=self.ptext[7],
			o_ctext8=self.ptext[8],
			o_ctext9=self.ptext[9],
			o_ctext10=self.ptext[10],
			o_ctext11=self.ptext[11],
			o_ctext12=self.ptext[12],
			o_ctext13=self.ptext[13],
			o_ctext14=self.ptext[14],
			o_ctext15=self.ptext[15],
		)

		self.specials += i, j, k, l
		"""
        
		### specify the Module behavior below

'''
@module name: AddRoundKey
@description: Combines each byte of the state with a block of the round key using bitwise xor. 
              The expanded key bytes are never reused. Once the first 16 bytes of the state are XORed against the first 16 bytes of the
              expanded key, then the expanded key bytes are never used again.

'''
class AddRoundKey(Module):
	def __init__(self):
		self.sm = [Signal(8, name_override="sm{}".format(x)) for x in range(16)]# state matrix input port from the cipher Module
		self.key = [Signal(8, name_override="key{}".format(x)) for x in range(16)]# cipher key input port from the cipher Module
		self.ctext=[Signal(8, name_override="ctext{}".format(x)) for x in range(16)]# cipher text output port 

		self.io = set()
		self.io = self.io.union(self.sm)
		self.io = self.io.union(self.key)
		self.io = self.io.union(self.ctext)

		### specify the Module behavior below

		for a in range(16): # ctext = sm XOR key
		    self.comb += self.ctext[a].eq(self.sm[a] ^ self.key[a]) 


'''
@module name: ShiftRow
@description: The ShiftRows step operates on the rows of the state; it cyclically shifts the bytes in each row by a certain offset. 
              For AES, the first row is left unchanged. Each byte of the second row is shifted one to the left. Similarly, the third 
              and fourth rows are shifted by offsets of two and three respectively. In this way, each column of the output 
              state of the ShiftRows step is composed of bytes from each column of the input state. The importance of this step is to 
              avoid the columns being encrypted independently, in which case AES degenerates into four independent block ciphers. 

'''
class ShiftRow(Module): # ShiftRow submodule
	def __init__(self):
		self.sm = [Signal(8, name_override="sm{}".format(x)) for x in range(16)]# state matrix input port from the cipher Module
		self.ctext=[Signal(8, name_override="ctext{}".format(x)) for x in range(16)]# cipher text output port
		self.sm_shifted=[Signal(8, name_override="sm_shifted{}".format(x)) for x in range(16)]# shifted state matrix output
		self.temp = Signal(8)
		self.enc_en = Signal(1, name_override="enc_en")

		self.io = set()
		self.io = self.io.union(self.sm)
		self.io = self.io.union(self.sm_shifted)
		self.io = {self.enc_en}
		#self.io = self.io.union(self.ctext)

		### specify the Module behavior below

		# emit state matrix as is on the cipher text output port
		'''
		for b in range(16):
			self.comb += self.ctext[b].eq(self.sm[b])
		'''
		#perform row shifting
		'''
		self.temp = self.ctext[13]
		self.ctext[13] = self.ctext[1]
		self.ctext[1] = self.ctext[5]
		self.ctext[5] = self.ctext[9]
		self.ctext[9] = self.temp

		self.temp = self.ctext[10]
		self.ctext[10] = self.ctext[2]
		self.ctext[2] = self.temp

		self.temp = self.ctext[14]
		self.ctext[14] = self.ctext[6]
		self.ctext[6] = self.temp

		self.temp = self.ctext[7]
		self.ctext[7] = self.ctext[3]
		self.ctext[3] = self.ctext[15]
		self.ctext[15] = self.ctext[11]
		self.ctext[11] = self.temp
		'''
		#peform row shifted
		
		# row 1 - left as is
		'''
		self.sm_shifted[0]=self.ctext[0]
		'''
		
		
		self.comb +=[
                If(self.enc_en, 
                   
                # row 1 - leave as is
                self.sm_shifted[0].eq(self.sm[0]),
		self.sm_shifted[1].eq(self.sm[1]),
		self.sm_shifted[2].eq(self.sm[2]),
		self.sm_shifted[3].eq(self.sm[3]),
		
		# row 2 - shift once to the left
		self.sm_shifted[4].eq(self.sm[5]),
		self.sm_shifted[5].eq(self.sm[6]),
		self.sm_shifted[6].eq(self.sm[7]),
		self.sm_shifted[7].eq(self.sm[4]),
		
		# row 3 - shift twice to the left
		self.sm_shifted[8].eq(self.sm[10]),
		self.sm_shifted[9].eq(self.sm[11]),
		self.sm_shifted[10].eq(self.sm[8]),
		self.sm_shifted[11].eq(self.sm[9]),
		
		# row 3 - shift twice to the left
		self.sm_shifted[12].eq(self.sm[15]),
		self.sm_shifted[13].eq(self.sm[12]),
		self.sm_shifted[14].eq(self.sm[13]),
		self.sm_shifted[15].eq(self.sm[14])
		).Else(
                    
                self.sm_shifted[0].eq(self.sm[0]),
                self.sm_shifted[1].eq(self.sm[1]),
                self.sm_shifted[2].eq(self.sm[2]),
                self.sm_shifted[3].eq(self.sm[3]),
        
                
                # row 2 - shift once to the left
                self.sm_shifted[4].eq(self.sm[5]),
                self.sm_shifted[5].eq(self.sm[6]),
                self.sm_shifted[6].eq(self.sm[7]),
                self.sm_shifted[7].eq(self.sm[4]),
                
                # row 3 - shift twice to the left
                self.sm_shifted[8].eq(self.sm[10]),
                self.sm_shifted[9].eq(self.sm[11]),
                self.sm_shifted[10].eq(self.sm[8]),
                self.sm_shifted[11].eq(self.sm[9]),
                
                self.sm_shifted[12].eq(self.sm[15]),
                self.sm_shifted[13].eq(self.sm[12]),
                self.sm_shifted[14].eq(self.sm[13]),
                self.sm_shifted[15].eq(self.sm[14]))]

def check_ShiftRow(dut,sm):
        for i in range(16):# loop to load testbench inputs onto input ports of our AESCipher core
                yield dut.sm[i].eq(sm[i])# load the ith byte of the plain text
        yield# wait a clock cycle  

class ShiftRowInv(Module): # ShiftRowInv submodule
	def __init__(self):
		self.sm = [Signal(8, name_override="sm{}".format(x)) for x in range(16)]# state matrix input port from the top level Module
		self.recovered=[Signal(8, name_override="recovered{}".format(x)) for x in range(16)]# recovered text output port
		self.temp = Signal(8)

		self.io = set()
		self.io = self.io.union(self.sm)
		self.io = self.io.union(self.recovered)

		### specify the Module behavior below

		# emit state matrix as is on the recovered text output port
		for x in range(16):
			self.comb += self.recovered[x].eq(self.sm[x]) 

		#perform row shifting
		self.temp = self.recovered[1]
		self.recovered[1] = self.recovered[13]
		self.recovered[13] = self.recovered[9]
		self.recovered[9] = self.recovered[5]
		self.recovered[5] = self.temp

		self.temp = self.recovered[2]
		self.recovered[2] = self.recovered[10]
		self.recovered[10] = self.temp

		self.temp = self.recovered[6]
		self.recovered[6] = self.recovered[14]
		self.recovered[14] = self.temp

		self.temp = self.recovered[15]
		self.recovered[15] = self.recovered[3]
		self.recovered[3] = self.recovered[7]
		self.recovered[7] = self.recovered[11]
		self.recovered[11] = self.temp

'''
@module name: SubBytes
@description: During encryption, each value of the state is replaced with the corresponding sbox value.

'''

class SubBytes(Module): # SubBytes submodule
	def __init__(self):
		#self.sm = [Signal(8, name_override="sm{}".format(x)) for x in range(16)]# state matrix input port from the cipher Module
		#self.ctext=[Signal(8, name_override="ctext{}".format(x)) for x in range(16)]# cipher text output port
		#self.sm_in=[Signal(8, name_override="sm_in{}".format(x)) for x in range(16)]# cipher text output port
		self.sm_out=Signal(8)#[Signal(8, name_override="sm_out{}".format(x)) for x in range(16)]# cipher text output port
		#self.temp=Signal(8)

		self.io = set()
		#self.io = self.io.union(self.sm_in)
		self.io = {self.sm_out}

		# instantiate a memory block containing 256 words, each of width 8 bits and initialise it with sbox matrix values
		self.specials.sboxmem = Memory(8, 256, init=[
                0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76,
                0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0,
                0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15,
                0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75,
                0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84,
                0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf,
                0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8,
                0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2,
                0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73,
                0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb,
                0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79,
                0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08,
                0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a,
                0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e,
                0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf,
                0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16]
                )
		self.rdport = self.sboxmem.get_port(async_read=True)
		self.specials += self.rdport
		self.ios = {self.rdport.adr}
		self.ios = {self.rdport.dat_r}
		
		### Specify the Module behavior below	
		
		# perform byte substitution
		self.comb += self.sm_out.eq(self.rdport.dat_r)
                    
def check_SubBytes(dut,sm):
        for i in range(16):# loop to load testbench inputs onto input ports of our AESCipher core
                yield dut.sm_in[i].eq(sm[i])# load the ith byte of the plain text
                yield
                yield dut.rdport.adr.eq(dut.sm_in[i])
                #yield
                    
class SubBytesInv(Module): # SubBytesInv submodule
	def __init__(self):
		self.sm = [Signal(8, name_override="sm{}".format(x)) for x in range(16)]# state matrix input port from the cipher Module
		self.recovered=[Signal(8, name_override="recovered{}".format(x)) for x in range(16)]# recovered text output port

		self.io = set()
		self.io = self.io.union(self.sm)
		self.io = self.io.union(self.recovered)

		# instantiate a memory block containing 256 words, each of width 8 bits and initialise it with array values
		# inverse sbox
		self.specials.invsboxmem =invsboxmem = Memory(8, 256, init=
					   [
		0x52, 0x09, 0x6a, 0xd5, 0x30, 0x36, 0xa5, 0x38, 0xbf, 0x40, 0xa3, 0x9e, 0x81, 0xf3, 0xd7, 0xfb,
		0x7c, 0xe3, 0x39, 0x82, 0x9b, 0x2f, 0xff, 0x87, 0x34, 0x8e, 0x43, 0x44, 0xc4, 0xde, 0xe9, 0xcb,
		0x54, 0x7b, 0x94, 0x32, 0xa6, 0xc2, 0x23, 0x3d, 0xee, 0x4c, 0x95, 0x0b, 0x42, 0xfa, 0xc3, 0x4e,
		0x08, 0x2e, 0xa1, 0x66, 0x28, 0xd9, 0x24, 0xb2, 0x76, 0x5b, 0xa2, 0x49, 0x6d, 0x8b, 0xd1, 0x25,
		0x72, 0xf8, 0xf6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xd4, 0xa4, 0x5c, 0xcc, 0x5d, 0x65, 0xb6, 0x92,
		0x6c, 0x70, 0x48, 0x50, 0xfd, 0xed, 0xb9, 0xda, 0x5e, 0x15, 0x46, 0x57, 0xa7, 0x8d, 0x9d, 0x84,
		0x90, 0xd8, 0xab, 0x00, 0x8c, 0xbc, 0xd3, 0x0a, 0xf7, 0xe4, 0x58, 0x05, 0xb8, 0xb3, 0x45, 0x06,
		0xd0, 0x2c, 0x1e, 0x8f, 0xca, 0x3f, 0x0f, 0x02, 0xc1, 0xaf, 0xbd, 0x03, 0x01, 0x13, 0x8a, 0x6b,
		0x3a, 0x91, 0x11, 0x41, 0x4f, 0x67, 0xdc, 0xea, 0x97, 0xf2, 0xcf, 0xce, 0xf0, 0xb4, 0xe6, 0x73,
		0x96, 0xac, 0x74, 0x22, 0xe7, 0xad, 0x35, 0x85, 0xe2, 0xf9, 0x37, 0xe8, 0x1c, 0x75, 0xdf, 0x6e,
		0x47, 0xf1, 0x1a, 0x71, 0x1d, 0x29, 0xc5, 0x89, 0x6f, 0xb7, 0x62, 0x0e, 0xaa, 0x18, 0xbe, 0x1b,
		0xfc, 0x56, 0x3e, 0x4b, 0xc6, 0xd2, 0x79, 0x20, 0x9a, 0xdb, 0xc0, 0xfe, 0x78, 0xcd, 0x5a, 0xf4,
		0x1f, 0xdd, 0xa8, 0x33, 0x88, 0x07, 0xc7, 0x31, 0xb1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xec, 0x5f,
		0x60, 0x51, 0x7f, 0xa9, 0x19, 0xb5, 0x4a, 0x0d, 0x2d, 0xe5, 0x7a, 0x9f, 0x93, 0xc9, 0x9c, 0xef,
		0xa0, 0xe0, 0x3b, 0x4d, 0xae, 0x2a, 0xf5, 0xb0, 0xc8, 0xeb, 0xbb, 0x3c, 0x83, 0x53, 0x99, 0x61,
		0x17, 0x2b, 0x04, 0x7e, 0xba, 0x77, 0xd6, 0x26, 0xe1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0c, 0x7d])
                
		### specify the Module behavior below
		
		# perform inverse byte substitution
		self.rdport = self.invsboxmem.get_port()
		self.specials += self.rdport
		self.ios = {self.rdport.adr}
		for x in range(len(self.sm)):
                    self.comb += [self.rdport.adr.eq(x), # set the read address to x
                                  self.recovered[x].eq(self.rdport.dat_r)] # read memory at x and write it to ctext at x

class MixColumn(Module): # MixColumn submodule
	def __init__(self):
		self.sm = [Signal(8, name_override="sm{}".format(x)) for x in range(16)]# state matrix input port from cipher Module
		self.ctext = [Signal(8, name="ctext{}".format(x)) for x in range(16)]# cipher text output port
		self.column = [Signal(8, name="col{}".format(x)) for x in range(4)] # to hold a column of stateMatrix
		self.temp = [Signal(8, name="temp{}".format(x)) for x in range(4)] # to hold a column of stateMatrix temporarily
		self.sm_out = [Signal(8, name="sm_out{}".format(x)) for x in range(16)]# cipher text output port
		self.mult20 = Signal(8)
		self.mult21 = Signal(8)
		self.mult22 = Signal(8)
		self.mult23 = Signal(8)
		self.mult30 = Signal(8)
		self.mult31 = Signal(8)
		self.mult32 = Signal(8)
		self.mult33 = Signal(8)

		# instantiate a memory block containing 256 words, each of width 8 bits and initialise it with array values
		# Multiplication by 2 - LUT, in GF(2^8)
		self.specials.mult2 =mult2 = Memory(8, 256, init=[
		0x00, 0x02, 0x04, 0x06, 0x08, 0x0a, 0x0c, 0x0e, 0x10, 0x12, 0x14, 0x16, 0x18, 0x1a, 0x1c, 0x1e,
		0x20, 0x22, 0x24, 0x26, 0x28, 0x2a, 0x2c, 0x2e, 0x30, 0x32, 0x34, 0x36, 0x38, 0x3a, 0x3c, 0x3e,
		0x40, 0x42, 0x44, 0x46, 0x48, 0x4a, 0x4c, 0x4e, 0x50, 0x52, 0x54, 0x56, 0x58, 0x5a, 0x5c, 0x5e,
		0x60, 0x62, 0x64, 0x66, 0x68, 0x6a, 0x6c, 0x6e, 0x70, 0x72, 0x74, 0x76, 0x78, 0x7a, 0x7c, 0x7e,
		0x80, 0x82, 0x84, 0x86, 0x88, 0x8a, 0x8c, 0x8e, 0x90, 0x92, 0x94, 0x96, 0x98, 0x9a, 0x9c, 0x9e,
		0xa0, 0xa2, 0xa4, 0xa6, 0xa8, 0xaa, 0xac, 0xae, 0xb0, 0xb2, 0xb4, 0xb6, 0xb8, 0xba, 0xbc, 0xbe,
		0xc0, 0xc2, 0xc4, 0xc6, 0xc8, 0xca, 0xcc, 0xce, 0xd0, 0xd2, 0xd4, 0xd6, 0xd8, 0xda, 0xdc, 0xde,
		0xe0, 0xe2, 0xe4, 0xe6, 0xe8, 0xea, 0xec, 0xee, 0xf0, 0xf2, 0xf4, 0xf6, 0xf8, 0xfa, 0xfc, 0xfe,
		0x1b, 0x19, 0x1f, 0x1d, 0x13, 0x11, 0x17, 0x15, 0x0b, 0x09, 0x0f, 0x0d, 0x03, 0x01, 0x07, 0x05,
		0x3b, 0x39, 0x3f, 0x3d, 0x33, 0x31, 0x37, 0x35, 0x2b, 0x29, 0x2f, 0x2d, 0x23, 0x21, 0x27, 0x25,
		0x5b, 0x59, 0x5f, 0x5d, 0x53, 0x51, 0x57, 0x55, 0x4b, 0x49, 0x4f, 0x4d, 0x43, 0x41, 0x47, 0x45,
		0x7b, 0x79, 0x7f, 0x7d, 0x73, 0x71, 0x77, 0x75, 0x6b, 0x69, 0x6f, 0x6d, 0x63, 0x61, 0x67, 0x65,
		0x9b, 0x99, 0x9f, 0x9d, 0x93, 0x91, 0x97, 0x95, 0x8b, 0x89, 0x8f, 0x8d, 0x83, 0x81, 0x87, 0x85,
		0xbb, 0xb9, 0xbf, 0xbd, 0xb3, 0xb1, 0xb7, 0xb5, 0xab, 0xa9, 0xaf, 0xad, 0xa3, 0xa1, 0xa7, 0xa5,
		0xdb, 0xd9, 0xdf, 0xdd, 0xd3, 0xd1, 0xd7, 0xd5, 0xcb, 0xc9, 0xcf, 0xcd, 0xc3, 0xc1, 0xc7, 0xc5,
		0xfb, 0xf9, 0xff, 0xfd, 0xf3, 0xf1, 0xf7, 0xf5, 0xeb, 0xe9, 0xef, 0xed, 0xe3, 0xe1, 0xe7, 0xe5]
		)
					   
		# Multiplication by 3 - LUT, in GF(2^8)
		self.specials.mult3 =mult3 = Memory(8, 256, init=[
		0x00, 0x03, 0x06, 0x05, 0x0c, 0x0f, 0x0a, 0x09, 0x18, 0x1b, 0x1e, 0x1d, 0x14, 0x17, 0x12, 0x11,
		0x30, 0x33, 0x36, 0x35, 0x3c, 0x3f, 0x3a, 0x39, 0x28, 0x2b, 0x2e, 0x2d, 0x24, 0x27, 0x22, 0x21,
		0x60, 0x63, 0x66, 0x65, 0x6c, 0x6f, 0x6a, 0x69, 0x78, 0x7b, 0x7e, 0x7d, 0x74, 0x77, 0x72, 0x71,
		0x50, 0x53, 0x56, 0x55, 0x5c, 0x5f, 0x5a, 0x59, 0x48, 0x4b, 0x4e, 0x4d, 0x44, 0x47, 0x42, 0x41,
		0xc0, 0xc3, 0xc6, 0xc5, 0xcc, 0xcf, 0xca, 0xc9, 0xd8, 0xdb, 0xde, 0xdd, 0xd4, 0xd7, 0xd2, 0xd1,
		0xf0, 0xf3, 0xf6, 0xf5, 0xfc, 0xff, 0xfa, 0xf9, 0xe8, 0xeb, 0xee, 0xed, 0xe4, 0xe7, 0xe2, 0xe1,
		0xa0, 0xa3, 0xa6, 0xa5, 0xac, 0xaf, 0xaa, 0xa9, 0xb8, 0xbb, 0xbe, 0xbd, 0xb4, 0xb7, 0xb2, 0xb1,
		0x90, 0x93, 0x96, 0x95, 0x9c, 0x9f, 0x9a, 0x99, 0x88, 0x8b, 0x8e, 0x8d, 0x84, 0x87, 0x82, 0x81,
		0x9b, 0x98, 0x9d, 0x9e, 0x97, 0x94, 0x91, 0x92, 0x83, 0x80, 0x85, 0x86, 0x8f, 0x8c, 0x89, 0x8a,
		0xab, 0xa8, 0xad, 0xae, 0xa7, 0xa4, 0xa1, 0xa2, 0xb3, 0xb0, 0xb5, 0xb6, 0xbf, 0xbc, 0xb9, 0xba,
		0xfb, 0xf8, 0xfd, 0xfe, 0xf7, 0xf4, 0xf1, 0xf2, 0xe3, 0xe0, 0xe5, 0xe6, 0xef, 0xec, 0xe9, 0xea,
		0xcb, 0xc8, 0xcd, 0xce, 0xc7, 0xc4, 0xc1, 0xc2, 0xd3, 0xd0, 0xd5, 0xd6, 0xdf, 0xdc, 0xd9, 0xda,
		0x5b, 0x58, 0x5d, 0x5e, 0x57, 0x54, 0x51, 0x52, 0x43, 0x40, 0x45, 0x46, 0x4f, 0x4c, 0x49, 0x4a,
		0x6b, 0x68, 0x6d, 0x6e, 0x67, 0x64, 0x61, 0x62, 0x73, 0x70, 0x75, 0x76, 0x7f, 0x7c, 0x79, 0x7a,
		0x3b, 0x38, 0x3d, 0x3e, 0x37, 0x34, 0x31, 0x32, 0x23, 0x20, 0x25, 0x26, 0x2f, 0x2c, 0x29, 0x2a,
		0x0b, 0x08, 0x0d, 0x0e, 0x07, 0x04, 0x01, 0x02, 0x13, 0x10, 0x15, 0x16, 0x1f, 0x1c, 0x19, 0x1a]
		)

		#self.io = set()
		#self.i = self.sm
		#self.o = self.ctext
		self.io = set()
		self.io = self.io.union(self.sm)
		self.io = self.io.union(self.ctext)
		self.mult2rdport = self.mult2.get_port(async_read=True)
		self.specials += self.mult2rdport
		self.mult3rdport = self.mult3.get_port(async_read=True)
		self.specials += self.mult3rdport
                #self.ios = {self.rdport.adr}
                #for x in range(len(self.sm)):
                #    self.comb += [self.rdport.adr.eq(x), # set the read address to x
                #                  self.recovered[x].eq(self.rdport.dat_r)] # read memory at x and write it to ctext at x

		### specify the Module behavior below
		# mix column method
		# 02 03 01 01
		# 01 02 03 01
		# 01 01 02 03
		# 03 01 01 02

		pos = 0 #to hold position in the column
		count = 0
		tmp = 0

		for i in range(16):
			count = i+1
			self.comb += self.temp[tmp].eq(self.sm[i]) #build a temporary column of 4 values in temp                     

			if count % 4 == 0: #check whether the column holds 4 elements
				# perform mixColumn computations on the column
					       
				self.sync += [self.mult2rdport.adr.eq(self.temp[0]),
                                              self.mult20.eq(self.mult2rdport.dat_r)] 
                                # perform lookup of the mult2 table at index temp[0] and store result in mult20
                                
				self.sync += [self.mult2rdport.adr.eq(self.temp[1]),
                                              self.mult21.eq(self.mult2rdport.dat_r)] 
                                # perform lookup of the mult2 table at index temp[1] and store result in mult21 
                                
				self.sync += [self.mult2rdport.adr.eq(self.temp[2]),
                                              self.mult22.eq(self.mult2rdport.dat_r)] 
                                # perform lookup of the mult2 table at index temp[2] and store result in mult22  
                                
				self.sync += [self.mult2rdport.adr.eq(self.temp[3]),
                                              self.mult23.eq(self.mult2rdport.dat_r)] 
                                # perform lookup of the mult2 table at index temp[3] and store result in mult23  
                                
				self.sync += [self.mult3rdport.adr.eq(self.temp[0]),
                                              self.mult30.eq(self.mult3rdport.dat_r)] 
                                # perform lookup of the mult3 table at index temp[0] and store result in mult30  
                                
				self.sync += [self.mult3rdport.adr.eq(self.temp[1]),
                                              self.mult31.eq(self.mult3rdport.dat_r)] 
                                # perform lookup of the mult3 table at index temp[1] and store result in mult31
                                
				self.sync += [self.mult3rdport.adr.eq(self.temp[2]),
                                              self.mult32.eq(self.mult3rdport.dat_r)] 
                                # perform lookup of the mult3 table at index temp[2] and store result in mult32  
                                
				self.sync += [self.mult3rdport.adr.eq(self.temp[3]),
                                              self.mult33.eq(self.mult3rdport.dat_r)] 
                                # perform lookup of the mult3 table at index temp[3] and store result in mult33  
                                
				self.comb += self.column[0].eq(self.mult20 ^ self.mult31 ^ self.temp[2] ^ self.temp[3])
				self.comb += self.column[1].eq(self.temp[0] ^ self.mult21 ^ self.mult32 ^ self.temp[3])
				self.comb += self.column[2].eq(self.temp[0] ^ self.temp[1] ^ self.mult22 ^ self.mult33)
				self.comb += self.column[3].eq(self.mult30 ^ self.temp[1] ^ self.temp[2] ^ self.mult23)

				#update stateMatrix with new column values
				for j in range(count-4,count):
					self.comb += self.sm_out[j].eq(self.column[pos])
					pos += 1 #go to next element

				pos = 0 #reset position
				tmp = 0 #reset tmp

			else:
				tmp += 1 #go to next element in temp

def check_MixColumn(dut,sm):
        for i in range(16):# loop to load testbench inputs onto input ports of our AESCipher core
                yield dut.sm[i].eq(sm[i])# load the ith byte of the plain text
        for i in range(32):# loop to load testbench inputs onto input ports of our AESCipher core
                yield #dut.sm[i].eq(sm[i])# load the ith byte of the plain text                
        #yield# wait a clock cycle  


class MixColumnInv(Module): # MixColumnInv submodule
	def __init__(self):
		self.sm = [Signal(8, name_override="sm{}".format(x)) for x in range(16)]# state matrix input port from the top level Module
		self.recovered = [Signal(8, name="rec{}".format(x)) for x in range(16)]# recovered text output port
		self.column = [Signal(8, name="col{}".format(x)) for x in range(4)] # to hold a column of stateMatrix
		self.temp = [Signal(8, name="temp{}".format(x)) for x in range(4)] # to hold a column of stateMatrix temporarily
		self.mult90 = Signal(8)
		self.mult91 = Signal(8)
		self.mult92 = Signal(8)
		self.mult93 = Signal(8)
		self.multB0 = Signal(8)
		self.multB1 = Signal(8)
		self.multB2 = Signal(8)
		self.multB3 = Signal(8)
		self.multD0 = Signal(8)
		self.multD1 = Signal(8)
		self.multD2 = Signal(8)
		self.multD3 = Signal(8)
		self.multE0 = Signal(8)
		self.multE1 = Signal(8)
		self.multE2 = Signal(8)
		self.multE3 = Signal(8)

		# instantiate a memory block containing 256 words, each of width 8 bits and initialise it with array values
		# Multiplication by 9 - LUT, in GF(2^8)
		self.specials.mult9 =mult9 = Memory(8, 256, init=[
		0x00, 0x09, 0x12, 0x1b, 0x24, 0x2d, 0x36, 0x3f, 0x48, 0x41, 0x5a, 0x53, 0x6c, 0x65, 0x7e, 0x77,
		0x90, 0x99, 0x82, 0x8b, 0xb4, 0xbd, 0xa6, 0xaf, 0xd8, 0xd1, 0xca, 0xc3, 0xfc, 0xf5, 0xee, 0xe7,
		0x3b, 0x32, 0x29, 0x20, 0x1f, 0x16, 0x0d, 0x04, 0x73, 0x7a, 0x61, 0x68, 0x57, 0x5e, 0x45, 0x4c,
		0xab, 0xa2, 0xb9, 0xb0, 0x8f, 0x86, 0x9d, 0x94, 0xe3, 0xea, 0xf1, 0xf8, 0xc7, 0xce, 0xd5, 0xdc,
		0x76, 0x7f, 0x64, 0x6d, 0x52, 0x5b, 0x40, 0x49, 0x3e, 0x37, 0x2c, 0x25, 0x1a, 0x13, 0x08, 0x01,
		0xe6, 0xef, 0xf4, 0xfd, 0xc2, 0xcb, 0xd0, 0xd9, 0xae, 0xa7, 0xbc, 0xb5, 0x8a, 0x83, 0x98, 0x91,
		0x4d, 0x44, 0x5f, 0x56, 0x69, 0x60, 0x7b, 0x72, 0x05, 0x0c, 0x17, 0x1e, 0x21, 0x28, 0x33, 0x3a,
		0xdd, 0xd4, 0xcf, 0xc6, 0xf9, 0xf0, 0xeb, 0xe2, 0x95, 0x9c, 0x87, 0x8e, 0xb1, 0xb8, 0xa3, 0xaa,
		0xec, 0xe5, 0xfe, 0xf7, 0xc8, 0xc1, 0xda, 0xd3, 0xa4, 0xad, 0xb6, 0xbf, 0x80, 0x89, 0x92, 0x9b,
		0x7c, 0x75, 0x6e, 0x67, 0x58, 0x51, 0x4a, 0x43, 0x34, 0x3d, 0x26, 0x2f, 0x10, 0x19, 0x02, 0x0b,
		0xd7, 0xde, 0xc5, 0xcc, 0xf3, 0xfa, 0xe1, 0xe8, 0x9f, 0x96, 0x8d, 0x84, 0xbb, 0xb2, 0xa9, 0xa0,
		0x47, 0x4e, 0x55, 0x5c, 0x63, 0x6a, 0x71, 0x78, 0x0f, 0x06, 0x1d, 0x14, 0x2b, 0x22, 0x39, 0x30,
		0x9a, 0x93, 0x88, 0x81, 0xbe, 0xb7, 0xac, 0xa5, 0xd2, 0xdb, 0xc0, 0xc9, 0xf6, 0xff, 0xe4, 0xed,
		0x0a, 0x03, 0x18, 0x11, 0x2e, 0x27, 0x3c, 0x35, 0x42, 0x4b, 0x50, 0x59, 0x66, 0x6f, 0x74, 0x7d,
		0xa1, 0xa8, 0xb3, 0xba, 0x85, 0x8c, 0x97, 0x9e, 0xe9, 0xe0, 0xfb, 0xf2, 0xcd, 0xc4, 0xdf, 0xd6,
		0x31, 0x38, 0x23, 0x2a, 0x15, 0x1c, 0x07, 0x0e, 0x79, 0x70, 0x6b, 0x62, 0x5d, 0x54, 0x4f, 0x46]
		)

		# Multiplication by B - LUT, in GF(2^8)
		self.specials.multB =multB = Memory(8, 256, init=[
		0x00, 0x0b, 0x16, 0x1d, 0x2c, 0x27, 0x3a, 0x31, 0x58, 0x53, 0x4e, 0x45, 0x74, 0x7f, 0x62, 0x69,
		0xb0, 0xbb, 0xa6, 0xad, 0x9c, 0x97, 0x8a, 0x81, 0xe8, 0xe3, 0xfe, 0xf5, 0xc4, 0xcf, 0xd2, 0xd9,
		0x7b, 0x70, 0x6d, 0x66, 0x57, 0x5c, 0x41, 0x4a, 0x23, 0x28, 0x35, 0x3e, 0x0f, 0x04, 0x19, 0x12,
		0xcb, 0xc0, 0xdd, 0xd6, 0xe7, 0xec, 0xf1, 0xfa, 0x93, 0x98, 0x85, 0x8e, 0xbf, 0xb4, 0xa9, 0xa2,
		0xf6, 0xfd, 0xe0, 0xeb, 0xda, 0xd1, 0xcc, 0xc7, 0xae, 0xa5, 0xb8, 0xb3, 0x82, 0x89, 0x94, 0x9f,
		0x46, 0x4d, 0x50, 0x5b, 0x6a, 0x61, 0x7c, 0x77, 0x1e, 0x15, 0x08, 0x03, 0x32, 0x39, 0x24, 0x2f,
		0x8d, 0x86, 0x9b, 0x90, 0xa1, 0xaa, 0xb7, 0xbc, 0xd5, 0xde, 0xc3, 0xc8, 0xf9, 0xf2, 0xef, 0xe4,
		0x3d, 0x36, 0x2b, 0x20, 0x11, 0x1a, 0x07, 0x0c, 0x65, 0x6e, 0x73, 0x78, 0x49, 0x42, 0x5f, 0x54,
		0xf7, 0xfc, 0xe1, 0xea, 0xdb, 0xd0, 0xcd, 0xc6, 0xaf, 0xa4, 0xb9, 0xb2, 0x83, 0x88, 0x95, 0x9e,
		0x47, 0x4c, 0x51, 0x5a, 0x6b, 0x60, 0x7d, 0x76, 0x1f, 0x14, 0x09, 0x02, 0x33, 0x38, 0x25, 0x2e,
		0x8c, 0x87, 0x9a, 0x91, 0xa0, 0xab, 0xb6, 0xbd, 0xd4, 0xdf, 0xc2, 0xc9, 0xf8, 0xf3, 0xee, 0xe5,
		0x3c, 0x37, 0x2a, 0x21, 0x10, 0x1b, 0x06, 0x0d, 0x64, 0x6f, 0x72, 0x79, 0x48, 0x43, 0x5e, 0x55,
		0x01, 0x0a, 0x17, 0x1c, 0x2d, 0x26, 0x3b, 0x30, 0x59, 0x52, 0x4f, 0x44, 0x75, 0x7e, 0x63, 0x68,
		0xb1, 0xba, 0xa7, 0xac, 0x9d, 0x96, 0x8b, 0x80, 0xe9, 0xe2, 0xff, 0xf4, 0xc5, 0xce, 0xd3, 0xd8,
		0x7a, 0x71, 0x6c, 0x67, 0x56, 0x5d, 0x40, 0x4b, 0x22, 0x29, 0x34, 0x3f, 0x0e, 0x05, 0x18, 0x13,
		0xca, 0xc1, 0xdc, 0xd7, 0xe6, 0xed, 0xf0, 0xfb, 0x92, 0x99, 0x84, 0x8f, 0xbe, 0xb5, 0xa8, 0xa3]
		)

		# Multiplication by D - LUT, in GF(2^8)
		self.specials.multD =multD = Memory(8, 256, init=[
		0x00, 0x0d, 0x1a, 0x17, 0x34, 0x39, 0x2e, 0x23, 0x68, 0x65, 0x72, 0x7f, 0x5c, 0x51, 0x46, 0x4b,
		0xd0, 0xdd, 0xca, 0xc7, 0xe4, 0xe9, 0xfe, 0xf3, 0xb8, 0xb5, 0xa2, 0xaf, 0x8c, 0x81, 0x96, 0x9b,
		0xbb, 0xb6, 0xa1, 0xac, 0x8f, 0x82, 0x95, 0x98, 0xd3, 0xde, 0xc9, 0xc4, 0xe7, 0xea, 0xfd, 0xf0,
		0x6b, 0x66, 0x71, 0x7c, 0x5f, 0x52, 0x45, 0x48, 0x03, 0x0e, 0x19, 0x14, 0x37, 0x3a, 0x2d, 0x20,
		0x6d, 0x60, 0x77, 0x7a, 0x59, 0x54, 0x43, 0x4e, 0x05, 0x08, 0x1f, 0x12, 0x31, 0x3c, 0x2b, 0x26,
		0xbd, 0xb0, 0xa7, 0xaa, 0x89, 0x84, 0x93, 0x9e, 0xd5, 0xd8, 0xcf, 0xc2, 0xe1, 0xec, 0xfb, 0xf6,
		0xd6, 0xdb, 0xcc, 0xc1, 0xe2, 0xef, 0xf8, 0xf5, 0xbe, 0xb3, 0xa4, 0xa9, 0x8a, 0x87, 0x90, 0x9d,
		0x06, 0x0b, 0x1c, 0x11, 0x32, 0x3f, 0x28, 0x25, 0x6e, 0x63, 0x74, 0x79, 0x5a, 0x57, 0x40, 0x4d,
		0xda, 0xd7, 0xc0, 0xcd, 0xee, 0xe3, 0xf4, 0xf9, 0xb2, 0xbf, 0xa8, 0xa5, 0x86, 0x8b, 0x9c, 0x91,
		0x0a, 0x07, 0x10, 0x1d, 0x3e, 0x33, 0x24, 0x29, 0x62, 0x6f, 0x78, 0x75, 0x56, 0x5b, 0x4c, 0x41,
		0x61, 0x6c, 0x7b, 0x76, 0x55, 0x58, 0x4f, 0x42, 0x09, 0x04, 0x13, 0x1e, 0x3d, 0x30, 0x27, 0x2a,
		0xb1, 0xbc, 0xab, 0xa6, 0x85, 0x88, 0x9f, 0x92, 0xd9, 0xd4, 0xc3, 0xce, 0xed, 0xe0, 0xf7, 0xfa,
		0xb7, 0xba, 0xad, 0xa0, 0x83, 0x8e, 0x99, 0x94, 0xdf, 0xd2, 0xc5, 0xc8, 0xeb, 0xe6, 0xf1, 0xfc,
		0x67, 0x6a, 0x7d, 0x70, 0x53, 0x5e, 0x49, 0x44, 0x0f, 0x02, 0x15, 0x18, 0x3b, 0x36, 0x21, 0x2c,
		0x0c, 0x01, 0x16, 0x1b, 0x38, 0x35, 0x22, 0x2f, 0x64, 0x69, 0x7e, 0x73, 0x50, 0x5d, 0x4a, 0x47,
		0xdc, 0xd1, 0xc6, 0xcb, 0xe8, 0xe5, 0xf2, 0xff, 0xb4, 0xb9, 0xae, 0xa3, 0x80, 0x8d, 0x9a, 0x97]
		)

		# Multiplication by E - LUT, in GF(2^8)
		self.specials.multE =multE = Memory(8, 256, init=[
		0x00, 0x0e, 0x1c, 0x12, 0x38, 0x36, 0x24, 0x2a, 0x70, 0x7e, 0x6c, 0x62, 0x48, 0x46, 0x54, 0x5a,
		0xe0, 0xee, 0xfc, 0xf2, 0xd8, 0xd6, 0xc4, 0xca, 0x90, 0x9e, 0x8c, 0x82, 0xa8, 0xa6, 0xb4, 0xba,
		0xdb, 0xd5, 0xc7, 0xc9, 0xe3, 0xed, 0xff, 0xf1, 0xab, 0xa5, 0xb7, 0xb9, 0x93, 0x9d, 0x8f, 0x81,
		0x3b, 0x35, 0x27, 0x29, 0x03, 0x0d, 0x1f, 0x11, 0x4b, 0x45, 0x57, 0x59, 0x73, 0x7d, 0x6f, 0x61,
		0xad, 0xa3, 0xb1, 0xbf, 0x95, 0x9b, 0x89, 0x87, 0xdd, 0xd3, 0xc1, 0xcf, 0xe5, 0xeb, 0xf9, 0xf7,
		0x4d, 0x43, 0x51, 0x5f, 0x75, 0x7b, 0x69, 0x67, 0x3d, 0x33, 0x21, 0x2f, 0x05, 0x0b, 0x19, 0x17,
		0x76, 0x78, 0x6a, 0x64, 0x4e, 0x40, 0x52, 0x5c, 0x06, 0x08, 0x1a, 0x14, 0x3e, 0x30, 0x22, 0x2c,
		0x96, 0x98, 0x8a, 0x84, 0xae, 0xa0, 0xb2, 0xbc, 0xe6, 0xe8, 0xfa, 0xf4, 0xde, 0xd0, 0xc2, 0xcc,
		0x41, 0x4f, 0x5d, 0x53, 0x79, 0x77, 0x65, 0x6b, 0x31, 0x3f, 0x2d, 0x23, 0x09, 0x07, 0x15, 0x1b,
		0xa1, 0xaf, 0xbd, 0xb3, 0x99, 0x97, 0x85, 0x8b, 0xd1, 0xdf, 0xcd, 0xc3, 0xe9, 0xe7, 0xf5, 0xfb,
		0x9a, 0x94, 0x86, 0x88, 0xa2, 0xac, 0xbe, 0xb0, 0xea, 0xe4, 0xf6, 0xf8, 0xd2, 0xdc, 0xce, 0xc0,
		0x7a, 0x74, 0x66, 0x68, 0x42, 0x4c, 0x5e, 0x50, 0x0a, 0x04, 0x16, 0x18, 0x32, 0x3c, 0x2e, 0x20,
		0xec, 0xe2, 0xf0, 0xfe, 0xd4, 0xda, 0xc8, 0xc6, 0x9c, 0x92, 0x80, 0x8e, 0xa4, 0xaa, 0xb8, 0xb6,
		0x0c, 0x02, 0x10, 0x1e, 0x34, 0x3a, 0x28, 0x26, 0x7c, 0x72, 0x60, 0x6e, 0x44, 0x4a, 0x58, 0x56,
		0x37, 0x39, 0x2b, 0x25, 0x0f, 0x01, 0x13, 0x1d, 0x47, 0x49, 0x5b, 0x55, 0x7f, 0x71, 0x63, 0x6d,
		0xd7, 0xd9, 0xcb, 0xc5, 0xef, 0xe1, 0xf3, 0xfd, 0xa7, 0xa9, 0xbb, 0xb5, 0x9f, 0x91, 0x83, 0x8d]
		)

		#self.io = set()
		self.i = self.sm
		self.o = self.recovered
		self.mult9rdport = self.mult9.get_port()
		self.specials += self.mult9rdport
		self.multDrdport = self.multD.get_port()
		self.specials += self.multDrdport
		self.multBrdport = self.multB.get_port()
		self.specials += self.multBrdport
		self.multErdport = self.multE.get_port()
		self.specials += self.multErdport

		### specify the Module behavior below
		# inverse mix column method
		# 0E 0B 0D 09
		# 09 0E 0B 0D
		# 0D 09 0E 0B
		# 0B 0D 09 0E

		pos = 0 #to hold position in the column
		count = 0
		tmp = 0

		for i in range(16):
			count = i+1 
			self.comb += self.temp[tmp].eq(self.sm[i]) #build a temporary column of 4 values

			if count % 4 == 0: #check whether the column holds 4 elements
				# perform mixColumn computations on the column
				
				self.comb += [self.multErdport.adr.eq(self.temp[0]),
                                              self.multE0.eq(self.multErdport.dat_r)] 
				self.comb += [self.multErdport.adr.eq(self.temp[1]),
                                              self.multE1.eq(self.multErdport.dat_r)] 
				self.comb += [self.multErdport.adr.eq(self.temp[2]),
                                              self.multE2.eq(self.multErdport.dat_r)] 
				self.comb += [self.multErdport.adr.eq(self.temp[3]),
                                              self.multE3.eq(self.multErdport.dat_r)] 
                                
				self.comb += [self.mult9rdport.adr.eq(self.temp[0]),
                                              self.mult90.eq(self.mult9rdport.dat_r)] 
				self.comb += [self.mult9rdport.adr.eq(self.temp[1]),
                                              self.mult91.eq(self.mult9rdport.dat_r)] 
				self.comb += [self.mult9rdport.adr.eq(self.temp[2]),
                                              self.mult92.eq(self.mult9rdport.dat_r)] 
				self.comb += [self.mult9rdport.adr.eq(self.temp[3]),
                                              self.mult93.eq(self.mult9rdport.dat_r)] 
                                
				self.comb += [self.multDrdport.adr.eq(self.temp[0]),
                                              self.multD0.eq(self.multDrdport.dat_r)] 
				self.comb += [self.multDrdport.adr.eq(self.temp[1]),
                                              self.multD1.eq(self.multDrdport.dat_r)] 
				self.comb += [self.multDrdport.adr.eq(self.temp[2]),
                                              self.multD2.eq(self.multDrdport.dat_r)] 
				self.comb += [self.multDrdport.adr.eq(self.temp[3]),
                                              self.multD3.eq(self.multDrdport.dat_r)] 
                                
				self.comb += [self.multBrdport.adr.eq(self.temp[0]),
                                              self.multB0.eq(self.multBrdport.dat_r)] 
				self.comb += [self.multBrdport.adr.eq(self.temp[1]),
                                              self.multB1.eq(self.multBrdport.dat_r)] 
				self.comb += [self.multBrdport.adr.eq(self.temp[2]),
                                              self.multB2.eq(self.multBrdport.dat_r)] 
				self.comb += [self.multBrdport.adr.eq(self.temp[3]),
                                              self.multB3.eq(self.multBrdport.dat_r)] 
				# column[0] = (0Extemp[0])^(0Bxtemp[1])^(0Dxtemp[2])^(09xtemp[3])
				self.comb += self.column[0].eq(multE0 ^ multB1 ^ multD2 ^ mult93)
				# column[1] = (09xtemp[0])^(0Extemp[1])^(0Bxtemp[2])^(0Dxtemp[3])
				self.comb += self.column[1].eq(mult90 ^ multE1 ^ multB2 ^ multD3)
				# column[2] = (0Dxtemp[0])^(09xtemp[1])^(0Extemp[2])^(0Bxtemp[3])
				self.comb += self.column[2].eq(multD0 ^ mult91 ^ multE2 ^ multB3)
				# column[3] = (0Bxtemp[0])^(0Dxtemp[1])^(09xtemp[2])^(0Extemp[3])
				self.comb += self.column[3].eq(multB0 ^ multD1 ^ mult92 ^ multE3)
	
				#update stateMatrix with new column values
				for j in range(count-4,count):
					self.comb += self.recovered[j].eq(self.column[pos])
					pos += 1 #go to next element

				pos = 0 #reset position
				tmp = 0 # reset tmp

			else:
				tmp += 1 #go to next element in column 


# Generate RTL for the parent module and the submodules, run through
# icarus for a syntax check
def test_instance_module():
        sub4 = SubBytes()
        convert(sub4, sub4.io, name="SubBytes").write("SubBytes.v")
        '''
	par = AES()
	convert(par, par.io, name="AES").write("AES.v")
	
	par1 = AES_Enc()
	convert(par1, par1.io, name="AES_Enc").write("AES_Enc.v")
	par2 = AES_Dec()
	convert(par2, par2.io, name="AES_Dec").write("AES_Dec.v")
	sub1 = AddRoundKey()
	convert(sub1, sub1.io, name="AddRoundKey").write("AddRoundKey.v")
	sub2 = ShiftRow()
	convert(sub2, sub2.io, name="ShiftRow").write("ShiftRow.v")
	sub3 = ShiftRowInv()
	convert(sub3, sub3.io, name="ShiftRowInv").write("ShiftRowInv.v")
	sub5 = SubBytesInv()
	convert(sub5, sub5.io, name="SubBytesInv").write("SubBytesInv.v")
	sub6 = SubBytesInv()
	convert(sub6, sub6.io, name="MixColumn").write("MixColumn.v")
	sub7 = SubBytesInv()
	convert(sub7, sub7.io, name="MixColumnInv").write("MixColumnInv.v")
	'''

def check_case(dut,ptext,key):
	for i in range(16):# loop to load testbench inputs onto input ports of our AESCipher core
		yield dut.ptext[i].eq(ptext[i])# load the ith byte of the plain text
		yield dut.key[i].eq(key[i])# load the ith byte of the key
	yield# wait a clock cycle  
    
def testbench(dut):
	ptext=[Signal(8) for x in range(16)]# input plain text test signal
	key=[Signal(8) for x in range(16)]# input cipher key test signal
	dummylen=0

	# prompt user for values
	msg = input("Please enter message to encrypt: ")
	key_in = input("Please 16 bytes enter key: ")

	msglen = len(msg) #length of message
	print("[OK] msg length =",msglen)

	#padd the message with dummy bytes to have a message multiples of 16 bytes long
	if msglen % 16 != 0:
		dummylen = 16 - (msglen % 16)
	msg = msg + ("." * dummylen)
	
	print("[OK] new padded message =",msg)

	#new length of msg
	newLen = len(msg)

	# convert inputs to matrices of corresponding ASCII values
	pt = textconverter(msg.encode('utf-8'))
	key_m = keyconverter(key_in.encode('utf-8'))

	for i in range(newLen):# loop to initialise ptext
		ptext[i]=pt[i]

	#for i in range(16):# loop to initialise key
		#key[i]=key_m[i]

	# allow 256 + 1 clock cycles to tick so that our mem memory is initialised with the 256 words
	#for i in range(256): 
	#	yield

	#yield from check_case(dut,ptext,key)# pass initialised testbench signals to check_case to exercise the dut
	#yield from check_ShiftRow(dut,ptext)# pass initialised testbench signals to check_case to exercise the dut
	yield from check_MixColumn(dut,ptext)# pass initialised testbench signals to check_case to exercise the dut
	#yield from check_SubBytes(dut,ptext)# pass initialised testbench signals to check_case to exercise the dut
	#print("sm_original: {} \nsm_shifted: {}".format((yield dut.sm),(yield dut.sm_shifted)))
	print("sm_in: {} \nsm_mixed: {}".format((yield dut.sm),(yield dut.sm_out)))
	#print("ptext: {} \nkey: {} \ncipher: {} \nrecovered: {}".format((yield dut.ptext),(yield dut.key),(yield dut.ctext),(yield dut.recovered)))

if __name__ == "__main__":
    #test_instance_module()
    dut=MixColumn()# instantiate AES module here
    run_simulation(dut, testbench(dut),vcd_name="migenAES_mixcolumn.vcd")# simulate the module with the logic described in testbench