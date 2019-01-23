#! /usr/bin/python3
import subprocess
from copy import copy
from migen import *
from migen.fhdl import verilog
from migen.fhdl.verilog import convert

from common import *
from KeyExpansion import KeyExpansion
from Round import Round
from AddRoundKey import AddRoundKey
from SubBytes import SubBytes
from ShiftRows import ShiftRows

'''
=================================================================================================================================
@module name: AddRoundKey
@description: 
              
@author: KOS
@contact: khobatha.setetemela@gmail.com
@date: November 2018
@interface:

@parameters:
-DATA_W
-KEY_W
-NO_ROUNDS

@inputs:
-clk: the clock signal
-reset: the module reset signal
-cipher_key: input cipher key
-valid_ckey_in: input cipher key valid flag
-plain_text: input plain text
-valid_ptext_in: input plain text valid flag


@outputs:
-valid_ctext_out: output cipher text valid flag
-cipher_text: output cipher text
=====================================================================================================================================
'''
class Top_PipelinedAES(Module): # MixColumn submodule
        def __init__(self,DATA_W,KEY_W,WORD_L,NO_ROUNDS):
                self.NO_DBYTES=int(DATA_W/8)
                self.NO_KBYTES=int(KEY_W/8)
                self.NO_WORDS=int(KEY_W/WORD_L)
                
                self.valid_ptext_in=Signal(name="TOP_valid_ptext")# input text data valid flag signal
                self.plain_text=[Signal(8,name="TOP_plain_text{}".format(s)) for s in range(self.NO_DBYTES)]# input text data signal array
                
                self.valid_ckey_in=Signal(name="TOP_valid_ckey")# input key data valid flag signal
                self.cipher_key=[Signal(8,name="TOP_cipher_key{}".format(s)) for s in range(self.NO_KBYTES)]# input key data signal array
                
                self.valid_ctext_out=Signal(name="TOP_valid_ctext_out")# output text data valid flag signal
                self.cipher_text=[Signal(8,name="TOP_cipher_text{}".format(s)) for s in range(self.NO_DBYTES)] # output text data signal array

                self.io = set()
                self.io = self.io.union(self.plain_text)
                self.io = self.io.union(self.cipher_key)
                self.io = self.io.union(self.cipher_text)
                
                ###
               
                self.valid_round_key=Signal(NO_ROUNDS,name="topw_valid_round_key")
                self.valid_round_data=Signal(NO_ROUNDS,name="topw_valid_round_dat")
                self.data_round=[Signal(DATA_W,name="topw_data_round{}".format(d)) for d in range(NO_ROUNDS)]
                self.valid_sub2shift=Signal(name="topw_valid_sub2shift")
                self.valid_shift2key=Signal(name="topw_valid_shift2key")
                self.data_sub2shift=Signal(DATA_W,name="topw_data_sub2shift")
                self.data_shift2key=Signal(DATA_W,name="topw_data_shift2key")
                self.w=[Signal(DATA_W,name="topw_w{}".format(k)) for k in range(NO_ROUNDS)]
                self.data_shift2key_delayed=Signal(DATA_W,name="topw_data_shift2key_delayed")
                self.valid_shift2key_delayed=Signal(name="topw_valid_sub2key_delayed")
                
                
               
               
               
                
                
                #-------------------------------------
                # default values
                #------------------------------------
                
                    
                
                #-------------------------------------
                # instantiate key expansion - feeds every round with round key
                #------------------------------------
                self.submodules.M_KEYEXP = KeyExpansion(DATA_W,KEY_W,WORD_L,NO_ROUNDS)
                
                for i in range(self.NO_WORDS):
                    self.sync+=[If(self.valid_ckey_in==1,
                                    self.M_KEYEXP.cipher_key[i][0:  8-1].eq(self.cipher_key[4*i]),
                                    self.M_KEYEXP.cipher_key[i][8:  16-1].eq(self.cipher_key[4*i+1]),
                                    self.M_KEYEXP.cipher_key[i][16: 24-1].eq(self.cipher_key[4*i+2]),
                                    self.M_KEYEXP.cipher_key[i][24: 32-1].eq(self.cipher_key[4*i+3]))]
                    
                self.sync+=self.M_KEYEXP.valid_in.eq(self.valid_ckey_in)
                
                for j in range(NO_ROUNDS):
                    self.sync+=[If(self.M_KEYEXP.valid_out[j]==1, 
                                   self.w[j].eq(self.M_KEYEXP.gen_round_keys[j]))]
                
                self.sync+=self.valid_round_key.eq(self.M_KEYEXP.valid_out)
                
                #-------------------------------------
                # add round key
                #-------------------------------------

                self.submodules.M0_ARK=AddRoundKey(DATA_W,KEY_W)
                 
                for b in range(self.NO_DBYTES):
                    self.sync+=[If(self.valid_ptext_in==1,
                                   self.M0_ARK.text_in[b].eq(self.plain_text[b]),
                                   self.M0_ARK.round_key_in[b].eq(self.cipher_key[b]))]
                    
                self.sync+=[self.M0_ARK.valid_text_in.eq(self.valid_ptext_in),
                            self.M0_ARK.valid_rkey_in.eq(self.valid_ckey_in),
                            self.valid_round_data[0].eq(self.M0_ARK.valid_data_out)
                            ]
                
                for b in range(16):
                    self.sync+=If(self.valid_round_data[0]==1,
                                  self.data_round[0][b*8:8*(b+1)-1].eq(self.M0_ARK.data_out[b]))
                
                #-------------------------------------
                # instantiate all rounds - interface with key expansion
                #-------------------------------------
                
                self.submodules.M_ROUNDS=[Round(DATA_W) for r in range(NO_ROUNDS-1)]
                
                for r in range(NO_ROUNDS-1):
                    self.sync+=[
                                If(self.valid_round_data[r]==1,
                                    self.M_ROUNDS[r].data_in[0].eq(self.data_round[r][0: 8-1]),
                                    self.M_ROUNDS[r].data_in[1].eq(self.data_round[r][8: 16-1]),
                                    self.M_ROUNDS[r].data_in[2].eq(self.data_round[r][16: 24-1]),
                                    self.M_ROUNDS[r].data_in[3].eq(self.data_round[r][24: 32-1]),
                                    self.M_ROUNDS[r].data_in[4].eq(self.data_round[r][32: 40-1]),
                                    self.M_ROUNDS[r].data_in[5].eq(self.data_round[r][40: 48-1]),
                                    self.M_ROUNDS[r].data_in[6].eq(self.data_round[r][48: 56-1]),
                                    self.M_ROUNDS[r].data_in[7].eq(self.data_round[r][56: 64-1]),
                                    self.M_ROUNDS[r].data_in[8].eq(self.data_round[r][64: 72-1]),
                                    self.M_ROUNDS[r].data_in[9].eq(self.data_round[r][72: 80-1]),
                                    self.M_ROUNDS[r].data_in[10].eq(self.data_round[r][80: 88-1]),
                                    self.M_ROUNDS[r].data_in[11].eq(self.data_round[r][88: 96-1]),
                                    self.M_ROUNDS[r].data_in[12].eq(self.data_round[r][96: 104-1]),
                                    self.M_ROUNDS[r].data_in[13].eq(self.data_round[r][104: 112-1]),
                                    self.M_ROUNDS[r].data_in[14].eq(self.data_round[r][112: 120-1]),
                                    self.M_ROUNDS[r].data_in[15].eq(self.data_round[r][120: 128-1]),
                                    
                                    self.M_ROUNDS[r].valid_data_in.eq(self.valid_round_data[r])),
                               
                                If(self.valid_round_key[(NO_ROUNDS-1)-r]==1,
                                    self.M_ROUNDS[r].round_key[0].eq(self.w[(NO_ROUNDS-1)-r][0: 8-1]),
                                    self.M_ROUNDS[r].round_key[1].eq(self.w[(NO_ROUNDS-1)-r][8: 16-1]),
                                    self.M_ROUNDS[r].round_key[2].eq(self.w[(NO_ROUNDS-1)-r][16: 24-1]),
                                    self.M_ROUNDS[r].round_key[3].eq(self.w[(NO_ROUNDS-1)-r][24: 32-1]),
                                    self.M_ROUNDS[r].round_key[4].eq(self.w[(NO_ROUNDS-1)-r][32: 40-1]),
                                    self.M_ROUNDS[r].round_key[5].eq(self.w[(NO_ROUNDS-1)-r][40: 48-1]),
                                    self.M_ROUNDS[r].round_key[6].eq(self.w[(NO_ROUNDS-1)-r][48: 56-1]),
                                    self.M_ROUNDS[r].round_key[7].eq(self.w[(NO_ROUNDS-1)-r][56: 64-1]),
                                    self.M_ROUNDS[r].round_key[8].eq(self.w[(NO_ROUNDS-1)-r][64: 72-1]),
                                    self.M_ROUNDS[r].round_key[9].eq(self.w[(NO_ROUNDS-1)-r][72: 80-1]),
                                    self.M_ROUNDS[r].round_key[10].eq(self.w[(NO_ROUNDS-1)-r][80: 88-1]),
                                    self.M_ROUNDS[r].round_key[11].eq(self.w[(NO_ROUNDS-1)-r][88: 96-1]),
                                    self.M_ROUNDS[r].round_key[12].eq(self.w[(NO_ROUNDS-1)-r][96: 104-1]),
                                    self.M_ROUNDS[r].round_key[13].eq(self.w[(NO_ROUNDS-1)-r][104: 112-1]),
                                    self.M_ROUNDS[r].round_key[14].eq(self.w[(NO_ROUNDS-1)-r][112: 120-1]),
                                    self.M_ROUNDS[r].round_key[15].eq(self.w[(NO_ROUNDS-1)-r][120: 128-1]),
                                
                                #self.M_ROUNDS[r].valid_key_in.eq(self.valid_round_key[r]),
                                
                                    self.valid_round_data[r+1].eq(self.M_ROUNDS[r].valid_data_out)),
                                
                                If(self.M_ROUNDS[r].valid_data_out==1,
                                    self.data_round[r+1][0:8-1].eq(self.M_ROUNDS[r].data_out[0]),
                                    self.data_round[r+1][8:16-1].eq(self.M_ROUNDS[r].data_out[1]),
                                    self.data_round[r+1][16:24-1].eq(self.M_ROUNDS[r].data_out[2]),
                                    self.data_round[r+1][24:32-1].eq(self.M_ROUNDS[r].data_out[3]),
                                    self.data_round[r+1][32:40-1].eq(self.M_ROUNDS[r].data_out[4]),
                                    self.data_round[r+1][40:48-1].eq(self.M_ROUNDS[r].data_out[5]),
                                    self.data_round[r+1][48:56-1].eq(self.M_ROUNDS[r].data_out[6]),
                                    self.data_round[r+1][56:64-1].eq(self.M_ROUNDS[r].data_out[7]),
                                    self.data_round[r+1][64:72-1].eq(self.M_ROUNDS[r].data_out[8]),
                                    self.data_round[r+1][72:80-1].eq(self.M_ROUNDS[r].data_out[9]),
                                    self.data_round[r+1][80:88-1].eq(self.M_ROUNDS[r].data_out[10]),
                                    self.data_round[r+1][88:96-1].eq(self.M_ROUNDS[r].data_out[11]),
                                    self.data_round[r+1][96:104-1].eq(self.M_ROUNDS[r].data_out[12]),
                                    self.data_round[r+1][104:112-1].eq(self.M_ROUNDS[r].data_out[13]),
                                    self.data_round[r+1][112:120-1].eq(self.M_ROUNDS[r].data_out[14]),
                                    self.data_round[r+1][120:128-1].eq(self.M_ROUNDS[r].data_out[15]),
                                    
                                    self.valid_round_data[r+1].eq(self.M_ROUNDS[r].valid_data_out))
                                ]
                '''
                for r in range(NO_ROUNDS-1):
                    self.sync+=[
                                
                                self.M_ROUNDS[r].valid_data_in.eq(self.valid_round_data[r]),
                                self.M_ROUNDS[r].valid_key_in.eq(self.valid_round_key[r]),
                                self.valid_round_data[r+1].eq(self.M_ROUNDS[r].valid_data_out)
                                
                                ]
                    
                for r in range(NO_ROUNDS-1):
                    self.sync+=[self.data_round[r+1][0:8-1].eq(self.M_ROUNDS[r].data_out[0]),
                                self.data_round[r+1][8:16-1].eq(self.M_ROUNDS[r].data_out[1]),
                                self.data_round[r+1][16:24-1].eq(self.M_ROUNDS[r].data_out[2]),
                                self.data_round[r+1][24:32-1].eq(self.M_ROUNDS[r].data_out[3]),
                                self.data_round[r+1][32:40-1].eq(self.M_ROUNDS[r].data_out[4]),
                                self.data_round[r+1][40:48-1].eq(self.M_ROUNDS[r].data_out[5]),
                                self.data_round[r+1][48:56-1].eq(self.M_ROUNDS[r].data_out[6]),
                                self.data_round[r+1][56:64-1].eq(self.M_ROUNDS[r].data_out[7]),
                                self.data_round[r+1][64:72-1].eq(self.M_ROUNDS[r].data_out[8]),
                                self.data_round[r+1][72:80-1].eq(self.M_ROUNDS[r].data_out[9]),
                                self.data_round[r+1][80:88-1].eq(self.M_ROUNDS[r].data_out[10]),
                                self.data_round[r+1][88:96-1].eq(self.M_ROUNDS[r].data_out[11]),
                                self.data_round[r+1][96:104-1].eq(self.M_ROUNDS[r].data_out[12]),
                                self.data_round[r+1][104:112-1].eq(self.M_ROUNDS[r].data_out[13]),
                                self.data_round[r+1][112:120-1].eq(self.M_ROUNDS[r].data_out[14]),
                                self.data_round[r+1][120:128-1].eq(self.M_ROUNDS[r].data_out[15])
                                ]
                    '''
                #-------------------------------------
                # final round - no mix columns step - SubBytes
                #-------------------------------------
                
                self.submodules.MN_SUB=SubBytes(DATA_W)
                
                for b in range(self.NO_DBYTES):# fill SubBytes module with input data
                    self.sync+=[If(self.valid_round_data[NO_ROUNDS-1]==1,
                                   self.MN_SUB.data_in[b].eq(self.data_round[NO_ROUNDS-1][8*b:8*(b+1)-1]))]
                    
                self.sync+=[self.MN_SUB.valid_in.eq(self.valid_round_data[NO_ROUNDS-1])]
                
                for b in range(self.NO_DBYTES):# fill SubBytes module with input data
                    self.sync+=[If(self.MN_SUB.valid_out==1,
                                   self.data_sub2shift.eq(self.MN_SUB.data_out[b]))]
                                   
                self.sync+=[self.valid_sub2shift.eq(self.MN_SUB.valid_out)] 

                #-------------------------------------
                # final round - no mix columns step - ShiftRows
                #-------------------------------------
                
                
                self.submodules.MN_SR=ShiftRows(DATA_W)
               
                for b in range(self.NO_DBYTES):# fill ShiftRows module with data
                    self.sync+=[If(self.valid_sub2shift==1,
                                   self.MN_SR.data_in[b].eq(self.data_sub2shift[8*b:8*(b+1)-1]))]
                    
                self.sync+=[self.MN_SR.valid_in.eq(self.valid_sub2shift)]
                
                for b in range(self.NO_DBYTES):# fill SubBytes module with input data
                    self.sync+=[If(self.MN_SR.valid_out==1,
                                   self.data_shift2key[8*b:8*(b+1)-1].eq(self.MN_SR.data_out[b]))]
                    
                self.sync+=self.valid_shift2key.eq(self.MN_SR.valid_out)
                
                #-------------------------------------
                # final round - no mix columns step - AddRoundKey
                #-------------------------------------
                
                
                self.submodules.MN_ARK=AddRoundKey(DATA_W,KEY_W)
                
                for b in range(self.NO_DBYTES):
                    self.sync+=[If(self.valid_round_key[NO_ROUNDS-1]==1,
                                   If(self.valid_shift2key_delayed==1,
                                   self.MN_ARK.text_in[b].eq(self.data_shift2key_delayed[8*b:8*(b+1)-1]),
                                   self.MN_ARK.round_key_in[b].eq(self.w[0][8*b:8*(b+1)-1])))]
                    
                self.sync+=[self.MN_ARK.valid_text_in.eq(self.valid_shift2key_delayed),
                            self.MN_ARK.valid_rkey_in.eq(self.valid_round_key[NO_ROUNDS-1])]

                for b in range(self.NO_DBYTES):
                    self.sync+=If(self.MN_ARK.valid_data_out==1,
                                  self.cipher_text[b].eq(self.MN_ARK.data_out[b]))
                
                self.sync+=[ self.valid_ctext_out.eq(self.MN_ARK.valid_data_out)]
                
                #-------------------------------------
                # introduce delay register to match pipeling stages
                #-------------------------------------
                self.sync+=If(self.data_shift2key==1,
                              self.data_shift2key_delayed.eq(self.data_shift2key),
                              self.valid_shift2key_delayed.eq(self.valid_shift2key))
                

def check_TopPipelinedAES(dut,text,key):
        for i in range(16):# loop to load testbench inputs onto input ports of our AESCipher core
                yield dut.plain_text[i].eq(text[i])
                yield dut.cipher_key[i].eq(key[i])
        yield dut.valid_ptext_in.eq(1)
        yield dut.valid_ckey_in.eq(1)   
        
        for i in range(256):
                yield #dut.cipher_text        


                
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
        #sub7 = KeyExpansion(DATA_W,KEY_L,WORD_L,NO_ROUNDS)
        #convert(sub7, sub7.io, name="KeyExpansion").write("KeyExpansion.v")
        #sub7 = AddRoundKey(DATA_W,KEY_L)
        #convert(sub7, sub7.io, name="AddRoundKey").write("AddRoundKey.v")
        sub8 = Top_PipelinedAES(DATA_W,KEY_L,WORD_L,NO_ROUNDS)
        convert(sub8, sub8.io, name="Top_PipelinedAES").write("Top_PipelinedAES.v")
                              
def testbench(dut):
        ptext=[Signal(8) for x in range(16)]# input plain text test signal
        key=[Signal(8) for x in range(16)]# input cipher key test signal
        dummylen=0

        # prompt user for values
        msg ="1234567890123456"#input("Please enter message to encrypt: ")
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
    
        newLen=16
        count=0x00
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
        
        #yield from check_KeyExpansion(dut,ptext)# pass initialised testbench signals to check_case to exercise the dut
        #yield from check_AddRoundKey(dut,ptext,key)# pass initialised testbench signals to check_case to exercise the dut
        yield from check_TopPipelinedAES(dut,ptext,key)# pass initialised testbench signals to check_case to exercise the dut
        #yield from check_SubBytes(dut,ptext)# pass initialised testbench signals to check_case to exercise the dut
        #print("sm_original: {} \nsm_shifted: {}".format((yield dut.sm),(yield dut.sm_shifted)))
        #print("sm_in: {} \nsm_mixed: {}".format((yield dut.sm),(yield dut.sm_out)))
        print("ptext: {} \nkey: {} \ncipher: {}".format((yield dut.plain_text),(yield dut.cipher_key),(yield dut.cipher_key)))
 
 
 
if __name__ == "__main__":
    test_instance_module()
    DATA_W=128
    KEY_W=128
    WORD_L=32
    NO_ROUNDS=10
    dut=Top_PipelinedAES(DATA_W,KEY_W,WORD_L,NO_ROUNDS)# instantiate AES module here
    ##run_simulation(dut, testbench(dut),vcd_name="migenAES_Top_PipelinedAES.vcd")# simulate the module with the logic described in testbench
