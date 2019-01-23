/* Machine-generated using Migen */
module MixColumns(
	input [7:0] data_in0,
	input [7:0] data_in1,
	input [7:0] data_in2,
	input [7:0] data_in3,
	input [7:0] data_in4,
	input [7:0] data_in5,
	input [7:0] data_in6,
	input [7:0] data_in7,
	input [7:0] data_in8,
	input [7:0] data_in9,
	input [7:0] data_in10,
	input [7:0] data_in11,
	input [7:0] data_in12,
	input [7:0] data_in13,
	input [7:0] data_in14,
	input [7:0] data_in15,
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

reg valid_in = 1'd0;
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
reg [7:0] state_mulx20 = 1'd0;
reg [7:0] state_mulx21 = 1'd0;
reg [7:0] state_mulx22 = 1'd0;
reg [7:0] state_mulx23 = 1'd0;
reg [7:0] state_mulx24 = 1'd0;
reg [7:0] state_mulx25 = 1'd0;
reg [7:0] state_mulx26 = 1'd0;
reg [7:0] state_mulx27 = 1'd0;
reg [7:0] state_mulx28 = 1'd0;
reg [7:0] state_mulx29 = 1'd0;
reg [7:0] state_mulx210 = 1'd0;
reg [7:0] state_mulx211 = 1'd0;
reg [7:0] state_mulx212 = 1'd0;
reg [7:0] state_mulx213 = 1'd0;
reg [7:0] state_mulx214 = 1'd0;
reg [7:0] state_mulx215 = 1'd0;
reg [7:0] state_mulx30 = 1'd0;
reg [7:0] state_mulx31 = 1'd0;
reg [7:0] state_mulx32 = 1'd0;
reg [7:0] state_mulx33 = 1'd0;
reg [7:0] state_mulx34 = 1'd0;
reg [7:0] state_mulx35 = 1'd0;
reg [7:0] state_mulx36 = 1'd0;
reg [7:0] state_mulx37 = 1'd0;
reg [7:0] state_mulx38 = 1'd0;
reg [7:0] state_mulx39 = 1'd0;
reg [7:0] state_mulx310 = 1'd0;
reg [7:0] state_mulx311 = 1'd0;
reg [7:0] state_mulx312 = 1'd0;
reg [7:0] state_mulx313 = 1'd0;
reg [7:0] state_mulx314 = 1'd0;
reg [7:0] state_mulx315 = 1'd0;

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
	if (valid_in) begin
		statem0 <= data_in0;
		statem1 <= data_in4;
		statem2 <= data_in8;
		statem3 <= data_in12;
		statem4 <= data_in1;
		statem5 <= data_in5;
		statem6 <= data_in9;
		statem7 <= data_in13;
		statem8 <= data_in2;
		statem9 <= data_in6;
		statem10 <= data_in10;
		statem11 <= data_in14;
		statem12 <= data_in3;
		statem13 <= data_in7;
		statem14 <= data_in11;
		statem15 <= data_in15;
	end
// synthesis translate_off
	dummy_d <= dummy_s;
// synthesis translate_on
end

// synthesis translate_off
reg dummy_d_1;
// synthesis translate_on
always @(*) begin
	state_mulx20 <= 1'd0;
	state_mulx30 <= 1'd0;
	if ((valid_in == 1'd1)) begin
		if ((statem0[7] == 1'd1)) begin
			state_mulx20 <= ((statem0 <<< 1'd1) ^ 5'd27);
		end else begin
			state_mulx20 <= (statem0 <<< 1'd1);
		end
		state_mulx30 <= (state_mulx20 ^ statem0);
	end
// synthesis translate_off
	dummy_d_1 <= dummy_s;
// synthesis translate_on
end

// synthesis translate_off
reg dummy_d_2;
// synthesis translate_on
always @(*) begin
	state_mulx21 <= 1'd0;
	state_mulx31 <= 1'd0;
	if ((valid_in == 1'd1)) begin
		if ((statem1[7] == 1'd1)) begin
			state_mulx21 <= ((statem1 <<< 1'd1) ^ 5'd27);
		end else begin
			state_mulx21 <= (statem1 <<< 1'd1);
		end
		state_mulx31 <= (state_mulx21 ^ statem1);
	end
// synthesis translate_off
	dummy_d_2 <= dummy_s;
// synthesis translate_on
end

// synthesis translate_off
reg dummy_d_3;
// synthesis translate_on
always @(*) begin
	state_mulx22 <= 1'd0;
	state_mulx32 <= 1'd0;
	if ((valid_in == 1'd1)) begin
		if ((statem2[7] == 1'd1)) begin
			state_mulx22 <= ((statem2 <<< 1'd1) ^ 5'd27);
		end else begin
			state_mulx22 <= (statem2 <<< 1'd1);
		end
		state_mulx32 <= (state_mulx22 ^ statem2);
	end
// synthesis translate_off
	dummy_d_3 <= dummy_s;
// synthesis translate_on
end

// synthesis translate_off
reg dummy_d_4;
// synthesis translate_on
always @(*) begin
	state_mulx23 <= 1'd0;
	state_mulx33 <= 1'd0;
	if ((valid_in == 1'd1)) begin
		if ((statem3[7] == 1'd1)) begin
			state_mulx23 <= ((statem3 <<< 1'd1) ^ 5'd27);
		end else begin
			state_mulx23 <= (statem3 <<< 1'd1);
		end
		state_mulx33 <= (state_mulx23 ^ statem3);
	end
// synthesis translate_off
	dummy_d_4 <= dummy_s;
// synthesis translate_on
end

// synthesis translate_off
reg dummy_d_5;
// synthesis translate_on
always @(*) begin
	state_mulx24 <= 1'd0;
	state_mulx34 <= 1'd0;
	if ((valid_in == 1'd1)) begin
		if ((statem4[7] == 1'd1)) begin
			state_mulx24 <= ((statem4 <<< 1'd1) ^ 5'd27);
		end else begin
			state_mulx24 <= (statem4 <<< 1'd1);
		end
		state_mulx34 <= (state_mulx24 ^ statem4);
	end
// synthesis translate_off
	dummy_d_5 <= dummy_s;
// synthesis translate_on
end

// synthesis translate_off
reg dummy_d_6;
// synthesis translate_on
always @(*) begin
	state_mulx25 <= 1'd0;
	state_mulx35 <= 1'd0;
	if ((valid_in == 1'd1)) begin
		if ((statem5[7] == 1'd1)) begin
			state_mulx25 <= ((statem5 <<< 1'd1) ^ 5'd27);
		end else begin
			state_mulx25 <= (statem5 <<< 1'd1);
		end
		state_mulx35 <= (state_mulx25 ^ statem5);
	end
// synthesis translate_off
	dummy_d_6 <= dummy_s;
// synthesis translate_on
end

// synthesis translate_off
reg dummy_d_7;
// synthesis translate_on
always @(*) begin
	state_mulx26 <= 1'd0;
	state_mulx36 <= 1'd0;
	if ((valid_in == 1'd1)) begin
		if ((statem6[7] == 1'd1)) begin
			state_mulx26 <= ((statem6 <<< 1'd1) ^ 5'd27);
		end else begin
			state_mulx26 <= (statem6 <<< 1'd1);
		end
		state_mulx36 <= (state_mulx26 ^ statem6);
	end
// synthesis translate_off
	dummy_d_7 <= dummy_s;
// synthesis translate_on
end

// synthesis translate_off
reg dummy_d_8;
// synthesis translate_on
always @(*) begin
	state_mulx27 <= 1'd0;
	state_mulx37 <= 1'd0;
	if ((valid_in == 1'd1)) begin
		if ((statem7[7] == 1'd1)) begin
			state_mulx27 <= ((statem7 <<< 1'd1) ^ 5'd27);
		end else begin
			state_mulx27 <= (statem7 <<< 1'd1);
		end
		state_mulx37 <= (state_mulx27 ^ statem7);
	end
// synthesis translate_off
	dummy_d_8 <= dummy_s;
// synthesis translate_on
end

// synthesis translate_off
reg dummy_d_9;
// synthesis translate_on
always @(*) begin
	state_mulx28 <= 1'd0;
	state_mulx38 <= 1'd0;
	if ((valid_in == 1'd1)) begin
		if ((statem8[7] == 1'd1)) begin
			state_mulx28 <= ((statem8 <<< 1'd1) ^ 5'd27);
		end else begin
			state_mulx28 <= (statem8 <<< 1'd1);
		end
		state_mulx38 <= (state_mulx28 ^ statem8);
	end
// synthesis translate_off
	dummy_d_9 <= dummy_s;
// synthesis translate_on
end

// synthesis translate_off
reg dummy_d_10;
// synthesis translate_on
always @(*) begin
	state_mulx29 <= 1'd0;
	state_mulx39 <= 1'd0;
	if ((valid_in == 1'd1)) begin
		if ((statem9[7] == 1'd1)) begin
			state_mulx29 <= ((statem9 <<< 1'd1) ^ 5'd27);
		end else begin
			state_mulx29 <= (statem9 <<< 1'd1);
		end
		state_mulx39 <= (state_mulx29 ^ statem9);
	end
// synthesis translate_off
	dummy_d_10 <= dummy_s;
// synthesis translate_on
end

// synthesis translate_off
reg dummy_d_11;
// synthesis translate_on
always @(*) begin
	state_mulx210 <= 1'd0;
	state_mulx310 <= 1'd0;
	if ((valid_in == 1'd1)) begin
		if ((statem10[7] == 1'd1)) begin
			state_mulx210 <= ((statem10 <<< 1'd1) ^ 5'd27);
		end else begin
			state_mulx210 <= (statem10 <<< 1'd1);
		end
		state_mulx310 <= (state_mulx210 ^ statem10);
	end
// synthesis translate_off
	dummy_d_11 <= dummy_s;
// synthesis translate_on
end

// synthesis translate_off
reg dummy_d_12;
// synthesis translate_on
always @(*) begin
	state_mulx211 <= 1'd0;
	state_mulx311 <= 1'd0;
	if ((valid_in == 1'd1)) begin
		if ((statem11[7] == 1'd1)) begin
			state_mulx211 <= ((statem11 <<< 1'd1) ^ 5'd27);
		end else begin
			state_mulx211 <= (statem11 <<< 1'd1);
		end
		state_mulx311 <= (state_mulx211 ^ statem11);
	end
// synthesis translate_off
	dummy_d_12 <= dummy_s;
// synthesis translate_on
end

// synthesis translate_off
reg dummy_d_13;
// synthesis translate_on
always @(*) begin
	state_mulx212 <= 1'd0;
	state_mulx312 <= 1'd0;
	if ((valid_in == 1'd1)) begin
		if ((statem12[7] == 1'd1)) begin
			state_mulx212 <= ((statem12 <<< 1'd1) ^ 5'd27);
		end else begin
			state_mulx212 <= (statem12 <<< 1'd1);
		end
		state_mulx312 <= (state_mulx212 ^ statem12);
	end
// synthesis translate_off
	dummy_d_13 <= dummy_s;
// synthesis translate_on
end

// synthesis translate_off
reg dummy_d_14;
// synthesis translate_on
always @(*) begin
	state_mulx213 <= 1'd0;
	state_mulx313 <= 1'd0;
	if ((valid_in == 1'd1)) begin
		if ((statem13[7] == 1'd1)) begin
			state_mulx213 <= ((statem13 <<< 1'd1) ^ 5'd27);
		end else begin
			state_mulx213 <= (statem13 <<< 1'd1);
		end
		state_mulx313 <= (state_mulx213 ^ statem13);
	end
// synthesis translate_off
	dummy_d_14 <= dummy_s;
// synthesis translate_on
end

// synthesis translate_off
reg dummy_d_15;
// synthesis translate_on
always @(*) begin
	state_mulx214 <= 1'd0;
	state_mulx314 <= 1'd0;
	if ((valid_in == 1'd1)) begin
		if ((statem14[7] == 1'd1)) begin
			state_mulx214 <= ((statem14 <<< 1'd1) ^ 5'd27);
		end else begin
			state_mulx214 <= (statem14 <<< 1'd1);
		end
		state_mulx314 <= (state_mulx214 ^ statem14);
	end
// synthesis translate_off
	dummy_d_15 <= dummy_s;
// synthesis translate_on
end

// synthesis translate_off
reg dummy_d_16;
// synthesis translate_on
always @(*) begin
	state_mulx215 <= 1'd0;
	state_mulx315 <= 1'd0;
	if ((valid_in == 1'd1)) begin
		if ((statem15[7] == 1'd1)) begin
			state_mulx215 <= ((statem15 <<< 1'd1) ^ 5'd27);
		end else begin
			state_mulx215 <= (statem15 <<< 1'd1);
		end
		state_mulx315 <= (state_mulx215 ^ statem15);
	end
// synthesis translate_off
	dummy_d_16 <= dummy_s;
// synthesis translate_on
end

always @(posedge sys_clk) begin
	if (sys_rst) begin
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
		if ((valid_in == 1'd1)) begin
			data_out15 <= (((state_mulx20 ^ state_mulx31) ^ statem2) ^ statem3);
			data_out14 <= (((statem0 ^ state_mulx21) ^ state_mulx32) ^ statem3);
			data_out13 <= (((statem0 ^ statem1) ^ state_mulx22) ^ state_mulx33);
			data_out12 <= (((state_mulx30 ^ statem1) ^ statem2) ^ state_mulx33);
			data_out11 <= (((state_mulx24 ^ state_mulx35) ^ statem6) ^ statem7);
			data_out10 <= (((statem4 ^ state_mulx25) ^ state_mulx36) ^ statem3);
			data_out9 <= (((statem4 ^ statem5) ^ state_mulx26) ^ state_mulx33);
			data_out8 <= (((state_mulx34 ^ statem5) ^ statem6) ^ state_mulx33);
			data_out7 <= (((state_mulx28 ^ state_mulx39) ^ statem10) ^ statem11);
			data_out6 <= (((statem8 ^ state_mulx29) ^ state_mulx310) ^ statem3);
			data_out5 <= (((statem8 ^ statem9) ^ state_mulx210) ^ state_mulx33);
			data_out4 <= (((state_mulx38 ^ statem9) ^ statem10) ^ state_mulx33);
			data_out3 <= (((state_mulx212 ^ state_mulx313) ^ statem14) ^ statem15);
			data_out2 <= (((statem12 ^ state_mulx213) ^ state_mulx314) ^ statem15);
			data_out1 <= (((statem12 ^ statem13) ^ state_mulx214) ^ state_mulx315);
			data_out0 <= (((state_mulx312 ^ statem13) ^ statem14) ^ state_mulx315);
		end
	end
end

endmodule
