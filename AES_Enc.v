/* Machine-generated using Migen */
module AES_Enc(
	input [7:0] ptext0,
	input [7:0] ptext1,
	input [7:0] ptext2,
	input [7:0] ptext3,
	input [7:0] ptext4,
	input [7:0] ptext5,
	input [7:0] ptext6,
	input [7:0] ptext7,
	input [7:0] ptext8,
	input [7:0] ptext9,
	input [7:0] ptext10,
	input [7:0] ptext11,
	input [7:0] ptext12,
	input [7:0] ptext13,
	input [7:0] ptext14,
	input [7:0] ptext15,
	input [7:0] key0,
	input [7:0] key1,
	input [7:0] key2,
	input [7:0] key3,
	input [7:0] key4,
	input [7:0] key5,
	input [7:0] key6,
	input [7:0] key7,
	input [7:0] key8,
	input [7:0] key9,
	input [7:0] key10,
	input [7:0] key11,
	input [7:0] key12,
	input [7:0] key13,
	input [7:0] key14,
	input [7:0] key15,
	input [7:0] ctext0,
	input [7:0] ctext1,
	input [7:0] ctext2,
	input [7:0] ctext3,
	input [7:0] ctext4,
	input [7:0] ctext5,
	input [7:0] ctext6,
	input [7:0] ctext7,
	input [7:0] ctext8,
	input [7:0] ctext9,
	input [7:0] ctext10,
	input [7:0] ctext11,
	input [7:0] ctext12,
	input [7:0] ctext13,
	input [7:0] ctext14,
	input [7:0] ctext15
);

wire [7:0] temp_temp0;
wire [7:0] temp_temp1;
wire [7:0] temp_temp2;
wire [7:0] temp_temp3;
wire [7:0] temp_temp4;
wire [7:0] temp_temp5;
wire [7:0] temp_temp6;
wire [7:0] temp_temp7;
wire [7:0] temp_temp8;
wire [7:0] temp_temp9;
wire [7:0] temp_temp10;
wire [7:0] temp_temp11;
wire [7:0] temp_temp12;
wire [7:0] temp_temp13;
wire [7:0] temp_temp14;
wire [7:0] temp_temp15;
wire [7:0] temp1_temp10;
wire [7:0] temp1_temp11;
wire [7:0] temp1_temp12;
wire [7:0] temp1_temp13;
wire [7:0] temp1_temp14;
wire [7:0] temp1_temp15;
wire [7:0] temp1_temp16;
wire [7:0] temp1_temp17;
wire [7:0] temp1_temp18;
wire [7:0] temp1_temp19;
wire [7:0] temp1_temp110;
wire [7:0] temp1_temp111;
wire [7:0] temp1_temp112;
wire [7:0] temp1_temp113;
wire [7:0] temp1_temp114;
wire [7:0] temp1_temp115;
wire [7:0] temp20;
wire [7:0] temp21;
wire [7:0] temp22;
wire [7:0] temp23;
wire [7:0] temp24;
wire [7:0] temp25;
wire [7:0] temp26;
wire [7:0] temp27;
wire [7:0] temp28;
wire [7:0] temp29;
wire [7:0] temp210;
wire [7:0] temp211;
wire [7:0] temp212;
wire [7:0] temp213;
wire [7:0] temp214;
wire [7:0] temp215;

// synthesis translate_off
reg dummy_s;
initial dummy_s <= 1'd0;
// synthesis translate_on
assign temp_temp0 = ctext0;
assign temp_temp1 = ctext1;
assign temp_temp2 = ctext2;
assign temp_temp3 = ctext3;
assign temp_temp4 = ctext4;
assign temp_temp5 = ctext5;
assign temp_temp6 = ctext6;
assign temp_temp7 = ctext7;
assign temp_temp8 = ctext8;
assign temp_temp9 = ctext9;
assign temp_temp10 = ctext10;
assign temp_temp11 = ctext11;
assign temp_temp12 = ctext12;
assign temp_temp13 = ctext13;
assign temp_temp14 = ctext14;
assign temp_temp15 = ctext15;
assign temp1_temp10 = ctext0;
assign temp1_temp11 = ctext1;
assign temp1_temp12 = ctext2;
assign temp1_temp13 = ctext3;
assign temp1_temp14 = ctext4;
assign temp1_temp15 = ctext5;
assign temp1_temp16 = ctext6;
assign temp1_temp17 = ctext7;
assign temp1_temp18 = ctext8;
assign temp1_temp19 = ctext9;
assign temp1_temp110 = ctext10;
assign temp1_temp111 = ctext11;
assign temp1_temp112 = ctext12;
assign temp1_temp113 = ctext13;
assign temp1_temp114 = ctext14;
assign temp1_temp115 = ctext15;
assign temp20 = ctext0;
assign temp21 = ctext1;
assign temp22 = ctext2;
assign temp23 = ctext3;
assign temp24 = ctext4;
assign temp25 = ctext5;
assign temp26 = ctext6;
assign temp27 = ctext7;
assign temp28 = ctext8;
assign temp29 = ctext9;
assign temp210 = ctext10;
assign temp211 = ctext11;
assign temp212 = ctext12;
assign temp213 = ctext13;
assign temp214 = ctext14;
assign temp215 = ctext15;

endmodule
