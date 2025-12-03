`timescale 1ns/1ps

module alu (
    input  wire [7:0] a,
    input  wire [7:0] b,
    input  wire [2:0] op,
    output wire [7:0] y,
    output wire       carry
);

    reg [8:0] tmp;

    always @(*) begin
        case (op)
            3'b000: tmp = a + b;
            3'b001: tmp = a - b;
            3'b010: tmp = a & b;
            3'b011: tmp = a | b;
            3'b100: tmp = a ^ b;
            default: tmp = 9'd0;
        endcase
    end

    assign y     = tmp[7:0];
    assign carry = tmp[8];

endmodule
