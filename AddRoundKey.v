/* Machine-generated using Migen */
module AddRoundKey(
	input [7:0] text_in0,
	input [7:0] text_in1,
	input [7:0] text_in2,
	input [7:0] text_in3,
	input [7:0] text_in4,
	input [7:0] text_in5,
	input [7:0] text_in6,
	input [7:0] text_in7,
	input [7:0] text_in8,
	input [7:0] text_in9,
	input [7:0] text_in10,
	input [7:0] text_in11,
	input [7:0] text_in12,
	input [7:0] text_in13,
	input [7:0] text_in14,
	input [7:0] text_in15,
	input [7:0] round_key_in0,
	input [7:0] round_key_in1,
	input [7:0] round_key_in2,
	input [7:0] round_key_in3,
	input [7:0] round_key_in4,
	input [7:0] round_key_in5,
	input [7:0] round_key_in6,
	input [7:0] round_key_in7,
	input [7:0] round_key_in8,
	input [7:0] round_key_in9,
	input [7:0] round_key_in10,
	input [7:0] round_key_in11,
	input [7:0] round_key_in12,
	input [7:0] round_key_in13,
	input [7:0] round_key_in14,
	input [7:0] round_key_in15,
	output reg [7:0] data_out0,
	output reg [7:0] data_out1,
	output reg [7:0] data_out2,
	output reg [7:0] data_out3,
	output reg [7:0] data_out4,
	output reg [7:0] data_out5,
	output reg [7:0] data_out6,
	output reg [7:0] data_out7,
	output reg [7:0] data_out8,
	output reg [7:0] data_out9,
	output reg [7:0] data_out10,
	output reg [7:0] data_out11,
	output reg [7:0] data_out12,
	output reg [7:0] data_out13,
	output reg [7:0] data_out14,
	output reg [7:0] data_out15,
	input sys_clk,
	input sys_rst
);

reg valid_text_in = 1'd0;
reg valid_rkey_in = 1'd0;
reg valid_data_out = 1'd0;


always @(posedge sys_clk) begin
	if (sys_rst) begin
		valid_data_out <= 1'd0;
		data_out0 <= 1'd0;
		data_out1 <= 1'd0;
		data_out2 <= 1'd0;
		data_out3 <= 1'd0;
		data_out4 <= 1'd0;
		data_out5 <= 1'd0;
		data_out6 <= 1'd0;
		data_out7 <= 1'd0;
		data_out8 <= 1'd0;
		data_out9 <= 1'd0;
		data_out10 <= 1'd0;
		data_out11 <= 1'd0;
		data_out12 <= 1'd0;
		data_out13 <= 1'd0;
		data_out14 <= 1'd0;
		data_out15 <= 1'd0;
	end else begin
		if ((valid_rkey_in == 1'd0)) begin
			data_out0 <= 1'd0;
		end else begin
			if ((valid_text_in == 1'd1)) begin
				data_out0 <= (text_in0 ^ round_key_in0);
			end
		end
		if ((valid_rkey_in == 1'd0)) begin
			data_out1 <= 1'd0;
		end else begin
			if ((valid_text_in == 1'd1)) begin
				data_out1 <= (text_in1 ^ round_key_in1);
			end
		end
		if ((valid_rkey_in == 1'd0)) begin
			data_out2 <= 1'd0;
		end else begin
			if ((valid_text_in == 1'd1)) begin
				data_out2 <= (text_in2 ^ round_key_in2);
			end
		end
		if ((valid_rkey_in == 1'd0)) begin
			data_out3 <= 1'd0;
		end else begin
			if ((valid_text_in == 1'd1)) begin
				data_out3 <= (text_in3 ^ round_key_in3);
			end
		end
		if ((valid_rkey_in == 1'd0)) begin
			data_out4 <= 1'd0;
		end else begin
			if ((valid_text_in == 1'd1)) begin
				data_out4 <= (text_in4 ^ round_key_in4);
			end
		end
		if ((valid_rkey_in == 1'd0)) begin
			data_out5 <= 1'd0;
		end else begin
			if ((valid_text_in == 1'd1)) begin
				data_out5 <= (text_in5 ^ round_key_in5);
			end
		end
		if ((valid_rkey_in == 1'd0)) begin
			data_out6 <= 1'd0;
		end else begin
			if ((valid_text_in == 1'd1)) begin
				data_out6 <= (text_in6 ^ round_key_in6);
			end
		end
		if ((valid_rkey_in == 1'd0)) begin
			data_out7 <= 1'd0;
		end else begin
			if ((valid_text_in == 1'd1)) begin
				data_out7 <= (text_in7 ^ round_key_in7);
			end
		end
		if ((valid_rkey_in == 1'd0)) begin
			data_out8 <= 1'd0;
		end else begin
			if ((valid_text_in == 1'd1)) begin
				data_out8 <= (text_in8 ^ round_key_in8);
			end
		end
		if ((valid_rkey_in == 1'd0)) begin
			data_out9 <= 1'd0;
		end else begin
			if ((valid_text_in == 1'd1)) begin
				data_out9 <= (text_in9 ^ round_key_in9);
			end
		end
		if ((valid_rkey_in == 1'd0)) begin
			data_out10 <= 1'd0;
		end else begin
			if ((valid_text_in == 1'd1)) begin
				data_out10 <= (text_in10 ^ round_key_in10);
			end
		end
		if ((valid_rkey_in == 1'd0)) begin
			data_out11 <= 1'd0;
		end else begin
			if ((valid_text_in == 1'd1)) begin
				data_out11 <= (text_in11 ^ round_key_in11);
			end
		end
		if ((valid_rkey_in == 1'd0)) begin
			data_out12 <= 1'd0;
		end else begin
			if ((valid_text_in == 1'd1)) begin
				data_out12 <= (text_in12 ^ round_key_in12);
			end
		end
		if ((valid_rkey_in == 1'd0)) begin
			data_out13 <= 1'd0;
		end else begin
			if ((valid_text_in == 1'd1)) begin
				data_out13 <= (text_in13 ^ round_key_in13);
			end
		end
		if ((valid_rkey_in == 1'd0)) begin
			data_out14 <= 1'd0;
		end else begin
			if ((valid_text_in == 1'd1)) begin
				data_out14 <= (text_in14 ^ round_key_in14);
			end
		end
		if ((valid_rkey_in == 1'd0)) begin
			data_out15 <= 1'd0;
		end else begin
			if ((valid_text_in == 1'd1)) begin
				data_out15 <= (text_in15 ^ round_key_in15);
			end
		end
		if ((valid_rkey_in == 1'd1)) begin
			valid_data_out <= 1'd1;
		end
	end
end

endmodule
