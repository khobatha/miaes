/* Machine-generated using Migen */
module AddKey(
	input [7:0] sm0,
	input [7:0] sm1,
	input [7:0] sm2,
	input [7:0] sm3,
	input [7:0] sm4,
	input [7:0] sm5,
	input [7:0] sm6,
	input [7:0] sm7,
	input [7:0] sm8,
	input [7:0] sm9,
	input [7:0] sm10,
	input [7:0] sm11,
	input [7:0] sm12,
	input [7:0] sm13,
	input [7:0] sm14,
	input [7:0] sm15,
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
	output reg [7:0] ctext0,
	output reg [7:0] ctext1,
	output reg [7:0] ctext2,
	output reg [7:0] ctext3,
	output reg [7:0] ctext4,
	output reg [7:0] ctext5,
	output reg [7:0] ctext6,
	output reg [7:0] ctext7,
	output reg [7:0] ctext8,
	output reg [7:0] ctext9,
	output reg [7:0] ctext10,
	output reg [7:0] ctext11,
	output reg [7:0] ctext12,
	output reg [7:0] ctext13,
	output reg [7:0] ctext14,
	output reg [7:0] ctext15,
	input sys_clk,
	input sys_rst
);



always @(posedge sys_clk) begin
	if (sys_rst) begin
		ctext0 <= 1'd0;
		ctext1 <= 1'd0;
		ctext2 <= 1'd0;
		ctext3 <= 1'd0;
		ctext4 <= 1'd0;
		ctext5 <= 1'd0;
		ctext6 <= 1'd0;
		ctext7 <= 1'd0;
		ctext8 <= 1'd0;
		ctext9 <= 1'd0;
		ctext10 <= 1'd0;
		ctext11 <= 1'd0;
		ctext12 <= 1'd0;
		ctext13 <= 1'd0;
		ctext14 <= 1'd0;
		ctext15 <= 1'd0;
	end else begin
		ctext0 <= (sm0 ^ key0);
		ctext1 <= (sm1 ^ key1);
		ctext2 <= (sm2 ^ key2);
		ctext3 <= (sm3 ^ key3);
		ctext4 <= (sm4 ^ key4);
		ctext5 <= (sm5 ^ key5);
		ctext6 <= (sm6 ^ key6);
		ctext7 <= (sm7 ^ key7);
		ctext8 <= (sm8 ^ key8);
		ctext9 <= (sm9 ^ key9);
		ctext10 <= (sm10 ^ key10);
		ctext11 <= (sm11 ^ key11);
		ctext12 <= (sm12 ^ key12);
		ctext13 <= (sm13 ^ key13);
		ctext14 <= (sm14 ^ key14);
		ctext15 <= (sm15 ^ key15);
	end
end

endmodule
