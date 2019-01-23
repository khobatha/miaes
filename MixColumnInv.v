/* Machine-generated using Migen */
module MixColumnInv(
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
	output [7:0] recovered0,
	output [7:0] recovered1,
	output [7:0] recovered2,
	output [7:0] recovered3,
	output [7:0] recovered4,
	output [7:0] recovered5,
	output [7:0] recovered6,
	output [7:0] recovered7,
	output [7:0] recovered8,
	output [7:0] recovered9,
	output [7:0] recovered10,
	output [7:0] recovered11,
	output [7:0] recovered12,
	output [7:0] recovered13,
	output [7:0] recovered14,
	output [7:0] recovered15,
	input sys_clk,
	input sys_rst
);

reg [7:0] adr = 1'd0;
wire [7:0] dat_r;

// synthesis translate_off
reg dummy_s;
initial dummy_s <= 1'd0;
// synthesis translate_on
assign recovered0 = dat_r;
assign recovered1 = dat_r;
assign recovered2 = dat_r;
assign recovered3 = dat_r;
assign recovered4 = dat_r;
assign recovered5 = dat_r;
assign recovered6 = dat_r;
assign recovered7 = dat_r;
assign recovered8 = dat_r;
assign recovered9 = dat_r;
assign recovered10 = dat_r;
assign recovered11 = dat_r;
assign recovered12 = dat_r;
assign recovered13 = dat_r;
assign recovered14 = dat_r;

// synthesis translate_off
reg dummy_d;
// synthesis translate_on
always @(*) begin
	adr <= 1'd0;
	adr <= 1'd0;
	adr <= 1'd1;
	adr <= 2'd2;
	adr <= 2'd3;
	adr <= 3'd4;
	adr <= 3'd5;
	adr <= 3'd6;
	adr <= 3'd7;
	adr <= 4'd8;
	adr <= 4'd9;
	adr <= 4'd10;
	adr <= 4'd11;
	adr <= 4'd12;
	adr <= 4'd13;
	adr <= 4'd14;
	adr <= 4'd15;
// synthesis translate_off
	dummy_d <= dummy_s;
// synthesis translate_on
end
assign recovered15 = dat_r;

reg [7:0] invsboxmem[0:255];
reg [7:0] memdat;
always @(posedge sys_clk) begin
	memdat <= invsboxmem[adr];
end

assign dat_r = memdat;

initial begin
	$readmemh("invsboxmem.init", invsboxmem);
end

endmodule
