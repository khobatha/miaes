#! /usr/bin/python3
import subprocess
from copy import copy
from migen import *
from migen.fhdl import verilog
from migen.fhdl.verilog import convert

from common import *
from SubBytes import SubBytes

'''
=================================================================================================================================
@module name: RoundKeyGenerator
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
              |16               | 16                |  44
              |24               | 16                |  52
              |32               | 16                |  60
              ------------------------------------------------------
              
@author: KOS
@contact: khobatha.setetemela@gmail.com
@date: November 2018
@interface:

@parameters:
-KEY_L
-WORD_L

@inputs:
-clk: the clock signal
-reset: the module reset signal
-valid_in: input data valid flag
-RCON_Word: round constant word
-cipher_key: input cipher key

@outputs:
-valid_out: output data valid flag
-round_key: round key
=====================================================================================================================================
'''
class RoundKeysGenerator(Module): # MixColumn submodule
        def __init__(self,KEY_L,WORD_L):
                self.NO_WORDS=int(KEY_L/WORD_L)
                self.NO_WBYTES=int(WORD_L/8)
                
                self.cipher_key=[Signal(WORD_L,name="RKGen_cipher_key{}".format(w)) for w in range(self.NO_WORDS)]# input cipher key signal array containing NO_WORDS words each of size WORD_L
                self.valid_in=Signal(name="RKGen_valid_key_in")# input data valid flag signal
                
                self.RCON_Word=Signal(WORD_L,name="RKGen_RCON_Word_in")# round constant word
                
                self.valid_out=Signal(name="RKGen_valid_round_key_out")# output data valid flag signal
                self.round_key=[Signal(WORD_L,name="RKGen_round_key{}".format(w)) for w in range(self.NO_WORDS)] # output generated round key signal array containing NO_WORDS words each of size WORD_L
                
               
               
                self.io = set()
                self.io = self.io.union(self.cipher_key)
                self.io = self.io.union(self.round_key)
                
                ###
                
                
                self.key_RotWord = [Signal(8) for b in range(self.NO_WBYTES)]
                self.key_FirstStage=[Signal(WORD_L) for w in range(self.NO_WORDS)]
                self.key_SecondStage=[Signal(WORD_L) for w in range(self.NO_WORDS)]
                self.key_Delayed=[Signal(WORD_L) for w in range(self.NO_WORDS)]
                self.key_SubBytes = [Signal(8) for b in range(self.NO_WBYTES)]
                self.key_SubBytesW=Signal(WORD_L)
                self.temp_RoundKey = [Signal(WORD_L) for w in range(self.NO_WORDS)]
                self.valid_first_stage = Signal()
                self.valid_round_key = Signal(name="RKGenw_valid_round_key")
                self.valid_subbytes_out = Signal(name="RKGenw_valid_subbytes")
                self.submodules.subBytes = SubBytes()
                
                #-------------------------------------
                # First stage register
                #-------------------------------------
                self.sync += [self.valid_first_stage.eq(0),
                              self.key_FirstStage[0].eq(0),
                              self.key_FirstStage[1].eq(0),
                              self.key_FirstStage[2].eq(0),
                              self.key_FirstStage[3].eq(0),
                              If(self.valid_in==1,
                                 self.key_FirstStage[0].eq(self.cipher_key[0]),
                                 self.key_FirstStage[1].eq(self.cipher_key[1]),
                                 self.key_FirstStage[2].eq(self.cipher_key[2]),
                                 self.key_FirstStage[3].eq(self.cipher_key[3])),
                              self.valid_first_stage.eq(self.valid_in)]
                #-------------------------------------
                # Second stage register
                #-------------------------------------
                self.sync += [self.key_SecondStage[0].eq(0),
                              self.key_SecondStage[1].eq(0),
                              self.key_SecondStage[2].eq(0),
                              self.key_SecondStage[3].eq(0),
                              If(self.valid_first_stage==1, 
                                 self.key_SecondStage[0].eq(self.key_FirstStage[0]),
                                 self.key_SecondStage[1].eq(self.key_FirstStage[1]),
                                 self.key_SecondStage[2].eq(self.key_FirstStage[2]),
                                 self.key_SecondStage[3].eq(self.key_FirstStage[3]))]
                #-------------------------------------
                # RotWord
                #-------------------------------------  
                self.comb +=[
                            self.key_RotWord[0].eq(self.key_FirstStage[1]),
                            self.key_RotWord[1].eq(self.key_FirstStage[2]),
                            self.key_RotWord[2].eq(self.key_FirstStage[3]),
                            self.key_RotWord[3].eq(self.key_FirstStage[0])]
                
                #-------------------------------------
                # SubBytes
                #-------------------------------------
                self.sync += [self.subBytes.data_in[0].eq(self.key_RotWord[0]),
                              self.subBytes.data_in[1].eq(self.key_RotWord[1]),
                              self.subBytes.data_in[2].eq(self.key_RotWord[2]),
                              self.subBytes.data_in[3].eq(self.key_RotWord[3]),
                              self.subBytes.valid_in.eq(1), 
                              If(self.subBytes.valid_out==1,
                                 self.key_SubBytes[0].eq(self.subBytes.data_out[0]),
                                 self.key_SubBytes[1].eq(self.subBytes.data_out[1]),
                                 self.key_SubBytes[2].eq(self.subBytes.data_out[2]),
                                 self.key_SubBytes[3].eq(self.subBytes.data_out[3]),
                                 self.valid_subbytes_out.eq(1))]
                
                #-------------------------------------
                # Round key calculations
                #-------------------------------------
               
                self.sync +=[If(self.valid_subbytes_out==1,
                                self.key_SubBytesW[0*8     :1*8-1].eq(self.key_SubBytes[0]),
                                self.key_SubBytesW[1*8     :2*8-1].eq(self.key_SubBytes[1]),
                                self.key_SubBytesW[2*8     :3*8-1].eq(self.key_SubBytes[2]),
                                self.key_SubBytesW[3*8     :4*8-1].eq(self.key_SubBytes[3]),
                                self.temp_RoundKey[3].eq(self.key_SecondStage[3] ^ self.key_SubBytesW ^ self.RCON_Word),
                                self.temp_RoundKey[2].eq(self.key_SecondStage[2] ^ self.temp_RoundKey[3]),
                                self.temp_RoundKey[1].eq(self.key_SecondStage[1] ^ self.temp_RoundKey[2]),
                                self.temp_RoundKey[0].eq(self.key_SecondStage[0] ^ self.temp_RoundKey[1]))
                             ]
                
                #-------------------------------------
                # Round key register - Third stage
                #-------------------------------------
                
                self.sync += [self.key_Delayed[0].eq(0),
                              self.key_Delayed[1].eq(0),
                              self.key_Delayed[2].eq(0),
                              self.key_Delayed[3].eq(0),
                              self.valid_round_key.eq(0),
                              If(self.valid_subbytes_out==1, 
                                 self.key_Delayed[0].eq(self.temp_RoundKey[0]),
                                 self.key_Delayed[1].eq(self.temp_RoundKey[0]),
                                 self.key_Delayed[2].eq(self.temp_RoundKey[0]),
                                 self.key_Delayed[3].eq(self.temp_RoundKey[0])
                                 ),
                              self.valid_round_key.eq(self.valid_subbytes_out)]
                
                #-------------------------------------
                # Output register - Fourth stage
                #-------------------------------------
                
                self.sync += [self.valid_out.eq(0),
                              self.round_key[0].eq(0),
                              self.round_key[1].eq(0),
                              self.round_key[2].eq(0),
                              self.round_key[3].eq(0),
                              If(self.valid_round_key==1, 
                                 self.round_key[0].eq(self.key_Delayed[0]),
                                 self.round_key[1].eq(self.key_Delayed[1]),
                                 self.round_key[2].eq(self.key_Delayed[2]),
                                 self.round_key[3].eq(self.key_Delayed[3]),
                                 ),
                              self.valid_out.eq(self.valid_round_key)]

def check_RoundKeyGenerator(dut,sm,rcw):
        for i in range(4):# loop to load testbench inputs onto input ports of our AESCipher core
                yield dut.cipher_key[i].eq(sm[i])
        yield dut.RCON_Word.eq(rcw)
        yield dut.valid_in.eq(1)
        
        for i in range(32):
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
        '''
        sub7 = MixColumns()
        convert(sub7, sub7.io, name="MixColumns").write("MixColumns.v")
                              
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
        rcw=0x6c000000
        yield from check_RoundKeyGenerator(dut,ptext,rcw)# pass initialised testbench signals to check_case to exercise the dut
        #yield from check_SubBytes(dut,ptext)# pass initialised testbench signals to check_case to exercise the dut
        #print("sm_original: {} \nsm_shifted: {}".format((yield dut.sm),(yield dut.sm_shifted)))
        #print("sm_in: {} \nsm_mixed: {}".format((yield dut.sm),(yield dut.sm_out)))
        #print("ptext: {} \nkey: {} \ncipher: {} \nrecovered: {}".format((yield dut.ptext),(yield dut.key),(yield dut.ctext),(yield dut.recovered)))
 
 
 
if __name__ == "__main__":
    #test_instance_module()
    dut=RoundKeysGenerator(128,32)# instantiate AES module here
    run_simulation(dut, testbench(dut),vcd_name="migenAES_RoundKeysGenerator.vcd")# simulate the module with the logic described in testbench
