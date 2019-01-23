/* Machine-generated using Migen */
module AES(
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
	input [7:0] ctext15,
	input [7:0] rec0,
	input [7:0] rec1,
	input [7:0] rec2,
	input [7:0] rec3,
	input [7:0] rec4,
	input [7:0] rec5,
	input [7:0] rec6,
	input [7:0] rec7,
	input [7:0] rec8,
	input [7:0] rec9,
	input [7:0] rec10,
	input [7:0] rec11,
	input [7:0] rec12,
	input [7:0] rec13,
	input [7:0] rec14,
	input [7:0] rec15
);

wire [7:0] temp0;
wire [7:0] temp1;
wire [7:0] temp2;
wire [7:0] temp3;
wire [7:0] temp4;
wire [7:0] temp5;
wire [7:0] temp6;
wire [7:0] temp7;
wire [7:0] temp8;
wire [7:0] temp9;
wire [7:0] temp10;
wire [7:0] temp11;
wire [7:0] temp12;
wire [7:0] temp13;
wire [7:0] temp14;
wire [7:0] temp15;

// synthesis translate_off
reg dummy_s;
initial dummy_s <= 1'd0;
// synthesis translate_on
assign temp0 = ctext0;
assign temp1 = ctext1;
assign temp2 = ctext2;
assign temp3 = ctext3;
assign temp4 = ctext4;
assign temp5 = ctext5;
assign temp6 = ctext6;
assign temp7 = ctext7;
assign temp8 = ctext8;
assign temp9 = ctext9;
assign temp10 = ctext10;
assign temp11 = ctext11;
assign temp12 = ctext12;
assign temp13 = ctext13;
assign temp14 = ctext14;
assign temp15 = ctext15;

endmodule
