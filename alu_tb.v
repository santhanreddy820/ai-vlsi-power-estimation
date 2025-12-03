`timescale 1ns/1ps
module alu_tb;

    // clock
    reg         clk;
    // stimulus
    reg  [7:0]  a, b;
    reg  [2:0]  op;
    // DUT outputs
    wire [7:0]  y;
    wire        carry;

    // logging helpers
    integer f, i;
    integer toggles_this_cycle;
    reg [7:0] y_prev;

    // instantiate DUT
    alu uut (
        .a(a),
        .b(b),
        .op(op),
        .y(y),
        .carry(carry)
    );

    // 100 MHz clock: period = 10 ns
    initial begin
        clk = 0;
        forever #5 clk = ~clk;   // toggle every 5 ns
    end

    // function: count how many bits changed in y since last cycle
    function integer count_toggles;
        input [7:0] old_y;
        input [7:0] new_y;
        integer k;
        begin
            count_toggles = 0;
            for (k = 0; k < 8; k = k + 1)
                if (old_y[k] !== new_y[k])
                    count_toggles = count_toggles + 1;
        end
    endfunction

    // function: Hamming weight (number of 1s) of an 8-bit value
    function integer popcount8;
        input [7:0] v;
        integer k;
        begin
            popcount8 = 0;
            for (k = 0; k < 8; k = k + 1)
                if (v[k] === 1'b1)
                    popcount8 = popcount8 + 1;
        end
    endfunction

    // log once every rising edge of clk
    always @(posedge clk) begin
        // how many bits of y toggled since last cycle?
        toggles_this_cycle = count_toggles(y_prev, y);
        y_prev             = y;

        // CSV row:
        // time, op, a, b, y, toggles, hw_a, hw_b
        $fwrite(f, "%0t,%0d,%0d,%0d,%0d,%0d,%0d,%0d\n",
                $time, op, a, b, y,
                toggles_this_cycle,
                popcount8(a),
                popcount8(b));
    end

    initial begin
        // open CSV file
        f = $fopen("activity.csv", "w");
        if (!f) begin
            $display("ERROR: Could not open activity.csv");
            $finish;
        end

        // header row
        $fwrite(f, "time,op,a,b,y,toggles,hw_a,hw_b\n");

        // initial values
        a = 0;
        b = 0;
        op = 0;
        y_prev = 0;
        toggles_this_cycle = 0;

        // apply new random pattern every cycle
        for (i = 0; i < 500; i = i + 1) begin
            @(posedge clk);        // wait for rising edge
            a  = $random;
            b  = $random;
            op = i % 5;            // cycle through first 5 ops
        end

        // let a few extra cycles pass
        repeat (4) @(posedge clk);

        $fclose(f);
        $display("Advanced simulation finished. activity.csv generated.");
        $finish;
    end

endmodule

