/* Machine-generated using Migen */
module ShiftRows(
	input [7:0] SHIFT_data_in0,
	input [7:0] SHIFT_data_in1,
	input [7:0] SHIFT_data_in2,
	input [7:0] SHIFT_data_in3,
	input [7:0] SHIFT_data_in4,
	input [7:0] SHIFT_data_in5,
	input [7:0] SHIFT_data_in6,
	input [7:0] SHIFT_data_in7,
	input [7:0] SHIFT_data_in8,
	input [7:0] SHIFT_data_in9,
	input [7:0] SHIFT_data_in10,
	input [7:0] SHIFT_data_in11,
	input [7:0] SHIFT_data_in12,
	input [7:0] SHIFT_data_in13,
	input [7:0] SHIFT_data_in14,
	input [7:0] SHIFT_data_in15,
	output reg [7:0] SHIFT_data_out0,
	output reg [7:0] SHIFT_data_out1,
	output reg [7:0] SHIFT_data_out2,
	output reg [7:0] SHIFT_data_out3,
	output reg [7:0] SHIFT_data_out4,
	output reg [7:0] SHIFT_data_out5,
	output reg [7:0] SHIFT_data_out6,
	output reg [7:0] SHIFT_data_out7,
	output reg [7:0] SHIFT_data_out8,
	output reg [7:0] SHIFT_data_out9,
	output reg [7:0] SHIFT_data_out10,
	output reg [7:0] SHIFT_data_out11,
	output reg [7:0] SHIFT_data_out12,
	output reg [7:0] SHIFT_data_out13,
	output reg [7:0] SHIFT_data_out14,
	output reg [7:0] SHIFT_data_out15
);

reg SHIFT_valid_data_in = 1'd0;
wire SHIFT_valid_data_out;
reg [7:0] statem0 = 1'd0;
reg [7:0] statem1 = 1'd0;
reg [7:0] statem2 = 1'd0;
reg [7:0] statem3 = 1'd0;
reg [7:0] statem4 = 1'd0;
reg [7:0] statem5 = 1'd0;
reg [7:0] statem6 = 1'd0;
reg [7:0] statem7 = 1'd0;
reg [7:0] statem8 = 1'd0;
reg [7:0] statem9 = 1'd0;
reg [7:0] statem10 = 1'd0;
reg [7:0] statem11 = 1'd0;
reg [7:0] statem12 = 1'd0;
reg [7:0] statem13 = 1'd0;
reg [7:0] statem14 = 1'd0;
reg [7:0] statem15 = 1'd0;

// synthesis translate_off
reg dummy_s;
initial dummy_s <= 1'd0;
// synthesis translate_on

// synthesis translate_off
reg dummy_d;
// synthesis translate_on
always @(*) begin
	statem0 <= 1'd0;
	statem1 <= 1'd0;
	statem2 <= 1'd0;
	statem3 <= 1'd0;
	statem4 <= 1'd0;
	statem5 <= 1'd0;
	statem6 <= 1'd0;
	statem7 <= 1'd0;
	statem8 <= 1'd0;
	statem9 <= 1'd0;
	statem10 <= 1'd0;
	statem11 <= 1'd0;
	statem12 <= 1'd0;
	statem13 <= 1'd0;
	statem14 <= 1'd0;
	statem15 <= 1'd0;
	if (SHIFT_valid_data_in) begin
		statem0 <= SHIFT_data_in0;
		statem1 <= SHIFT_data_in4;
		statem2 <= SHIFT_data_in8;
		statem3 <= SHIFT_data_in12;
		statem4 <= SHIFT_data_in1;
		statem5 <= SHIFT_data_in5;
		statem6 <= SHIFT_data_in9;
		statem7 <= SHIFT_data_in13;
		statem8 <= SHIFT_data_in2;
		statem9 <= SHIFT_data_in6;
		statem10 <= SHIFT_data_in10;
		statem11 <= SHIFT_data_in14;
		statem12 <= SHIFT_data_in3;
		statem13 <= SHIFT_data_in7;
		statem14 <= SHIFT_data_in11;
		statem15 <= SHIFT_data_in15;
	end
// synthesis translate_off
	dummy_d <= dummy_s;
// synthesis translate_on
end

// synthesis translate_off
reg dummy_d_1;
// synthesis translate_on
always @(*) begin
	SHIFT_data_out13 <= 1'd0;
	SHIFT_data_out14 <= 1'd0;
	SHIFT_data_out15 <= 1'd0;
	SHIFT_data_out0 <= 1'd0;
	SHIFT_data_out1 <= 1'd0;
	SHIFT_data_out2 <= 1'd0;
	SHIFT_data_out3 <= 1'd0;
	SHIFT_data_out4 <= 1'd0;
	SHIFT_data_out5 <= 1'd0;
	SHIFT_data_out6 <= 1'd0;
	SHIFT_data_out7 <= 1'd0;
	SHIFT_data_out8 <= 1'd0;
	SHIFT_data_out9 <= 1'd0;
	SHIFT_data_out10 <= 1'd0;
	SHIFT_data_out11 <= 1'd0;
	SHIFT_data_out12 <= 1'd0;
	if ((SHIFT_valid_data_in == 1'd1)) begin
		SHIFT_data_out0 <= statem0;
		SHIFT_data_out1 <= statem1;
		SHIFT_data_out2 <= statem2;
		SHIFT_data_out3 <= statem3;
		SHIFT_data_out4 <= statem5;
		SHIFT_data_out5 <= statem6;
		SHIFT_data_out6 <= statem7;
		SHIFT_data_out7 <= statem4;
		SHIFT_data_out8 <= statem10;
		SHIFT_data_out9 <= statem11;
		SHIFT_data_out10 <= statem8;
		SHIFT_data_out11 <= statem9;
		SHIFT_data_out12 <= statem15;
		SHIFT_data_out13 <= statem12;
		SHIFT_data_out14 <= statem13;
		SHIFT_data_out15 <= statem14;
	end
// synthesis translate_off
	dummy_d_1 <= dummy_s;
// synthesis translate_on
end
assign SHIFT_valid_data_out = 1'd1;

endmodule
