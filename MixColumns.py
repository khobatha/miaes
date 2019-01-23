#! /usr/bin/python3
import subprocess
from copy import copy
from migen import *
from migen.fhdl import verilog
from migen.fhdl.verilog import convert

from common import *

'''
=================================================================================================================================
@module name: MixColumns
@description: The ShiftRows step operates on the rows of the state; it cyclically shifts the bytes in each row by a certain offset. 
              For AES, the first row is left unchanged. Each byte of the second row is shifted one to the left. Similarly, the third 
              and fourth rows are shifted by offsets of two and three respectively. In this way, each column of the output 
              state of the ShiftRows step is composed of bytes from each column of the input state. The importance of this step is to 
              avoid the columns being encrypted independently, in which case AES degenerates into four independent block ciphers.
@author: KOS
@contact: khobatha.setetemela@gmail.com
@date: November 2018
@interface:

@parameters:
-DATA_W
-NO_BYTES

@inputs:
-clk: the clock signal
-reset: the module reset signal
-valid_in: input data valid flag
-data_in: input data
-enc_en: encryption enable flag

@outputs:
-valid_out: output data valid flag
-data_out: output data
=====================================================================================================================================
'''
class MixColumns(Module): # MixColumn submodule
        def __init__(self,DATA_W=128,BYTE_NBITS=3):
                self.NO_BYTES=int(DATA_W/(2**BYTE_NBITS))
                
                self.valid_in=Signal(name="MIX_valid_data_in")# input data valid flag signal
                self.data_in=[Signal(2**BYTE_NBITS,name="MIX_data_in{}".format(s)) for s in range(self.NO_BYTES)]# input data signal array
                
                self.valid_out=Signal(name="MIX_valid_data_out")# output data valid flag signal
                self.data_out=[Signal(2**BYTE_NBITS,name="MIX_data_out{}".format(s)) for s in range(self.NO_BYTES)] # output data signal array

                self.io = set()
                self.io = self.io.union(self.data_in)
                self.io = self.io.union(self.data_out)
                
                ###
                
                self.statem=[Signal(2**BYTE_NBITS) for s in range(self.NO_BYTES)] # state matrix
                self.state_mulx2=[Signal(2**BYTE_NBITS) for s in range(self.NO_BYTES)] # state matrix
                self.state_mulx3=[Signal(2**BYTE_NBITS) for s in range(self.NO_BYTES)] # state matrix
                
                #-------------------------------------
                # fill the state matrix with input data
                #-------------------------------------
                self.comb +=[
                If(self.valid_in, 
                # row 0    
                self.statem[0].eq(self.data_in[0]),
                self.statem[1].eq(self.data_in[4]),
                self.statem[2].eq(self.data_in[8]),
                self.statem[3].eq(self.data_in[12]),
                
                # row 1 
                self.statem[4].eq(self.data_in[1]),
                self.statem[5].eq(self.data_in[5]),
                self.statem[6].eq(self.data_in[9]),
                self.statem[7].eq(self.data_in[13]),
                
                # row 2 
                self.statem[8].eq(self.data_in[2]),
                self.statem[9].eq(self.data_in[6]),
                self.statem[10].eq(self.data_in[10]),
                self.statem[11].eq(self.data_in[14]),
                
                # row 3 
                self.statem[12].eq(self.data_in[3]),
                self.statem[13].eq(self.data_in[7]),
                self.statem[14].eq(self.data_in[11]),
                self.statem[15].eq(self.data_in[15])
                )]
                
                #------------------------------------------------
                # fill the multply by 2 and multply by 3 matrices
                #------------------------------------------------
                for b in range(self.NO_BYTES):
                    self.sync+=[If(self.valid_in==1,
                                If(self.statem[b][7]==1,self.state_mulx2[b].eq((self.statem[b]<<1)^(0x1b)))
                                .Else(self.state_mulx2[b].eq((self.statem[b]<<1))),
                                      self.state_mulx3[b].eq(self.state_mulx2[b]^self.statem[b])
                                )
                        ]

                #------------------------------------------------
                # perform the mix columns operation
                #------------------------------------------------
                self.sync+=[If(self.valid_in==1,
                              
                           self.data_out[15].eq(self.state_mulx2[0]^self.state_mulx3[1]^self.statem[2]^self.statem[3]),
                           self.data_out[14].eq(self.statem[0]^self.state_mulx2[1]^self.state_mulx3[2]^self.statem[3]),
                           self.data_out[13].eq(self.statem[0]^self.statem[1]^self.state_mulx2[2]^self.state_mulx3[3]),
                           self.data_out[12].eq(self.state_mulx3[0]^self.statem[1]^self.statem[2]^self.state_mulx3[3]),
                           #*****************************************************************************************
                           self.data_out[11].eq(self.state_mulx2[4]^self.state_mulx3[5]^self.statem[6]^self.statem[7]),
                           self.data_out[10].eq(self.statem[4]^self.state_mulx2[5]^self.state_mulx3[6]^self.statem[3]),
                           self.data_out[9].eq(self.statem[4]^self.statem[5]^self.state_mulx2[6]^self.state_mulx3[3]),
                           self.data_out[8].eq(self.state_mulx3[4]^self.statem[5]^self.statem[6]^self.state_mulx3[3]),
                           #*****************************************************************************************
                           self.data_out[7].eq(self.state_mulx2[8]^self.state_mulx3[9]^self.statem[10]^self.statem[11]),
                           self.data_out[6].eq(self.statem[8]^self.state_mulx2[9]^self.state_mulx3[10]^self.statem[3]),
                           self.data_out[5].eq(self.statem[8]^self.statem[9]^self.state_mulx2[10]^self.state_mulx3[3]),
                           self.data_out[4].eq(self.state_mulx3[8]^self.statem[9]^self.statem[10]^self.state_mulx3[3]),
                           #********************************************************************************************
                           self.data_out[3].eq(self.state_mulx2[12]^self.state_mulx3[13]^self.statem[14]^self.statem[15]),
                           self.data_out[2].eq(self.statem[12]^self.state_mulx2[13]^self.state_mulx3[14]^self.statem[15]),
                           self.data_out[1].eq(self.statem[12]^self.statem[13]^self.state_mulx2[14]^self.state_mulx3[15]),
                           self.data_out[0].eq(self.state_mulx3[12]^self.statem[13]^self.statem[14]^self.state_mulx3[15]),
                           #********************************************************************************************
                           ),self.valid_out.eq(1)]

def check_MixColumns(dut,sm):
        for i in range(16):# loop to load testbench inputs onto input ports of our AESCipher core
                yield dut.data_in[i].eq(sm[i])# load the ith byte of the plain text
        yield dut.valid_in.eq(1)
        #yield dut.encrypt_en.eq(1)
        
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
        msg ="1234" #input("Please enter message to encrypt: ")
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
        yield from check_MixColumns(dut,ptext)# pass initialised testbench signals to check_case to exercise the dut
        #yield from check_SubBytes(dut,ptext)# pass initialised testbench signals to check_case to exercise the dut
        #print("sm_original: {} \nsm_shifted: {}".format((yield dut.sm),(yield dut.sm_shifted)))
        #print("sm_in: {} \nsm_mixed: {}".format((yield dut.sm),(yield dut.sm_out)))
        #print("ptext: {} \nkey: {} \ncipher: {} \nrecovered: {}".format((yield dut.ptext),(yield dut.key),(yield dut.ctext),(yield dut.recovered)))
 
 
 
if __name__ == "__main__":
    #test_instance_module()
    dut=MixColumns()# instantiate AES module here
    run_simulation(dut, testbench(dut),vcd_name="migenAES_MixColumns.vcd")# simulate the module with the logic described in testbench
