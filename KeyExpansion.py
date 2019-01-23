#! /usr/bin/python3
import subprocess
from copy import copy
from migen import *
from migen.fhdl import verilog
from migen.fhdl.verilog import convert

from common import *
from RoundKeysGenerator import RoundKeysGenerator

'''
=================================================================================================================================
@module name: KeyExpansion
@description: Prior to encryption or decryption the key must be expanded. The expande key is used in the AddRoundKey module. The 
              key expansion module performs a maximum of 4 consecutive operations. The functions are:
              ........
              ROT WORD 
              SUB WORD 
              RCON 
              EK 
              K
              ........
              An iteration of the above operations is called a round. The amount of rounds of the key expansion operation depends
              on the key size:
              ------------------------------------------------------
              |Key size(bytes)  | Block size(bytes) |  Rounds
              |-----------------------------------------------------
              |16               | 16                |  10
              |24               | 16                |  12
              |32               | 16                |  14
              ------------------------------------------------------
              
@author: KOS
@contact: khobatha.setetemela@gmail.com
@date: November 2018
@interface:

@parameters:
-DATA_W
-KEY_L
-NO_ROUNDS

@inputs:
-clk: the clock signal
-reset: the module reset signal
-valid_in: input data valid flag
-cipher_key: cipher key

@outputs:
-valid_out: output data valid flag
-gen_round_keys: expanded round keys
=====================================================================================================================================
'''
class KeyExpansion(Module): # MixColumn submodule
        def __init__(self,DATA_W,KEY_L,WORD_L,NO_ROUNDS,BYTE_NBITS=3):
                self.NO_WORDS=int(KEY_L/WORD_L)
                self.NO_BYTES=int(WORD_L/8)
                
                self.cipher_key=[Signal(WORD_L,name="KEEXP_cipher_key{}".format(w)) for w in range(self.NO_WORDS)]# input cipher key signal array containing NO_WORDS words each of size WORD_L
                self.valid_in=Signal(name="KEEXP_valid_cipher_in")# input data valid flag signal
                
                
                self.gen_round_keys=[Signal(DATA_W,name="KEEXP_gen_round_keys{}".format(k)) for k in range(NO_ROUNDS)] # output generated round key signal array containing NO_WORDS words each of size WORD_L
                self.valid_out=Signal(NO_ROUNDS,name="KEEXP_valid_rkeys_out")# output data valid flag signal
                
                self.io = set()
                self.io = self.io.union(self.cipher_key)
                self.io = self.io.union(self.gen_round_keys)
                
                ###
                self.RCON=[Signal(32,name="KEEXPw_RCON{}".format(s)) for s in range(10)] # round constant values
                self.keygen_valid_out=Signal(NO_ROUNDS,name="KEEXPw_keygen_valid_out")# output data valid flag signal
                self.w=[Signal(DATA_W,name="KEEXPw_w{}".format(k)) for k in range(NO_ROUNDS)] # output generated round key signal array containing NO_WORDS words each of size WORD_L
                
                self.submodules.rkgen_array = [RoundKeysGenerator(KEY_L,WORD_L) for m in range(NO_ROUNDS)]
                self.submodules.M0_RKGEN=RoundKeysGenerator(KEY_L,WORD_L)
                
                #-------------------------------------
                # initialise round constants
                #-------------------------------------
                self.comb +=[self.RCON[0].eq(0x01000000),
                             self.RCON[1].eq(0x02000000),
                             self.RCON[2].eq(0x04000000),
                             self.RCON[3].eq(0x08000000),
                             self.RCON[4].eq(0x10000000),
                             self.RCON[5].eq(0x20000000),
                             self.RCON[6].eq(0x40000000),
                             self.RCON[7].eq(0x80000000),
                             self.RCON[8].eq(0x1b000000),
                             self.RCON[9].eq(0x36000000)
                             ]
                
                
                #------------------------------------------------
                # interface RoundKeyGenerator 0 with KeyExpansion
                #------------------------------------------------
                
                self.comb+=[self.M0_RKGEN.RCON_Word.eq(self.RCON[0]),# input: round constant
                            
                                
                                If(self.valid_in==1,
                                    self.M0_RKGEN.cipher_key[0].eq(self.cipher_key[0]),# input: cipher key
                                    self.M0_RKGEN.cipher_key[1].eq(self.cipher_key[1]),
                                    self.M0_RKGEN.cipher_key[2].eq(self.cipher_key[2]),
                                    self.M0_RKGEN.cipher_key[3].eq(self.cipher_key[3]),
                                
                                    self.M0_RKGEN.valid_in.eq(self.valid_in)),# input: valid input flag
                                
                                If(self.M0_RKGEN.valid_out==1,
                                    self.w[0][0       : WORD_L-1].eq(self.M0_RKGEN.round_key[0]),# output: generated round key
                                    self.w[0][WORD_L  : 2*WORD_L-1].eq(self.M0_RKGEN.round_key[1]),
                                    self.w[0][2*WORD_L: 3*WORD_L-1].eq(self.M0_RKGEN.round_key[2]),
                                    self.w[0][3*WORD_L: 4*WORD_L-1].eq(self.M0_RKGEN.round_key[3]),
                                
                                    self.keygen_valid_out[0].eq(self.M0_RKGEN.valid_out))# output: valid generated round key output flag
                                ]
                
                
                #------------------------------------------------
                # interface RoundKeyGenerator with KeyExpansion
                #------------------------------------------------
                for r in range(NO_ROUNDS):
                    self.comb+=[If(r!=0,
                                self.rkgen_array[r].RCON_Word.eq(self.RCON[r]),# input: round constant
                                
                                If(self.keygen_valid_out[r-1]==1,
                                    self.rkgen_array[r].cipher_key[0].eq(self.w[r-1][0       : WORD_L-1]),# input: cipher key
                                    self.rkgen_array[r].cipher_key[1].eq(self.w[r-1][WORD_L  : 2*WORD_L-1]),
                                    self.rkgen_array[r].cipher_key[2].eq(self.w[r-1][2*WORD_L: 3*WORD_L-1]),
                                    self.rkgen_array[r].cipher_key[3].eq(self.w[r-1][3*WORD_L: 4*WORD_L-1]),
                                
                                    self.rkgen_array[r].valid_in.eq(self.keygen_valid_out[r-1])),# input: valid input flag
                                
                                If(self.rkgen_array[r].valid_out==1,
                                    self.w[r][0       : WORD_L-1].eq(self.rkgen_array[r].round_key[0]),# output: generated round key
                                    self.w[r][WORD_L  : 2*WORD_L-1].eq(self.rkgen_array[r].round_key[1]),
                                    self.w[r][2*WORD_L: 3*WORD_L-1].eq(self.rkgen_array[r].round_key[2]),
                                    self.w[r][3*WORD_L: 4*WORD_L-1].eq(self.rkgen_array[r].round_key[3]),
                                    self.keygen_valid_out[r].eq(self.rkgen_array[r].valid_out))# output: valid generated round key output flag
                                
                                )
                                ]
               
                #------------------------------------------------
                # assign all round keys to one output
                #------------------------------------------------
                '''
                If(self.keygen_valid_out[0]==1, 
                                 If(self.keygen_valid_out[1]==1,
                                 If(self.keygen_valid_out[2]==1,
                                 If(self.keygen_valid_out[3]==1,
                                 If(self.keygen_valid_out[4]==1,
                                 If(self.keygen_valid_out[5]==1,
                                 If(self.keygen_valid_out[6]==1,
                                 If(self.keygen_valid_out[7]==1,
                                 If(self.keygen_valid_out[8]==1,
                                 If(self.keygen_valid_out[9]==1,
                '''
                for k in range(10):
                    self.sync+=If(self.keygen_valid_out[1]==1,
                                  self.gen_round_keys[k].eq(self.w[k])
                                  ).Else(self.gen_round_keys[k].eq(0))
                    
                self.sync +=self.valid_out.eq(self.keygen_valid_out)#))))))))))]

def check_KeyExpansion(dut,sm):
        for i in range(4):# loop to load testbench inputs onto input ports of our AESCipher core
                yield dut.cipher_key[i].eq(sm[i])# load the ith byte of the plain text
        yield dut.valid_in.eq(1)
        
        for i in range(100):
                yield                


                
# Generate RTL for the parent module and the submodules, run through
# icarus for a syntax check
def test_instance_module():
        '''
        sub4 = SubBytes()
        convert(sub4, sub4.io, name="SubBytes").write("SubBytes.v")
        par = AES()
        convert(par, par.io, name="AES").write("AES.v")
        
        par1 = AES_Enc()
        convert(par1, par1.io, name="AES_Enc").write("AES_Enc.v")
        par2 = AES_Dec()
        convert(par2, par2.io, name="AES_Dec").write("AES_Dec.v")
        sub1 = AddRoundKey()
        convert(sub1, sub1.io, name="AddRoundKey").write("AddRoundKey.v")
       
        sub2 = ShiftRows()
        convert(sub2, sub2.io, name="ShiftRows").write("ShiftRows.v")
        
        sub3 = ShiftRowInv()
        convert(sub3, sub3.io, name="ShiftRowInv").write("ShiftRowInv.v")
        sub5 = SubBytesInv()
        convert(sub5, sub5.io, name="SubBytesInv").write("SubBytesInv.v")
        sub6 = SubBytesInv()
        convert(sub6, sub6.io, name="MixColumn").write("MixColumn.v")
        
        sub7 = MixColumns()
        convert(sub7, sub7.io, name="MixColumns").write("MixColumns.v")
        '''
        DATA_W=128
        KEY_L=128
        WORD_L=32
        NO_ROUNDS=10
        #dut=KeyExpansion(DATA_W,KEY_L,WORD_L,NO_ROUNDS)# instantiate AES module here
        sub7 = KeyExpansion(DATA_W,KEY_L,WORD_L,NO_ROUNDS)
        convert(sub7, sub7.io, name="KeyExpansion").write("KeyExpansion.v")
                              
def testbench(dut):
        ptext=[Signal(8) for x in range(16)]# input plain text test signal
        key=[Signal(8) for x in range(16)]# input cipher key test signal
        dummylen=0

        # prompt user for values
        msg ="1234567890123456" #input("Please enter message to encrypt: ")
        key_in ="1234567890123456" #input("Please 16 bytes enter key: ")

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

        for i in range(16):# loop to initialise key
                key[i]=key_m[i]

        # allow 256 + 1 clock cycles to tick so that our mem memory is initialised with the 256 words
        #for i in range(256): 
        #       yield

        #yield from check_case(dut,ptext,key)# pass initialised testbench signals to check_case to exercise the dut
        #yield from check_ShiftRows(dut,ptext)# pass initialised testbench signals to check_case to exercise the dut
        #yield from check_MixColumns(dut,ptext)# pass initialised testbench signals to check_case to exercise the dut
        #rcw=0x6c000000
        
        yield from check_KeyExpansion(dut,ptext)# pass initialised testbench signals to check_case to exercise the dut
        #yield from check_SubBytes(dut,ptext)# pass initialised testbench signals to check_case to exercise the dut
        #print("sm_original: {} \nsm_shifted: {}".format((yield dut.sm),(yield dut.sm_shifted)))
        #print("sm_in: {} \nsm_mixed: {}".format((yield dut.sm),(yield dut.sm_out)))
        #print("ptext: {} \nkey: {} \ncipher: {} \nrecovered: {}".format((yield dut.ptext),(yield dut.key),(yield dut.ctext),(yield dut.recovered)))
 
 
 
if __name__ == "__main__":
    #test_instance_module()
    DATA_W=128
    KEY_L=128
    WORD_L=32
    NO_ROUNDS=10
    dut=KeyExpansion(DATA_W,KEY_L,WORD_L,NO_ROUNDS)# instantiate AES module here
    run_simulation(dut, testbench(dut),vcd_name="migenAES_KeyExpansion.vcd")# simulate the module with the logic described in testbench
