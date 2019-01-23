/* Machine-generated using Migen */
module SubBytes(
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

reg [7:0] bytescount = 1'd0;
reg valid_in = 1'd0;
reg valid_out = 1'd0;
reg [7:0] adr = 1'd0;
wire [7:0] dat_r;


always @(posedge sys_clk) begin
	if (sys_rst) begin
		valid_out <= 1'd0;
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
		adr <= 1'd0;
	end else begin
		if (valid_in) begin
			if ((data_in0 == 1'd0)) begin
				adr <= data_in0;
				data_out0 <= dat_r;
			end else begin
				if ((data_in0 == 6'd49)) begin
					adr <= data_in0;
					data_out0 <= dat_r;
				end else begin
					if ((data_in0 == 6'd50)) begin
						adr <= data_in0;
						data_out0 <= dat_r;
					end else begin
						if ((data_in0 == 6'd51)) begin
							adr <= data_in0;
							data_out0 <= dat_r;
						end else begin
							if ((data_in0 == 6'd52)) begin
								adr <= data_in0;
								data_out0 <= dat_r;
							end else begin
								if ((data_in0 == 6'd53)) begin
									adr <= data_in0;
									data_out0 <= dat_r;
								end else begin
									if ((data_in0 == 6'd54)) begin
										adr <= data_in0;
										data_out0 <= dat_r;
									end else begin
										if ((data_in0 == 6'd55)) begin
											adr <= data_in0;
											data_out0 <= dat_r;
										end else begin
											if ((data_in0 == 6'd56)) begin
												adr <= data_in0;
												data_out0 <= dat_r;
											end else begin
												if ((data_in0 == 6'd57)) begin
													adr <= data_in0;
													data_out0 <= dat_r;
												end else begin
													if ((data_in0 == 7'd64)) begin
														adr <= data_in0;
														data_out0 <= dat_r;
													end else begin
														if ((data_in0 == 7'd65)) begin
															adr <= data_in0;
															data_out0 <= dat_r;
														end else begin
															if ((data_in0 == 7'd66)) begin
																adr <= data_in0;
																data_out0 <= dat_r;
															end else begin
																if ((data_in0 == 7'd67)) begin
																	adr <= data_in0;
																	data_out0 <= dat_r;
																end else begin
																	if ((data_in0 == 7'd68)) begin
																		adr <= data_in0;
																		data_out0 <= dat_r;
																	end else begin
																		if ((data_in0 == 7'd69)) begin
																			adr <= data_in0;
																			data_out0 <= dat_r;
																		end else begin
																			if ((data_in0 == 7'd70)) begin
																				adr <= data_in0;
																				data_out0 <= dat_r;
																			end else begin
																				if ((data_in0 == 7'd71)) begin
																					adr <= data_in0;
																					data_out0 <= dat_r;
																				end else begin
																					if ((data_in0 == 7'd72)) begin
																						adr <= data_in0;
																						data_out0 <= dat_r;
																					end else begin
																						if ((data_in0 == 7'd73)) begin
																							adr <= data_in0;
																							data_out0 <= dat_r;
																						end else begin
																							if ((data_in0 == 7'd80)) begin
																								adr <= data_in0;
																								data_out0 <= dat_r;
																							end else begin
																								if ((data_in0 == 7'd81)) begin
																									adr <= data_in0;
																									data_out0 <= dat_r;
																								end else begin
																									data_out0 <= 1'd0;
																								end
																							end
																						end
																					end
																				end
																			end
																		end
																	end
																end
															end
														end
													end
												end
											end
										end
									end
								end
							end
						end
					end
				end
			end
		end
		if (valid_in) begin
			if ((data_in1 == 1'd0)) begin
				adr <= data_in1;
				data_out1 <= dat_r;
			end else begin
				if ((data_in1 == 6'd49)) begin
					adr <= data_in1;
					data_out1 <= dat_r;
				end else begin
					if ((data_in1 == 6'd50)) begin
						adr <= data_in1;
						data_out1 <= dat_r;
					end else begin
						if ((data_in1 == 6'd51)) begin
							adr <= data_in1;
							data_out1 <= dat_r;
						end else begin
							if ((data_in1 == 6'd52)) begin
								adr <= data_in1;
								data_out1 <= dat_r;
							end else begin
								if ((data_in1 == 6'd53)) begin
									adr <= data_in1;
									data_out1 <= dat_r;
								end else begin
									if ((data_in1 == 6'd54)) begin
										adr <= data_in1;
										data_out1 <= dat_r;
									end else begin
										if ((data_in1 == 6'd55)) begin
											adr <= data_in1;
											data_out1 <= dat_r;
										end else begin
											if ((data_in1 == 6'd56)) begin
												adr <= data_in1;
												data_out1 <= dat_r;
											end else begin
												if ((data_in1 == 6'd57)) begin
													adr <= data_in1;
													data_out1 <= dat_r;
												end else begin
													if ((data_in1 == 7'd64)) begin
														adr <= data_in1;
														data_out1 <= dat_r;
													end else begin
														if ((data_in1 == 7'd65)) begin
															adr <= data_in1;
															data_out1 <= dat_r;
														end else begin
															if ((data_in1 == 7'd66)) begin
																adr <= data_in1;
																data_out1 <= dat_r;
															end else begin
																if ((data_in1 == 7'd67)) begin
																	adr <= data_in1;
																	data_out1 <= dat_r;
																end else begin
																	if ((data_in1 == 7'd68)) begin
																		adr <= data_in1;
																		data_out1 <= dat_r;
																	end else begin
																		if ((data_in1 == 7'd69)) begin
																			adr <= data_in1;
																			data_out1 <= dat_r;
																		end else begin
																			if ((data_in1 == 7'd70)) begin
																				adr <= data_in1;
																				data_out1 <= dat_r;
																			end else begin
																				if ((data_in1 == 7'd71)) begin
																					adr <= data_in1;
																					data_out1 <= dat_r;
																				end else begin
																					if ((data_in1 == 7'd72)) begin
																						adr <= data_in1;
																						data_out1 <= dat_r;
																					end else begin
																						if ((data_in1 == 7'd73)) begin
																							adr <= data_in1;
																							data_out1 <= dat_r;
																						end else begin
																							if ((data_in1 == 7'd80)) begin
																								adr <= data_in1;
																								data_out1 <= dat_r;
																							end else begin
																								if ((data_in1 == 7'd81)) begin
																									adr <= data_in1;
																									data_out1 <= dat_r;
																								end else begin
																									data_out1 <= 1'd0;
																								end
																							end
																						end
																					end
																				end
																			end
																		end
																	end
																end
															end
														end
													end
												end
											end
										end
									end
								end
							end
						end
					end
				end
			end
		end
		if (valid_in) begin
			if ((data_in2 == 1'd0)) begin
				adr <= data_in2;
				data_out2 <= dat_r;
			end else begin
				if ((data_in2 == 6'd49)) begin
					adr <= data_in2;
					data_out2 <= dat_r;
				end else begin
					if ((data_in2 == 6'd50)) begin
						adr <= data_in2;
						data_out2 <= dat_r;
					end else begin
						if ((data_in2 == 6'd51)) begin
							adr <= data_in2;
							data_out2 <= dat_r;
						end else begin
							if ((data_in2 == 6'd52)) begin
								adr <= data_in2;
								data_out2 <= dat_r;
							end else begin
								if ((data_in2 == 6'd53)) begin
									adr <= data_in2;
									data_out2 <= dat_r;
								end else begin
									if ((data_in2 == 6'd54)) begin
										adr <= data_in2;
										data_out2 <= dat_r;
									end else begin
										if ((data_in2 == 6'd55)) begin
											adr <= data_in2;
											data_out2 <= dat_r;
										end else begin
											if ((data_in2 == 6'd56)) begin
												adr <= data_in2;
												data_out2 <= dat_r;
											end else begin
												if ((data_in2 == 6'd57)) begin
													adr <= data_in2;
													data_out2 <= dat_r;
												end else begin
													if ((data_in2 == 7'd64)) begin
														adr <= data_in2;
														data_out2 <= dat_r;
													end else begin
														if ((data_in2 == 7'd65)) begin
															adr <= data_in2;
															data_out2 <= dat_r;
														end else begin
															if ((data_in2 == 7'd66)) begin
																adr <= data_in2;
																data_out2 <= dat_r;
															end else begin
																if ((data_in2 == 7'd67)) begin
																	adr <= data_in2;
																	data_out2 <= dat_r;
																end else begin
																	if ((data_in2 == 7'd68)) begin
																		adr <= data_in2;
																		data_out2 <= dat_r;
																	end else begin
																		if ((data_in2 == 7'd69)) begin
																			adr <= data_in2;
																			data_out2 <= dat_r;
																		end else begin
																			if ((data_in2 == 7'd70)) begin
																				adr <= data_in2;
																				data_out2 <= dat_r;
																			end else begin
																				if ((data_in2 == 7'd71)) begin
																					adr <= data_in2;
																					data_out2 <= dat_r;
																				end else begin
																					if ((data_in2 == 7'd72)) begin
																						adr <= data_in2;
																						data_out2 <= dat_r;
																					end else begin
																						if ((data_in2 == 7'd73)) begin
																							adr <= data_in2;
																							data_out2 <= dat_r;
																						end else begin
																							if ((data_in2 == 7'd80)) begin
																								adr <= data_in2;
																								data_out2 <= dat_r;
																							end else begin
																								if ((data_in2 == 7'd81)) begin
																									adr <= data_in2;
																									data_out2 <= dat_r;
																								end else begin
																									data_out2 <= 1'd0;
																								end
																							end
																						end
																					end
																				end
																			end
																		end
																	end
																end
															end
														end
													end
												end
											end
										end
									end
								end
							end
						end
					end
				end
			end
		end
		if (valid_in) begin
			if ((data_in3 == 1'd0)) begin
				adr <= data_in3;
				data_out3 <= dat_r;
			end else begin
				if ((data_in3 == 6'd49)) begin
					adr <= data_in3;
					data_out3 <= dat_r;
				end else begin
					if ((data_in3 == 6'd50)) begin
						adr <= data_in3;
						data_out3 <= dat_r;
					end else begin
						if ((data_in3 == 6'd51)) begin
							adr <= data_in3;
							data_out3 <= dat_r;
						end else begin
							if ((data_in3 == 6'd52)) begin
								adr <= data_in3;
								data_out3 <= dat_r;
							end else begin
								if ((data_in3 == 6'd53)) begin
									adr <= data_in3;
									data_out3 <= dat_r;
								end else begin
									if ((data_in3 == 6'd54)) begin
										adr <= data_in3;
										data_out3 <= dat_r;
									end else begin
										if ((data_in3 == 6'd55)) begin
											adr <= data_in3;
											data_out3 <= dat_r;
										end else begin
											if ((data_in3 == 6'd56)) begin
												adr <= data_in3;
												data_out3 <= dat_r;
											end else begin
												if ((data_in3 == 6'd57)) begin
													adr <= data_in3;
													data_out3 <= dat_r;
												end else begin
													if ((data_in3 == 7'd64)) begin
														adr <= data_in3;
														data_out3 <= dat_r;
													end else begin
														if ((data_in3 == 7'd65)) begin
															adr <= data_in3;
															data_out3 <= dat_r;
														end else begin
															if ((data_in3 == 7'd66)) begin
																adr <= data_in3;
																data_out3 <= dat_r;
															end else begin
																if ((data_in3 == 7'd67)) begin
																	adr <= data_in3;
																	data_out3 <= dat_r;
																end else begin
																	if ((data_in3 == 7'd68)) begin
																		adr <= data_in3;
																		data_out3 <= dat_r;
																	end else begin
																		if ((data_in3 == 7'd69)) begin
																			adr <= data_in3;
																			data_out3 <= dat_r;
																		end else begin
																			if ((data_in3 == 7'd70)) begin
																				adr <= data_in3;
																				data_out3 <= dat_r;
																			end else begin
																				if ((data_in3 == 7'd71)) begin
																					adr <= data_in3;
																					data_out3 <= dat_r;
																				end else begin
																					if ((data_in3 == 7'd72)) begin
																						adr <= data_in3;
																						data_out3 <= dat_r;
																					end else begin
																						if ((data_in3 == 7'd73)) begin
																							adr <= data_in3;
																							data_out3 <= dat_r;
																						end else begin
																							if ((data_in3 == 7'd80)) begin
																								adr <= data_in3;
																								data_out3 <= dat_r;
																							end else begin
																								if ((data_in3 == 7'd81)) begin
																									adr <= data_in3;
																									data_out3 <= dat_r;
																								end else begin
																									data_out3 <= 1'd0;
																								end
																							end
																						end
																					end
																				end
																			end
																		end
																	end
																end
															end
														end
													end
												end
											end
										end
									end
								end
							end
						end
					end
				end
			end
		end
		if (valid_in) begin
			if ((data_in4 == 1'd0)) begin
				adr <= data_in4;
				data_out4 <= dat_r;
			end else begin
				if ((data_in4 == 6'd49)) begin
					adr <= data_in4;
					data_out4 <= dat_r;
				end else begin
					if ((data_in4 == 6'd50)) begin
						adr <= data_in4;
						data_out4 <= dat_r;
					end else begin
						if ((data_in4 == 6'd51)) begin
							adr <= data_in4;
							data_out4 <= dat_r;
						end else begin
							if ((data_in4 == 6'd52)) begin
								adr <= data_in4;
								data_out4 <= dat_r;
							end else begin
								if ((data_in4 == 6'd53)) begin
									adr <= data_in4;
									data_out4 <= dat_r;
								end else begin
									if ((data_in4 == 6'd54)) begin
										adr <= data_in4;
										data_out4 <= dat_r;
									end else begin
										if ((data_in4 == 6'd55)) begin
											adr <= data_in4;
											data_out4 <= dat_r;
										end else begin
											if ((data_in4 == 6'd56)) begin
												adr <= data_in4;
												data_out4 <= dat_r;
											end else begin
												if ((data_in4 == 6'd57)) begin
													adr <= data_in4;
													data_out4 <= dat_r;
												end else begin
													if ((data_in4 == 7'd64)) begin
														adr <= data_in4;
														data_out4 <= dat_r;
													end else begin
														if ((data_in4 == 7'd65)) begin
															adr <= data_in4;
															data_out4 <= dat_r;
														end else begin
															if ((data_in4 == 7'd66)) begin
																adr <= data_in4;
																data_out4 <= dat_r;
															end else begin
																if ((data_in4 == 7'd67)) begin
																	adr <= data_in4;
																	data_out4 <= dat_r;
																end else begin
																	if ((data_in4 == 7'd68)) begin
																		adr <= data_in4;
																		data_out4 <= dat_r;
																	end else begin
																		if ((data_in4 == 7'd69)) begin
																			adr <= data_in4;
																			data_out4 <= dat_r;
																		end else begin
																			if ((data_in4 == 7'd70)) begin
																				adr <= data_in4;
																				data_out4 <= dat_r;
																			end else begin
																				if ((data_in4 == 7'd71)) begin
																					adr <= data_in4;
																					data_out4 <= dat_r;
																				end else begin
																					if ((data_in4 == 7'd72)) begin
																						adr <= data_in4;
																						data_out4 <= dat_r;
																					end else begin
																						if ((data_in4 == 7'd73)) begin
																							adr <= data_in4;
																							data_out4 <= dat_r;
																						end else begin
																							if ((data_in4 == 7'd80)) begin
																								adr <= data_in4;
																								data_out4 <= dat_r;
																							end else begin
																								if ((data_in4 == 7'd81)) begin
																									adr <= data_in4;
																									data_out4 <= dat_r;
																								end else begin
																									data_out4 <= 1'd0;
																								end
																							end
																						end
																					end
																				end
																			end
																		end
																	end
																end
															end
														end
													end
												end
											end
										end
									end
								end
							end
						end
					end
				end
			end
		end
		if (valid_in) begin
			if ((data_in5 == 1'd0)) begin
				adr <= data_in5;
				data_out5 <= dat_r;
			end else begin
				if ((data_in5 == 6'd49)) begin
					adr <= data_in5;
					data_out5 <= dat_r;
				end else begin
					if ((data_in5 == 6'd50)) begin
						adr <= data_in5;
						data_out5 <= dat_r;
					end else begin
						if ((data_in5 == 6'd51)) begin
							adr <= data_in5;
							data_out5 <= dat_r;
						end else begin
							if ((data_in5 == 6'd52)) begin
								adr <= data_in5;
								data_out5 <= dat_r;
							end else begin
								if ((data_in5 == 6'd53)) begin
									adr <= data_in5;
									data_out5 <= dat_r;
								end else begin
									if ((data_in5 == 6'd54)) begin
										adr <= data_in5;
										data_out5 <= dat_r;
									end else begin
										if ((data_in5 == 6'd55)) begin
											adr <= data_in5;
											data_out5 <= dat_r;
										end else begin
											if ((data_in5 == 6'd56)) begin
												adr <= data_in5;
												data_out5 <= dat_r;
											end else begin
												if ((data_in5 == 6'd57)) begin
													adr <= data_in5;
													data_out5 <= dat_r;
												end else begin
													if ((data_in5 == 7'd64)) begin
														adr <= data_in5;
														data_out5 <= dat_r;
													end else begin
														if ((data_in5 == 7'd65)) begin
															adr <= data_in5;
															data_out5 <= dat_r;
														end else begin
															if ((data_in5 == 7'd66)) begin
																adr <= data_in5;
																data_out5 <= dat_r;
															end else begin
																if ((data_in5 == 7'd67)) begin
																	adr <= data_in5;
																	data_out5 <= dat_r;
																end else begin
																	if ((data_in5 == 7'd68)) begin
																		adr <= data_in5;
																		data_out5 <= dat_r;
																	end else begin
																		if ((data_in5 == 7'd69)) begin
																			adr <= data_in5;
																			data_out5 <= dat_r;
																		end else begin
																			if ((data_in5 == 7'd70)) begin
																				adr <= data_in5;
																				data_out5 <= dat_r;
																			end else begin
																				if ((data_in5 == 7'd71)) begin
																					adr <= data_in5;
																					data_out5 <= dat_r;
																				end else begin
																					if ((data_in5 == 7'd72)) begin
																						adr <= data_in5;
																						data_out5 <= dat_r;
																					end else begin
																						if ((data_in5 == 7'd73)) begin
																							adr <= data_in5;
																							data_out5 <= dat_r;
																						end else begin
																							if ((data_in5 == 7'd80)) begin
																								adr <= data_in5;
																								data_out5 <= dat_r;
																							end else begin
																								if ((data_in5 == 7'd81)) begin
																									adr <= data_in5;
																									data_out5 <= dat_r;
																								end else begin
																									data_out5 <= 1'd0;
																								end
																							end
																						end
																					end
																				end
																			end
																		end
																	end
																end
															end
														end
													end
												end
											end
										end
									end
								end
							end
						end
					end
				end
			end
		end
		if (valid_in) begin
			if ((data_in6 == 1'd0)) begin
				adr <= data_in6;
				data_out6 <= dat_r;
			end else begin
				if ((data_in6 == 6'd49)) begin
					adr <= data_in6;
					data_out6 <= dat_r;
				end else begin
					if ((data_in6 == 6'd50)) begin
						adr <= data_in6;
						data_out6 <= dat_r;
					end else begin
						if ((data_in6 == 6'd51)) begin
							adr <= data_in6;
							data_out6 <= dat_r;
						end else begin
							if ((data_in6 == 6'd52)) begin
								adr <= data_in6;
								data_out6 <= dat_r;
							end else begin
								if ((data_in6 == 6'd53)) begin
									adr <= data_in6;
									data_out6 <= dat_r;
								end else begin
									if ((data_in6 == 6'd54)) begin
										adr <= data_in6;
										data_out6 <= dat_r;
									end else begin
										if ((data_in6 == 6'd55)) begin
											adr <= data_in6;
											data_out6 <= dat_r;
										end else begin
											if ((data_in6 == 6'd56)) begin
												adr <= data_in6;
												data_out6 <= dat_r;
											end else begin
												if ((data_in6 == 6'd57)) begin
													adr <= data_in6;
													data_out6 <= dat_r;
												end else begin
													if ((data_in6 == 7'd64)) begin
														adr <= data_in6;
														data_out6 <= dat_r;
													end else begin
														if ((data_in6 == 7'd65)) begin
															adr <= data_in6;
															data_out6 <= dat_r;
														end else begin
															if ((data_in6 == 7'd66)) begin
																adr <= data_in6;
																data_out6 <= dat_r;
															end else begin
																if ((data_in6 == 7'd67)) begin
																	adr <= data_in6;
																	data_out6 <= dat_r;
																end else begin
																	if ((data_in6 == 7'd68)) begin
																		adr <= data_in6;
																		data_out6 <= dat_r;
																	end else begin
																		if ((data_in6 == 7'd69)) begin
																			adr <= data_in6;
																			data_out6 <= dat_r;
																		end else begin
																			if ((data_in6 == 7'd70)) begin
																				adr <= data_in6;
																				data_out6 <= dat_r;
																			end else begin
																				if ((data_in6 == 7'd71)) begin
																					adr <= data_in6;
																					data_out6 <= dat_r;
																				end else begin
																					if ((data_in6 == 7'd72)) begin
																						adr <= data_in6;
																						data_out6 <= dat_r;
																					end else begin
																						if ((data_in6 == 7'd73)) begin
																							adr <= data_in6;
																							data_out6 <= dat_r;
																						end else begin
																							if ((data_in6 == 7'd80)) begin
																								adr <= data_in6;
																								data_out6 <= dat_r;
																							end else begin
																								if ((data_in6 == 7'd81)) begin
																									adr <= data_in6;
																									data_out6 <= dat_r;
																								end else begin
																									data_out6 <= 1'd0;
																								end
																							end
																						end
																					end
																				end
																			end
																		end
																	end
																end
															end
														end
													end
												end
											end
										end
									end
								end
							end
						end
					end
				end
			end
		end
		if (valid_in) begin
			if ((data_in7 == 1'd0)) begin
				adr <= data_in7;
				data_out7 <= dat_r;
			end else begin
				if ((data_in7 == 6'd49)) begin
					adr <= data_in7;
					data_out7 <= dat_r;
				end else begin
					if ((data_in7 == 6'd50)) begin
						adr <= data_in7;
						data_out7 <= dat_r;
					end else begin
						if ((data_in7 == 6'd51)) begin
							adr <= data_in7;
							data_out7 <= dat_r;
						end else begin
							if ((data_in7 == 6'd52)) begin
								adr <= data_in7;
								data_out7 <= dat_r;
							end else begin
								if ((data_in7 == 6'd53)) begin
									adr <= data_in7;
									data_out7 <= dat_r;
								end else begin
									if ((data_in7 == 6'd54)) begin
										adr <= data_in7;
										data_out7 <= dat_r;
									end else begin
										if ((data_in7 == 6'd55)) begin
											adr <= data_in7;
											data_out7 <= dat_r;
										end else begin
											if ((data_in7 == 6'd56)) begin
												adr <= data_in7;
												data_out7 <= dat_r;
											end else begin
												if ((data_in7 == 6'd57)) begin
													adr <= data_in7;
													data_out7 <= dat_r;
												end else begin
													if ((data_in7 == 7'd64)) begin
														adr <= data_in7;
														data_out7 <= dat_r;
													end else begin
														if ((data_in7 == 7'd65)) begin
															adr <= data_in7;
															data_out7 <= dat_r;
														end else begin
															if ((data_in7 == 7'd66)) begin
																adr <= data_in7;
																data_out7 <= dat_r;
															end else begin
																if ((data_in7 == 7'd67)) begin
																	adr <= data_in7;
																	data_out7 <= dat_r;
																end else begin
																	if ((data_in7 == 7'd68)) begin
																		adr <= data_in7;
																		data_out7 <= dat_r;
																	end else begin
																		if ((data_in7 == 7'd69)) begin
																			adr <= data_in7;
																			data_out7 <= dat_r;
																		end else begin
																			if ((data_in7 == 7'd70)) begin
																				adr <= data_in7;
																				data_out7 <= dat_r;
																			end else begin
																				if ((data_in7 == 7'd71)) begin
																					adr <= data_in7;
																					data_out7 <= dat_r;
																				end else begin
																					if ((data_in7 == 7'd72)) begin
																						adr <= data_in7;
																						data_out7 <= dat_r;
																					end else begin
																						if ((data_in7 == 7'd73)) begin
																							adr <= data_in7;
																							data_out7 <= dat_r;
																						end else begin
																							if ((data_in7 == 7'd80)) begin
																								adr <= data_in7;
																								data_out7 <= dat_r;
																							end else begin
																								if ((data_in7 == 7'd81)) begin
																									adr <= data_in7;
																									data_out7 <= dat_r;
																								end else begin
																									data_out7 <= 1'd0;
																								end
																							end
																						end
																					end
																				end
																			end
																		end
																	end
																end
															end
														end
													end
												end
											end
										end
									end
								end
							end
						end
					end
				end
			end
		end
		if (valid_in) begin
			if ((data_in8 == 1'd0)) begin
				adr <= data_in8;
				data_out8 <= dat_r;
			end else begin
				if ((data_in8 == 6'd49)) begin
					adr <= data_in8;
					data_out8 <= dat_r;
				end else begin
					if ((data_in8 == 6'd50)) begin
						adr <= data_in8;
						data_out8 <= dat_r;
					end else begin
						if ((data_in8 == 6'd51)) begin
							adr <= data_in8;
							data_out8 <= dat_r;
						end else begin
							if ((data_in8 == 6'd52)) begin
								adr <= data_in8;
								data_out8 <= dat_r;
							end else begin
								if ((data_in8 == 6'd53)) begin
									adr <= data_in8;
									data_out8 <= dat_r;
								end else begin
									if ((data_in8 == 6'd54)) begin
										adr <= data_in8;
										data_out8 <= dat_r;
									end else begin
										if ((data_in8 == 6'd55)) begin
											adr <= data_in8;
											data_out8 <= dat_r;
										end else begin
											if ((data_in8 == 6'd56)) begin
												adr <= data_in8;
												data_out8 <= dat_r;
											end else begin
												if ((data_in8 == 6'd57)) begin
													adr <= data_in8;
													data_out8 <= dat_r;
												end else begin
													if ((data_in8 == 7'd64)) begin
														adr <= data_in8;
														data_out8 <= dat_r;
													end else begin
														if ((data_in8 == 7'd65)) begin
															adr <= data_in8;
															data_out8 <= dat_r;
														end else begin
															if ((data_in8 == 7'd66)) begin
																adr <= data_in8;
																data_out8 <= dat_r;
															end else begin
																if ((data_in8 == 7'd67)) begin
																	adr <= data_in8;
																	data_out8 <= dat_r;
																end else begin
																	if ((data_in8 == 7'd68)) begin
																		adr <= data_in8;
																		data_out8 <= dat_r;
																	end else begin
																		if ((data_in8 == 7'd69)) begin
																			adr <= data_in8;
																			data_out8 <= dat_r;
																		end else begin
																			if ((data_in8 == 7'd70)) begin
																				adr <= data_in8;
																				data_out8 <= dat_r;
																			end else begin
																				if ((data_in8 == 7'd71)) begin
																					adr <= data_in8;
																					data_out8 <= dat_r;
																				end else begin
																					if ((data_in8 == 7'd72)) begin
																						adr <= data_in8;
																						data_out8 <= dat_r;
																					end else begin
																						if ((data_in8 == 7'd73)) begin
																							adr <= data_in8;
																							data_out8 <= dat_r;
																						end else begin
																							if ((data_in8 == 7'd80)) begin
																								adr <= data_in8;
																								data_out8 <= dat_r;
																							end else begin
																								if ((data_in8 == 7'd81)) begin
																									adr <= data_in8;
																									data_out8 <= dat_r;
																								end else begin
																									data_out8 <= 1'd0;
																								end
																							end
																						end
																					end
																				end
																			end
																		end
																	end
																end
															end
														end
													end
												end
											end
										end
									end
								end
							end
						end
					end
				end
			end
		end
		if (valid_in) begin
			if ((data_in9 == 1'd0)) begin
				adr <= data_in9;
				data_out9 <= dat_r;
			end else begin
				if ((data_in9 == 6'd49)) begin
					adr <= data_in9;
					data_out9 <= dat_r;
				end else begin
					if ((data_in9 == 6'd50)) begin
						adr <= data_in9;
						data_out9 <= dat_r;
					end else begin
						if ((data_in9 == 6'd51)) begin
							adr <= data_in9;
							data_out9 <= dat_r;
						end else begin
							if ((data_in9 == 6'd52)) begin
								adr <= data_in9;
								data_out9 <= dat_r;
							end else begin
								if ((data_in9 == 6'd53)) begin
									adr <= data_in9;
									data_out9 <= dat_r;
								end else begin
									if ((data_in9 == 6'd54)) begin
										adr <= data_in9;
										data_out9 <= dat_r;
									end else begin
										if ((data_in9 == 6'd55)) begin
											adr <= data_in9;
											data_out9 <= dat_r;
										end else begin
											if ((data_in9 == 6'd56)) begin
												adr <= data_in9;
												data_out9 <= dat_r;
											end else begin
												if ((data_in9 == 6'd57)) begin
													adr <= data_in9;
													data_out9 <= dat_r;
												end else begin
													if ((data_in9 == 7'd64)) begin
														adr <= data_in9;
														data_out9 <= dat_r;
													end else begin
														if ((data_in9 == 7'd65)) begin
															adr <= data_in9;
															data_out9 <= dat_r;
														end else begin
															if ((data_in9 == 7'd66)) begin
																adr <= data_in9;
																data_out9 <= dat_r;
															end else begin
																if ((data_in9 == 7'd67)) begin
																	adr <= data_in9;
																	data_out9 <= dat_r;
																end else begin
																	if ((data_in9 == 7'd68)) begin
																		adr <= data_in9;
																		data_out9 <= dat_r;
																	end else begin
																		if ((data_in9 == 7'd69)) begin
																			adr <= data_in9;
																			data_out9 <= dat_r;
																		end else begin
																			if ((data_in9 == 7'd70)) begin
																				adr <= data_in9;
																				data_out9 <= dat_r;
																			end else begin
																				if ((data_in9 == 7'd71)) begin
																					adr <= data_in9;
																					data_out9 <= dat_r;
																				end else begin
																					if ((data_in9 == 7'd72)) begin
																						adr <= data_in9;
																						data_out9 <= dat_r;
																					end else begin
																						if ((data_in9 == 7'd73)) begin
																							adr <= data_in9;
																							data_out9 <= dat_r;
																						end else begin
																							if ((data_in9 == 7'd80)) begin
																								adr <= data_in9;
																								data_out9 <= dat_r;
																							end else begin
																								if ((data_in9 == 7'd81)) begin
																									adr <= data_in9;
																									data_out9 <= dat_r;
																								end else begin
																									data_out9 <= 1'd0;
																								end
																							end
																						end
																					end
																				end
																			end
																		end
																	end
																end
															end
														end
													end
												end
											end
										end
									end
								end
							end
						end
					end
				end
			end
		end
		if (valid_in) begin
			if ((data_in10 == 1'd0)) begin
				adr <= data_in10;
				data_out10 <= dat_r;
			end else begin
				if ((data_in10 == 6'd49)) begin
					adr <= data_in10;
					data_out10 <= dat_r;
				end else begin
					if ((data_in10 == 6'd50)) begin
						adr <= data_in10;
						data_out10 <= dat_r;
					end else begin
						if ((data_in10 == 6'd51)) begin
							adr <= data_in10;
							data_out10 <= dat_r;
						end else begin
							if ((data_in10 == 6'd52)) begin
								adr <= data_in10;
								data_out10 <= dat_r;
							end else begin
								if ((data_in10 == 6'd53)) begin
									adr <= data_in10;
									data_out10 <= dat_r;
								end else begin
									if ((data_in10 == 6'd54)) begin
										adr <= data_in10;
										data_out10 <= dat_r;
									end else begin
										if ((data_in10 == 6'd55)) begin
											adr <= data_in10;
											data_out10 <= dat_r;
										end else begin
											if ((data_in10 == 6'd56)) begin
												adr <= data_in10;
												data_out10 <= dat_r;
											end else begin
												if ((data_in10 == 6'd57)) begin
													adr <= data_in10;
													data_out10 <= dat_r;
												end else begin
													if ((data_in10 == 7'd64)) begin
														adr <= data_in10;
														data_out10 <= dat_r;
													end else begin
														if ((data_in10 == 7'd65)) begin
															adr <= data_in10;
															data_out10 <= dat_r;
														end else begin
															if ((data_in10 == 7'd66)) begin
																adr <= data_in10;
																data_out10 <= dat_r;
															end else begin
																if ((data_in10 == 7'd67)) begin
																	adr <= data_in10;
																	data_out10 <= dat_r;
																end else begin
																	if ((data_in10 == 7'd68)) begin
																		adr <= data_in10;
																		data_out10 <= dat_r;
																	end else begin
																		if ((data_in10 == 7'd69)) begin
																			adr <= data_in10;
																			data_out10 <= dat_r;
																		end else begin
																			if ((data_in10 == 7'd70)) begin
																				adr <= data_in10;
																				data_out10 <= dat_r;
																			end else begin
																				if ((data_in10 == 7'd71)) begin
																					adr <= data_in10;
																					data_out10 <= dat_r;
																				end else begin
																					if ((data_in10 == 7'd72)) begin
																						adr <= data_in10;
																						data_out10 <= dat_r;
																					end else begin
																						if ((data_in10 == 7'd73)) begin
																							adr <= data_in10;
																							data_out10 <= dat_r;
																						end else begin
																							if ((data_in10 == 7'd80)) begin
																								adr <= data_in10;
																								data_out10 <= dat_r;
																							end else begin
																								if ((data_in10 == 7'd81)) begin
																									adr <= data_in10;
																									data_out10 <= dat_r;
																								end else begin
																									data_out10 <= 1'd0;
																								end
																							end
																						end
																					end
																				end
																			end
																		end
																	end
																end
															end
														end
													end
												end
											end
										end
									end
								end
							end
						end
					end
				end
			end
		end
		if (valid_in) begin
			if ((data_in11 == 1'd0)) begin
				adr <= data_in11;
				data_out11 <= dat_r;
			end else begin
				if ((data_in11 == 6'd49)) begin
					adr <= data_in11;
					data_out11 <= dat_r;
				end else begin
					if ((data_in11 == 6'd50)) begin
						adr <= data_in11;
						data_out11 <= dat_r;
					end else begin
						if ((data_in11 == 6'd51)) begin
							adr <= data_in11;
							data_out11 <= dat_r;
						end else begin
							if ((data_in11 == 6'd52)) begin
								adr <= data_in11;
								data_out11 <= dat_r;
							end else begin
								if ((data_in11 == 6'd53)) begin
									adr <= data_in11;
									data_out11 <= dat_r;
								end else begin
									if ((data_in11 == 6'd54)) begin
										adr <= data_in11;
										data_out11 <= dat_r;
									end else begin
										if ((data_in11 == 6'd55)) begin
											adr <= data_in11;
											data_out11 <= dat_r;
										end else begin
											if ((data_in11 == 6'd56)) begin
												adr <= data_in11;
												data_out11 <= dat_r;
											end else begin
												if ((data_in11 == 6'd57)) begin
													adr <= data_in11;
													data_out11 <= dat_r;
												end else begin
													if ((data_in11 == 7'd64)) begin
														adr <= data_in11;
														data_out11 <= dat_r;
													end else begin
														if ((data_in11 == 7'd65)) begin
															adr <= data_in11;
															data_out11 <= dat_r;
														end else begin
															if ((data_in11 == 7'd66)) begin
																adr <= data_in11;
																data_out11 <= dat_r;
															end else begin
																if ((data_in11 == 7'd67)) begin
																	adr <= data_in11;
																	data_out11 <= dat_r;
																end else begin
																	if ((data_in11 == 7'd68)) begin
																		adr <= data_in11;
																		data_out11 <= dat_r;
																	end else begin
																		if ((data_in11 == 7'd69)) begin
																			adr <= data_in11;
																			data_out11 <= dat_r;
																		end else begin
																			if ((data_in11 == 7'd70)) begin
																				adr <= data_in11;
																				data_out11 <= dat_r;
																			end else begin
																				if ((data_in11 == 7'd71)) begin
																					adr <= data_in11;
																					data_out11 <= dat_r;
																				end else begin
																					if ((data_in11 == 7'd72)) begin
																						adr <= data_in11;
																						data_out11 <= dat_r;
																					end else begin
																						if ((data_in11 == 7'd73)) begin
																							adr <= data_in11;
																							data_out11 <= dat_r;
																						end else begin
																							if ((data_in11 == 7'd80)) begin
																								adr <= data_in11;
																								data_out11 <= dat_r;
																							end else begin
																								if ((data_in11 == 7'd81)) begin
																									adr <= data_in11;
																									data_out11 <= dat_r;
																								end else begin
																									data_out11 <= 1'd0;
																								end
																							end
																						end
																					end
																				end
																			end
																		end
																	end
																end
															end
														end
													end
												end
											end
										end
									end
								end
							end
						end
					end
				end
			end
		end
		if (valid_in) begin
			if ((data_in12 == 1'd0)) begin
				adr <= data_in12;
				data_out12 <= dat_r;
			end else begin
				if ((data_in12 == 6'd49)) begin
					adr <= data_in12;
					data_out12 <= dat_r;
				end else begin
					if ((data_in12 == 6'd50)) begin
						adr <= data_in12;
						data_out12 <= dat_r;
					end else begin
						if ((data_in12 == 6'd51)) begin
							adr <= data_in12;
							data_out12 <= dat_r;
						end else begin
							if ((data_in12 == 6'd52)) begin
								adr <= data_in12;
								data_out12 <= dat_r;
							end else begin
								if ((data_in12 == 6'd53)) begin
									adr <= data_in12;
									data_out12 <= dat_r;
								end else begin
									if ((data_in12 == 6'd54)) begin
										adr <= data_in12;
										data_out12 <= dat_r;
									end else begin
										if ((data_in12 == 6'd55)) begin
											adr <= data_in12;
											data_out12 <= dat_r;
										end else begin
											if ((data_in12 == 6'd56)) begin
												adr <= data_in12;
												data_out12 <= dat_r;
											end else begin
												if ((data_in12 == 6'd57)) begin
													adr <= data_in12;
													data_out12 <= dat_r;
												end else begin
													if ((data_in12 == 7'd64)) begin
														adr <= data_in12;
														data_out12 <= dat_r;
													end else begin
														if ((data_in12 == 7'd65)) begin
															adr <= data_in12;
															data_out12 <= dat_r;
														end else begin
															if ((data_in12 == 7'd66)) begin
																adr <= data_in12;
																data_out12 <= dat_r;
															end else begin
																if ((data_in12 == 7'd67)) begin
																	adr <= data_in12;
																	data_out12 <= dat_r;
																end else begin
																	if ((data_in12 == 7'd68)) begin
																		adr <= data_in12;
																		data_out12 <= dat_r;
																	end else begin
																		if ((data_in12 == 7'd69)) begin
																			adr <= data_in12;
																			data_out12 <= dat_r;
																		end else begin
																			if ((data_in12 == 7'd70)) begin
																				adr <= data_in12;
																				data_out12 <= dat_r;
																			end else begin
																				if ((data_in12 == 7'd71)) begin
																					adr <= data_in12;
																					data_out12 <= dat_r;
																				end else begin
																					if ((data_in12 == 7'd72)) begin
																						adr <= data_in12;
																						data_out12 <= dat_r;
																					end else begin
																						if ((data_in12 == 7'd73)) begin
																							adr <= data_in12;
																							data_out12 <= dat_r;
																						end else begin
																							if ((data_in12 == 7'd80)) begin
																								adr <= data_in12;
																								data_out12 <= dat_r;
																							end else begin
																								if ((data_in12 == 7'd81)) begin
																									adr <= data_in12;
																									data_out12 <= dat_r;
																								end else begin
																									data_out12 <= 1'd0;
																								end
																							end
																						end
																					end
																				end
																			end
																		end
																	end
																end
															end
														end
													end
												end
											end
										end
									end
								end
							end
						end
					end
				end
			end
		end
		if (valid_in) begin
			if ((data_in13 == 1'd0)) begin
				adr <= data_in13;
				data_out13 <= dat_r;
			end else begin
				if ((data_in13 == 6'd49)) begin
					adr <= data_in13;
					data_out13 <= dat_r;
				end else begin
					if ((data_in13 == 6'd50)) begin
						adr <= data_in13;
						data_out13 <= dat_r;
					end else begin
						if ((data_in13 == 6'd51)) begin
							adr <= data_in13;
							data_out13 <= dat_r;
						end else begin
							if ((data_in13 == 6'd52)) begin
								adr <= data_in13;
								data_out13 <= dat_r;
							end else begin
								if ((data_in13 == 6'd53)) begin
									adr <= data_in13;
									data_out13 <= dat_r;
								end else begin
									if ((data_in13 == 6'd54)) begin
										adr <= data_in13;
										data_out13 <= dat_r;
									end else begin
										if ((data_in13 == 6'd55)) begin
											adr <= data_in13;
											data_out13 <= dat_r;
										end else begin
											if ((data_in13 == 6'd56)) begin
												adr <= data_in13;
												data_out13 <= dat_r;
											end else begin
												if ((data_in13 == 6'd57)) begin
													adr <= data_in13;
													data_out13 <= dat_r;
												end else begin
													if ((data_in13 == 7'd64)) begin
														adr <= data_in13;
														data_out13 <= dat_r;
													end else begin
														if ((data_in13 == 7'd65)) begin
															adr <= data_in13;
															data_out13 <= dat_r;
														end else begin
															if ((data_in13 == 7'd66)) begin
																adr <= data_in13;
																data_out13 <= dat_r;
															end else begin
																if ((data_in13 == 7'd67)) begin
																	adr <= data_in13;
																	data_out13 <= dat_r;
																end else begin
																	if ((data_in13 == 7'd68)) begin
																		adr <= data_in13;
																		data_out13 <= dat_r;
																	end else begin
																		if ((data_in13 == 7'd69)) begin
																			adr <= data_in13;
																			data_out13 <= dat_r;
																		end else begin
																			if ((data_in13 == 7'd70)) begin
																				adr <= data_in13;
																				data_out13 <= dat_r;
																			end else begin
																				if ((data_in13 == 7'd71)) begin
																					adr <= data_in13;
																					data_out13 <= dat_r;
																				end else begin
																					if ((data_in13 == 7'd72)) begin
																						adr <= data_in13;
																						data_out13 <= dat_r;
																					end else begin
																						if ((data_in13 == 7'd73)) begin
																							adr <= data_in13;
																							data_out13 <= dat_r;
																						end else begin
																							if ((data_in13 == 7'd80)) begin
																								adr <= data_in13;
																								data_out13 <= dat_r;
																							end else begin
																								if ((data_in13 == 7'd81)) begin
																									adr <= data_in13;
																									data_out13 <= dat_r;
																								end else begin
																									data_out13 <= 1'd0;
																								end
																							end
																						end
																					end
																				end
																			end
																		end
																	end
																end
															end
														end
													end
												end
											end
										end
									end
								end
							end
						end
					end
				end
			end
		end
		if (valid_in) begin
			if ((data_in14 == 1'd0)) begin
				adr <= data_in14;
				data_out14 <= dat_r;
			end else begin
				if ((data_in14 == 6'd49)) begin
					adr <= data_in14;
					data_out14 <= dat_r;
				end else begin
					if ((data_in14 == 6'd50)) begin
						adr <= data_in14;
						data_out14 <= dat_r;
					end else begin
						if ((data_in14 == 6'd51)) begin
							adr <= data_in14;
							data_out14 <= dat_r;
						end else begin
							if ((data_in14 == 6'd52)) begin
								adr <= data_in14;
								data_out14 <= dat_r;
							end else begin
								if ((data_in14 == 6'd53)) begin
									adr <= data_in14;
									data_out14 <= dat_r;
								end else begin
									if ((data_in14 == 6'd54)) begin
										adr <= data_in14;
										data_out14 <= dat_r;
									end else begin
										if ((data_in14 == 6'd55)) begin
											adr <= data_in14;
											data_out14 <= dat_r;
										end else begin
											if ((data_in14 == 6'd56)) begin
												adr <= data_in14;
												data_out14 <= dat_r;
											end else begin
												if ((data_in14 == 6'd57)) begin
													adr <= data_in14;
													data_out14 <= dat_r;
												end else begin
													if ((data_in14 == 7'd64)) begin
														adr <= data_in14;
														data_out14 <= dat_r;
													end else begin
														if ((data_in14 == 7'd65)) begin
															adr <= data_in14;
															data_out14 <= dat_r;
														end else begin
															if ((data_in14 == 7'd66)) begin
																adr <= data_in14;
																data_out14 <= dat_r;
															end else begin
																if ((data_in14 == 7'd67)) begin
																	adr <= data_in14;
																	data_out14 <= dat_r;
																end else begin
																	if ((data_in14 == 7'd68)) begin
																		adr <= data_in14;
																		data_out14 <= dat_r;
																	end else begin
																		if ((data_in14 == 7'd69)) begin
																			adr <= data_in14;
																			data_out14 <= dat_r;
																		end else begin
																			if ((data_in14 == 7'd70)) begin
																				adr <= data_in14;
																				data_out14 <= dat_r;
																			end else begin
																				if ((data_in14 == 7'd71)) begin
																					adr <= data_in14;
																					data_out14 <= dat_r;
																				end else begin
																					if ((data_in14 == 7'd72)) begin
																						adr <= data_in14;
																						data_out14 <= dat_r;
																					end else begin
																						if ((data_in14 == 7'd73)) begin
																							adr <= data_in14;
																							data_out14 <= dat_r;
																						end else begin
																							if ((data_in14 == 7'd80)) begin
																								adr <= data_in14;
																								data_out14 <= dat_r;
																							end else begin
																								if ((data_in14 == 7'd81)) begin
																									adr <= data_in14;
																									data_out14 <= dat_r;
																								end else begin
																									data_out14 <= 1'd0;
																								end
																							end
																						end
																					end
																				end
																			end
																		end
																	end
																end
															end
														end
													end
												end
											end
										end
									end
								end
							end
						end
					end
				end
			end
		end
		if (valid_in) begin
			if ((data_in15 == 1'd0)) begin
				adr <= data_in15;
				data_out15 <= dat_r;
			end else begin
				if ((data_in15 == 6'd49)) begin
					adr <= data_in15;
					data_out15 <= dat_r;
				end else begin
					if ((data_in15 == 6'd50)) begin
						adr <= data_in15;
						data_out15 <= dat_r;
					end else begin
						if ((data_in15 == 6'd51)) begin
							adr <= data_in15;
							data_out15 <= dat_r;
						end else begin
							if ((data_in15 == 6'd52)) begin
								adr <= data_in15;
								data_out15 <= dat_r;
							end else begin
								if ((data_in15 == 6'd53)) begin
									adr <= data_in15;
									data_out15 <= dat_r;
								end else begin
									if ((data_in15 == 6'd54)) begin
										adr <= data_in15;
										data_out15 <= dat_r;
									end else begin
										if ((data_in15 == 6'd55)) begin
											adr <= data_in15;
											data_out15 <= dat_r;
										end else begin
											if ((data_in15 == 6'd56)) begin
												adr <= data_in15;
												data_out15 <= dat_r;
											end else begin
												if ((data_in15 == 6'd57)) begin
													adr <= data_in15;
													data_out15 <= dat_r;
												end else begin
													if ((data_in15 == 7'd64)) begin
														adr <= data_in15;
														data_out15 <= dat_r;
													end else begin
														if ((data_in15 == 7'd65)) begin
															adr <= data_in15;
															data_out15 <= dat_r;
														end else begin
															if ((data_in15 == 7'd66)) begin
																adr <= data_in15;
																data_out15 <= dat_r;
															end else begin
																if ((data_in15 == 7'd67)) begin
																	adr <= data_in15;
																	data_out15 <= dat_r;
																end else begin
																	if ((data_in15 == 7'd68)) begin
																		adr <= data_in15;
																		data_out15 <= dat_r;
																	end else begin
																		if ((data_in15 == 7'd69)) begin
																			adr <= data_in15;
																			data_out15 <= dat_r;
																		end else begin
																			if ((data_in15 == 7'd70)) begin
																				adr <= data_in15;
																				data_out15 <= dat_r;
																			end else begin
																				if ((data_in15 == 7'd71)) begin
																					adr <= data_in15;
																					data_out15 <= dat_r;
																				end else begin
																					if ((data_in15 == 7'd72)) begin
																						adr <= data_in15;
																						data_out15 <= dat_r;
																					end else begin
																						if ((data_in15 == 7'd73)) begin
																							adr <= data_in15;
																							data_out15 <= dat_r;
																						end else begin
																							if ((data_in15 == 7'd80)) begin
																								adr <= data_in15;
																								data_out15 <= dat_r;
																							end else begin
																								if ((data_in15 == 7'd81)) begin
																									adr <= data_in15;
																									data_out15 <= dat_r;
																								end else begin
																									data_out15 <= 1'd0;
																								end
																							end
																						end
																					end
																				end
																			end
																		end
																	end
																end
															end
														end
													end
												end
											end
										end
									end
								end
							end
						end
					end
				end
			end
		end
		if ((bytescount == 5'd16)) begin
			valid_out <= 1'd1;
		end
	end
end

reg [7:0] sboxmem[0:255];
reg [7:0] memdat;
always @(posedge sys_clk) begin
	memdat <= sboxmem[adr];
end

assign dat_r = memdat;

initial begin
	$readmemh("sboxmem.init", sboxmem);
end

endmodule
