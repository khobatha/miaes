#! /usr/bin/python3
import subprocess
from copy import copy
from migen import *
from migen.fhdl import verilog
from migen.fhdl.verilog import convert

from common import *

'''
=======================================================================================================
@module name: SubBytes
@description: During encryption, each value of the state is replaced with the corresponding sbox value.
@author: KOS
@contact: khobatha.setetemela@gmail.com
@date: November 2018
@interface:

@parameters:
-DATA_W

@inputs:
-clk: the clock signal
-reset: the module reset signal
-valid_in: input data valid flag
-data_in: input data

@outputs:
-valid_out: output data valid flag
-data_out: output data
==========================================================================================================
'''

class SubBytes(Module): # SubBytes submodule
        def __init__(self,DATA_W=128):
                self.NO_BYTES=int(DATA_W/8)
                
                self.valid_in=Signal(name="SUB_valid_data_in")# input data valid flag signal
                self.data_in=[Signal(8,name="SUB_data_in{}".format(s)) for s in range(self.NO_BYTES)]# input data signal array
                
                self.valid_out=Signal(name="SUB_valid_data_out")# output data valid flag signal
                self.data_out=[Signal(8,name="SUB_data_out{}".format(s)) for s in range(self.NO_BYTES)] # output data signal array
                

                self.io = set()
                self.io = self.io.union(self.data_in)
                self.io = self.io.union(self.data_out)
                
                ### Specify the Module behavior below 
                
                
                # Perform byte subsitution
                for b in range(self.NO_BYTES):
                    self.sync+=[If(self.valid_in==1,
                                    If(self.data_in[b]==0x00,self.data_out[b].eq(0x63))
                                    .Elif(self.data_in[b]==0x01,self.data_out[b].eq(0x7c))
                                    .Elif(self.data_in[b]==0x02,self.data_out[b].eq(0x77))
                                    .Elif(self.data_in[b]==0x03,self.data_out[b].eq(0x7b))
                                    .Elif(self.data_in[b]==0x04,self.data_out[b].eq(0xf2))
                                    .Elif(self.data_in[b]==0x05,self.data_out[b].eq(0x6b))
                                    .Elif(self.data_in[b]==0x06,self.data_out[b].eq(0x6f))
                                    .Elif(self.data_in[b]==0x07,self.data_out[b].eq(0xc5))
                                    .Elif(self.data_in[b]==0x08,self.data_out[b].eq(0x30))
                                    .Elif(self.data_in[b]==0x09,self.data_out[b].eq(0x01))
                                    .Elif(self.data_in[b]==0x0a,self.data_out[b].eq(0x67))
                                    .Elif(self.data_in[b]==0x0b,self.data_out[b].eq(0x2b))
                                    .Elif(self.data_in[b]==0x0c,self.data_out[b].eq(0xf3))
                                    .Elif(self.data_in[b]==0x0d,self.data_out[b].eq(0xd7))
                                    .Elif(self.data_in[b]==0x0e,self.data_out[b].eq(0xab))
                                    .Elif(self.data_in[b]==0x0f,self.data_out[b].eq(0x76))
                                    #*****************************************************
                                    .Elif(self.data_in[b]==0x10,self.data_out[b].eq(0xca))
                                    .Elif(self.data_in[b]==0x11,self.data_out[b].eq(0x82))
                                    .Elif(self.data_in[b]==0x12,self.data_out[b].eq(0xc9))
                                    .Elif(self.data_in[b]==0x13,self.data_out[b].eq(0x7d))
                                    .Elif(self.data_in[b]==0x14,self.data_out[b].eq(0xfa))
                                    .Elif(self.data_in[b]==0x15,self.data_out[b].eq(0x59))
                                    .Elif(self.data_in[b]==0x16,self.data_out[b].eq(0x47))
                                    .Elif(self.data_in[b]==0x17,self.data_out[b].eq(0xf0))
                                    .Elif(self.data_in[b]==0x18,self.data_out[b].eq(0xad))
                                    .Elif(self.data_in[b]==0x19,self.data_out[b].eq(0xd4))
                                    .Elif(self.data_in[b]==0x1a,self.data_out[b].eq(0xa2))
                                    .Elif(self.data_in[b]==0x1b,self.data_out[b].eq(0xaf))
                                    .Elif(self.data_in[b]==0x1c,self.data_out[b].eq(0x9c))
                                    .Elif(self.data_in[b]==0x1d,self.data_out[b].eq(0xa4))
                                    .Elif(self.data_in[b]==0x1e,self.data_out[b].eq(0x72))
                                    .Elif(self.data_in[b]==0x1f,self.data_out[b].eq(0xc0))
                                    #*****************************************************
                                    .Elif(self.data_in[b]==0x20,self.data_out[b].eq(0xb7))
                                    .Elif(self.data_in[b]==0x21,self.data_out[b].eq(0xfd))
                                    .Elif(self.data_in[b]==0x22,self.data_out[b].eq(0x93))
                                    .Elif(self.data_in[b]==0x23,self.data_out[b].eq(0x26))
                                    .Elif(self.data_in[b]==0x24,self.data_out[b].eq(0x36))
                                    .Elif(self.data_in[b]==0x25,self.data_out[b].eq(0x3f))
                                    .Elif(self.data_in[b]==0x26,self.data_out[b].eq(0xf7))
                                    .Elif(self.data_in[b]==0x27,self.data_out[b].eq(0xcc))
                                    .Elif(self.data_in[b]==0x28,self.data_out[b].eq(0x34))
                                    .Elif(self.data_in[b]==0x29,self.data_out[b].eq(0xa5))
                                    .Elif(self.data_in[b]==0x2a,self.data_out[b].eq(0xe5))
                                    .Elif(self.data_in[b]==0x2b,self.data_out[b].eq(0xf1))
                                    .Elif(self.data_in[b]==0x2c,self.data_out[b].eq(0x71))
                                    .Elif(self.data_in[b]==0x2d,self.data_out[b].eq(0xd8))
                                    .Elif(self.data_in[b]==0x2e,self.data_out[b].eq(0x31))
                                    .Elif(self.data_in[b]==0x2f,self.data_out[b].eq(0x15))
                                    #*****************************************************
                                    .Elif(self.data_in[b]==0x30,self.data_out[b].eq(0x04))
                                    .Elif(self.data_in[b]==0x31,self.data_out[b].eq(0xc7))
                                    .Elif(self.data_in[b]==0x32,self.data_out[b].eq(0x23))
                                    .Elif(self.data_in[b]==0x33,self.data_out[b].eq(0xc3))
                                    .Elif(self.data_in[b]==0x34,self.data_out[b].eq(0x18))
                                    .Elif(self.data_in[b]==0x35,self.data_out[b].eq(0x96))
                                    .Elif(self.data_in[b]==0x36,self.data_out[b].eq(0x05))
                                    .Elif(self.data_in[b]==0x37,self.data_out[b].eq(0x9a))
                                    .Elif(self.data_in[b]==0x38,self.data_out[b].eq(0x07))
                                    .Elif(self.data_in[b]==0x39,self.data_out[b].eq(0x12))
                                    .Elif(self.data_in[b]==0x3a,self.data_out[b].eq(0x80))
                                    .Elif(self.data_in[b]==0x3b,self.data_out[b].eq(0xe2))
                                    .Elif(self.data_in[b]==0x3c,self.data_out[b].eq(0xeb))
                                    .Elif(self.data_in[b]==0x3d,self.data_out[b].eq(0x27))
                                    .Elif(self.data_in[b]==0x3e,self.data_out[b].eq(0xb2))
                                    .Elif(self.data_in[b]==0x3f,self.data_out[b].eq(0x75))
                                    #*****************************************************
                                    .Elif(self.data_in[b]==0x40,self.data_out[b].eq(0x09))
                                    .Elif(self.data_in[b]==0x41,self.data_out[b].eq(0x83))
                                    .Elif(self.data_in[b]==0x42,self.data_out[b].eq(0x2c))
                                    .Elif(self.data_in[b]==0x43,self.data_out[b].eq(0x1a))
                                    .Elif(self.data_in[b]==0x44,self.data_out[b].eq(0x1b))
                                    .Elif(self.data_in[b]==0x45,self.data_out[b].eq(0x6e))
                                    .Elif(self.data_in[b]==0x46,self.data_out[b].eq(0x5a))
                                    .Elif(self.data_in[b]==0x47,self.data_out[b].eq(0xa0))
                                    .Elif(self.data_in[b]==0x48,self.data_out[b].eq(0x52))
                                    .Elif(self.data_in[b]==0x49,self.data_out[b].eq(0x3b))
                                    .Elif(self.data_in[b]==0x4a,self.data_out[b].eq(0xd6))
                                    .Elif(self.data_in[b]==0x4b,self.data_out[b].eq(0xb3))
                                    .Elif(self.data_in[b]==0x4c,self.data_out[b].eq(0x29))
                                    .Elif(self.data_in[b]==0x4d,self.data_out[b].eq(0xe3))
                                    .Elif(self.data_in[b]==0x4e,self.data_out[b].eq(0x2f))
                                    .Elif(self.data_in[b]==0x4f,self.data_out[b].eq(0x84))
                                    #*****************************************************
                                    .Elif(self.data_in[b]==0x50,self.data_out[b].eq(0x53))
                                    .Elif(self.data_in[b]==0x51,self.data_out[b].eq(0xd1))
                                    .Elif(self.data_in[b]==0x52,self.data_out[b].eq(0x00))
                                    .Elif(self.data_in[b]==0x53,self.data_out[b].eq(0xed))
                                    .Elif(self.data_in[b]==0x54,self.data_out[b].eq(0x20))
                                    .Elif(self.data_in[b]==0x55,self.data_out[b].eq(0xfc))
                                    .Elif(self.data_in[b]==0x56,self.data_out[b].eq(0xb1))
                                    .Elif(self.data_in[b]==0x57,self.data_out[b].eq(0x5b))
                                    .Elif(self.data_in[b]==0x58,self.data_out[b].eq(0x6a))
                                    .Elif(self.data_in[b]==0x59,self.data_out[b].eq(0xcb))
                                    .Elif(self.data_in[b]==0x5a,self.data_out[b].eq(0xbe))
                                    .Elif(self.data_in[b]==0x5b,self.data_out[b].eq(0x39))
                                    .Elif(self.data_in[b]==0x5c,self.data_out[b].eq(0x4a))
                                    .Elif(self.data_in[b]==0x5d,self.data_out[b].eq(0x4c))
                                    .Elif(self.data_in[b]==0x5e,self.data_out[b].eq(0x58))
                                    .Elif(self.data_in[b]==0x5f,self.data_out[b].eq(0xcf))
                                    #*****************************************************
                                    .Elif(self.data_in[b]==0x60,self.data_out[b].eq(0xd0))
                                    .Elif(self.data_in[b]==0x61,self.data_out[b].eq(0xef))
                                    .Elif(self.data_in[b]==0x62,self.data_out[b].eq(0xaa))
                                    .Elif(self.data_in[b]==0x63,self.data_out[b].eq(0xfb))
                                    .Elif(self.data_in[b]==0x64,self.data_out[b].eq(0x43))
                                    .Elif(self.data_in[b]==0x65,self.data_out[b].eq(0x4d))
                                    .Elif(self.data_in[b]==0x66,self.data_out[b].eq(0x33))
                                    .Elif(self.data_in[b]==0x67,self.data_out[b].eq(0x85))
                                    .Elif(self.data_in[b]==0x68,self.data_out[b].eq(0x45))
                                    .Elif(self.data_in[b]==0x69,self.data_out[b].eq(0xf9))
                                    .Elif(self.data_in[b]==0x6a,self.data_out[b].eq(0x02))
                                    .Elif(self.data_in[b]==0x6b,self.data_out[b].eq(0x7f))
                                    .Elif(self.data_in[b]==0x6c,self.data_out[b].eq(0x50))
                                    .Elif(self.data_in[b]==0x6d,self.data_out[b].eq(0x3c))
                                    .Elif(self.data_in[b]==0x6e,self.data_out[b].eq(0x9f))
                                    .Elif(self.data_in[b]==0x6f,self.data_out[b].eq(0xa8))
                                    #*****************************************************
                                    .Elif(self.data_in[b]==0x70,self.data_out[b].eq(0x51))
                                    .Elif(self.data_in[b]==0x71,self.data_out[b].eq(0xa3))
                                    .Elif(self.data_in[b]==0x72,self.data_out[b].eq(0x40))
                                    .Elif(self.data_in[b]==0x73,self.data_out[b].eq(0x8f))
                                    .Elif(self.data_in[b]==0x74,self.data_out[b].eq(0x92))
                                    .Elif(self.data_in[b]==0x75,self.data_out[b].eq(0x9d))
                                    .Elif(self.data_in[b]==0x76,self.data_out[b].eq(0x38))
                                    .Elif(self.data_in[b]==0x77,self.data_out[b].eq(0xf5))
                                    .Elif(self.data_in[b]==0x78,self.data_out[b].eq(0xbc))
                                    .Elif(self.data_in[b]==0x79,self.data_out[b].eq(0xb6))
                                    .Elif(self.data_in[b]==0x7a,self.data_out[b].eq(0xda))
                                    .Elif(self.data_in[b]==0x7b,self.data_out[b].eq(0x21))
                                    .Elif(self.data_in[b]==0x7c,self.data_out[b].eq(0x10))
                                    .Elif(self.data_in[b]==0x7d,self.data_out[b].eq(0xff))
                                    .Elif(self.data_in[b]==0x7e,self.data_out[b].eq(0xf3))
                                    .Elif(self.data_in[b]==0x7f,self.data_out[b].eq(0xd2))
                                    #*****************************************************
                                    .Else(self.data_out[b].eq(0x00)),
                                    #*****************************************************
                                    self.valid_out.eq(1)
                                 )]
                                
                # set the output data valid signal flag    
                #self.sync+=If(self.bytescount>self.NO_BYTES,self.valid_out.eq(1))
                    
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

def check_SubBytes(dut,sm):
        for i in range(16):# loop to load testbench inputs onto input ports of our AESCipher core
                yield dut.data_in[i].eq(sm[i])# load the ith byte of the plain text
                yield
        yield dut.valid_in.eq(1)
        #yield dut.encrypt_en.eq(1)
        yield
        yield
        yield
        yield
        for i in range(32):
               yield
                
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
        #yield from check_ShiftRow(dut,ptext)# pass initialised testbench signals to check_case to exercise the dut
        #yield from check_MixColumn(dut,ptext)# pass initialised testbench signals to check_case to exercise the dut
        yield from check_SubBytes(dut,ptext)# pass initialised testbench signals to check_case to exercise the dut
        #print("sm_original: {} \nsm_shifted: {}".format((yield dut.sm),(yield dut.sm_shifted)))
        #print("sm_in: {} \nsm_mixed: {}".format((yield dut.sm),(yield dut.sm_out)))
        #print("ptext: {} \nkey: {} \ncipher: {} \nrecovered: {}".format((yield dut.ptext),(yield dut.key),(yield dut.ctext),(yield dut.recovered)))
 
 
 
if __name__ == "__main__":
    #test_instance_module()
    dut=SubBytes()# instantiate AES module here
    run_simulation(dut, testbench(dut),vcd_name="migenAES_SubBytes.vcd")# simulate the module with the logic described in testbench