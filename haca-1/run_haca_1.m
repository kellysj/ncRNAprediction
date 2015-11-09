
%w1_haca_1%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
tFp_w1_haca_1 = [];
tFn_w1_haca_1 = [];
hFp_w1_haca_1 = [];
hFn_w1_haca_1 = [];

[trainFalsePos,trainFalseNeg,testFalsePos,testFalseNeg] = fold_0_window_1_haca_1;
tFp_w1_haca_1 = [tFp_w1_haca_1, trainFalsePos];
tFn_w1_haca_1 = [tFn_w1_haca_1, trainFalseNeg];
hFp_w1_haca_1 = [hFp_w1_haca_1, testFalsePos];
hFn_w1_haca_1 = [hFn_w1_haca_1, testFalseNeg];

[trainFalsePos,trainFalseNeg,testFalsePos,testFalseNeg] = fold_1_window_1_haca_1;
tFp_w1_haca_1 = [tFp_w1_haca_1, trainFalsePos];
tFn_w1_haca_1 = [tFn_w1_haca_1, trainFalseNeg];
hFp_w1_haca_1 = [hFp_w1_haca_1, testFalsePos];
hFn_w1_haca_1 = [hFn_w1_haca_1, testFalseNeg];

[trainFalsePos,trainFalseNeg,testFalsePos,testFalseNeg] = fold_2_window_1_haca_1;
tFp_w1_haca_1 = [tFp_w1_haca_1, trainFalsePos];
tFn_w1_haca_1 = [tFn_w1_haca_1, trainFalseNeg];
hFp_w1_haca_1 = [hFp_w1_haca_1, testFalsePos];
hFn_w1_haca_1 = [hFn_w1_haca_1, testFalseNeg];

[trainFalsePos,trainFalseNeg,testFalsePos,testFalseNeg] = fold_3_window_1_haca_1;
tFp_w1_haca_1 = [tFp_w1_haca_1, trainFalsePos];
tFn_w1_haca_1 = [tFn_w1_haca_1, trainFalseNeg];
hFp_w1_haca_1 = [hFp_w1_haca_1, testFalsePos];
hFn_w1_haca_1 = [hFn_w1_haca_1, testFalseNeg];

[trainFalsePos,trainFalseNeg,testFalsePos,testFalseNeg] = fold_4_window_1_haca_1;
tFp_w1_haca_1 = [tFp_w1_haca_1, trainFalsePos];
tFn_w1_haca_1 = [tFn_w1_haca_1, trainFalseNeg];
hFp_w1_haca_1 = [hFp_w1_haca_1, testFalsePos];
hFn_w1_haca_1 = [hFn_w1_haca_1, testFalseNeg];

[trainFalsePos,trainFalseNeg,testFalsePos,testFalseNeg] = fold_5_window_1_haca_1;
tFp_w1_haca_1 = [tFp_w1_haca_1, trainFalsePos];
tFn_w1_haca_1 = [tFn_w1_haca_1, trainFalseNeg];
hFp_w1_haca_1 = [hFp_w1_haca_1, testFalsePos];
hFn_w1_haca_1 = [hFn_w1_haca_1, testFalseNeg];

[trainFalsePos,trainFalseNeg,testFalsePos,testFalseNeg] = fold_6_window_1_haca_1;
tFp_w1_haca_1 = [tFp_w1_haca_1, trainFalsePos];
tFn_w1_haca_1 = [tFn_w1_haca_1, trainFalseNeg];
hFp_w1_haca_1 = [hFp_w1_haca_1, testFalsePos];
hFn_w1_haca_1 = [hFn_w1_haca_1, testFalseNeg];

[trainFalsePos,trainFalseNeg,testFalsePos,testFalseNeg] = fold_7_window_1_haca_1;
tFp_w1_haca_1 = [tFp_w1_haca_1, trainFalsePos];
tFn_w1_haca_1 = [tFn_w1_haca_1, trainFalseNeg];
hFp_w1_haca_1 = [hFp_w1_haca_1, testFalsePos];
hFn_w1_haca_1 = [hFn_w1_haca_1, testFalseNeg];

[trainFalsePos,trainFalseNeg,testFalsePos,testFalseNeg] = fold_8_window_1_haca_1;
tFp_w1_haca_1 = [tFp_w1_haca_1, trainFalsePos];
tFn_w1_haca_1 = [tFn_w1_haca_1, trainFalseNeg];
hFp_w1_haca_1 = [hFp_w1_haca_1, testFalsePos];
hFn_w1_haca_1 = [hFn_w1_haca_1, testFalseNeg];

[trainFalsePos,trainFalseNeg,testFalsePos,testFalseNeg] = fold_9_window_1_haca_1;
tFp_w1_haca_1 = [tFp_w1_haca_1, trainFalsePos];
tFn_w1_haca_1 = [tFn_w1_haca_1, trainFalseNeg];
hFp_w1_haca_1 = [hFp_w1_haca_1, testFalsePos];
hFn_w1_haca_1 = [hFn_w1_haca_1, testFalseNeg];


tErr_w1_haca_1 = [tFp_w1_haca_1;tFn_w1_haca_1];
hErr_w1_haca_1 = [hFp_w1_haca_1;hFn_w1_haca_1];


%w2_haca_1%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
tFp_w2_haca_1 = [];
tFn_w2_haca_1 = [];
hFp_w2_haca_1 = [];
hFn_w2_haca_1 = [];

[trainFalsePos,trainFalseNeg,testFalsePos,testFalseNeg] = fold_0_window_2_haca_1;
tFp_w2_haca_1 = [tFp_w2_haca_1, trainFalsePos];
tFn_w2_haca_1 = [tFn_w2_haca_1, trainFalseNeg];
hFp_w2_haca_1 = [hFp_w2_haca_1, testFalsePos];
hFn_w2_haca_1 = [hFn_w2_haca_1, testFalseNeg];

[trainFalsePos,trainFalseNeg,testFalsePos,testFalseNeg] = fold_1_window_2_haca_1;
tFp_w2_haca_1 = [tFp_w2_haca_1, trainFalsePos];
tFn_w2_haca_1 = [tFn_w2_haca_1, trainFalseNeg];
hFp_w2_haca_1 = [hFp_w2_haca_1, testFalsePos];
hFn_w2_haca_1 = [hFn_w2_haca_1, testFalseNeg];

[trainFalsePos,trainFalseNeg,testFalsePos,testFalseNeg] = fold_2_window_2_haca_1;
tFp_w2_haca_1 = [tFp_w2_haca_1, trainFalsePos];
tFn_w2_haca_1 = [tFn_w2_haca_1, trainFalseNeg];
hFp_w2_haca_1 = [hFp_w2_haca_1, testFalsePos];
hFn_w2_haca_1 = [hFn_w2_haca_1, testFalseNeg];

[trainFalsePos,trainFalseNeg,testFalsePos,testFalseNeg] = fold_3_window_2_haca_1;
tFp_w2_haca_1 = [tFp_w2_haca_1, trainFalsePos];
tFn_w2_haca_1 = [tFn_w2_haca_1, trainFalseNeg];
hFp_w2_haca_1 = [hFp_w2_haca_1, testFalsePos];
hFn_w2_haca_1 = [hFn_w2_haca_1, testFalseNeg];

[trainFalsePos,trainFalseNeg,testFalsePos,testFalseNeg] = fold_4_window_2_haca_1;
tFp_w2_haca_1 = [tFp_w2_haca_1, trainFalsePos];
tFn_w2_haca_1 = [tFn_w2_haca_1, trainFalseNeg];
hFp_w2_haca_1 = [hFp_w2_haca_1, testFalsePos];
hFn_w2_haca_1 = [hFn_w2_haca_1, testFalseNeg];

[trainFalsePos,trainFalseNeg,testFalsePos,testFalseNeg] = fold_5_window_2_haca_1;
tFp_w2_haca_1 = [tFp_w2_haca_1, trainFalsePos];
tFn_w2_haca_1 = [tFn_w2_haca_1, trainFalseNeg];
hFp_w2_haca_1 = [hFp_w2_haca_1, testFalsePos];
hFn_w2_haca_1 = [hFn_w2_haca_1, testFalseNeg];

[trainFalsePos,trainFalseNeg,testFalsePos,testFalseNeg] = fold_6_window_2_haca_1;
tFp_w2_haca_1 = [tFp_w2_haca_1, trainFalsePos];
tFn_w2_haca_1 = [tFn_w2_haca_1, trainFalseNeg];
hFp_w2_haca_1 = [hFp_w2_haca_1, testFalsePos];
hFn_w2_haca_1 = [hFn_w2_haca_1, testFalseNeg];

[trainFalsePos,trainFalseNeg,testFalsePos,testFalseNeg] = fold_7_window_2_haca_1;
tFp_w2_haca_1 = [tFp_w2_haca_1, trainFalsePos];
tFn_w2_haca_1 = [tFn_w2_haca_1, trainFalseNeg];
hFp_w2_haca_1 = [hFp_w2_haca_1, testFalsePos];
hFn_w2_haca_1 = [hFn_w2_haca_1, testFalseNeg];

[trainFalsePos,trainFalseNeg,testFalsePos,testFalseNeg] = fold_8_window_2_haca_1;
tFp_w2_haca_1 = [tFp_w2_haca_1, trainFalsePos];
tFn_w2_haca_1 = [tFn_w2_haca_1, trainFalseNeg];
hFp_w2_haca_1 = [hFp_w2_haca_1, testFalsePos];
hFn_w2_haca_1 = [hFn_w2_haca_1, testFalseNeg];

[trainFalsePos,trainFalseNeg,testFalsePos,testFalseNeg] = fold_9_window_2_haca_1;
tFp_w2_haca_1 = [tFp_w2_haca_1, trainFalsePos];
tFn_w2_haca_1 = [tFn_w2_haca_1, trainFalseNeg];
hFp_w2_haca_1 = [hFp_w2_haca_1, testFalsePos];
hFn_w2_haca_1 = [hFn_w2_haca_1, testFalseNeg];


tErr_w2_haca_1 = [tFp_w2_haca_1;tFn_w2_haca_1];
hErr_w2_haca_1 = [hFp_w2_haca_1;hFn_w2_haca_1];


%w3_haca_1%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
tFp_w3_haca_1 = [];
tFn_w3_haca_1 = [];
hFp_w3_haca_1 = [];
hFn_w3_haca_1 = [];

[trainFalsePos,trainFalseNeg,testFalsePos,testFalseNeg] = fold_0_window_3_haca_1;
tFp_w3_haca_1 = [tFp_w3_haca_1, trainFalsePos];
tFn_w3_haca_1 = [tFn_w3_haca_1, trainFalseNeg];
hFp_w3_haca_1 = [hFp_w3_haca_1, testFalsePos];
hFn_w3_haca_1 = [hFn_w3_haca_1, testFalseNeg];

[trainFalsePos,trainFalseNeg,testFalsePos,testFalseNeg] = fold_1_window_3_haca_1;
tFp_w3_haca_1 = [tFp_w3_haca_1, trainFalsePos];
tFn_w3_haca_1 = [tFn_w3_haca_1, trainFalseNeg];
hFp_w3_haca_1 = [hFp_w3_haca_1, testFalsePos];
hFn_w3_haca_1 = [hFn_w3_haca_1, testFalseNeg];

[trainFalsePos,trainFalseNeg,testFalsePos,testFalseNeg] = fold_2_window_3_haca_1;
tFp_w3_haca_1 = [tFp_w3_haca_1, trainFalsePos];
tFn_w3_haca_1 = [tFn_w3_haca_1, trainFalseNeg];
hFp_w3_haca_1 = [hFp_w3_haca_1, testFalsePos];
hFn_w3_haca_1 = [hFn_w3_haca_1, testFalseNeg];

[trainFalsePos,trainFalseNeg,testFalsePos,testFalseNeg] = fold_3_window_3_haca_1;
tFp_w3_haca_1 = [tFp_w3_haca_1, trainFalsePos];
tFn_w3_haca_1 = [tFn_w3_haca_1, trainFalseNeg];
hFp_w3_haca_1 = [hFp_w3_haca_1, testFalsePos];
hFn_w3_haca_1 = [hFn_w3_haca_1, testFalseNeg];

[trainFalsePos,trainFalseNeg,testFalsePos,testFalseNeg] = fold_4_window_3_haca_1;
tFp_w3_haca_1 = [tFp_w3_haca_1, trainFalsePos];
tFn_w3_haca_1 = [tFn_w3_haca_1, trainFalseNeg];
hFp_w3_haca_1 = [hFp_w3_haca_1, testFalsePos];
hFn_w3_haca_1 = [hFn_w3_haca_1, testFalseNeg];

[trainFalsePos,trainFalseNeg,testFalsePos,testFalseNeg] = fold_5_window_3_haca_1;
tFp_w3_haca_1 = [tFp_w3_haca_1, trainFalsePos];
tFn_w3_haca_1 = [tFn_w3_haca_1, trainFalseNeg];
hFp_w3_haca_1 = [hFp_w3_haca_1, testFalsePos];
hFn_w3_haca_1 = [hFn_w3_haca_1, testFalseNeg];

[trainFalsePos,trainFalseNeg,testFalsePos,testFalseNeg] = fold_6_window_3_haca_1;
tFp_w3_haca_1 = [tFp_w3_haca_1, trainFalsePos];
tFn_w3_haca_1 = [tFn_w3_haca_1, trainFalseNeg];
hFp_w3_haca_1 = [hFp_w3_haca_1, testFalsePos];
hFn_w3_haca_1 = [hFn_w3_haca_1, testFalseNeg];

[trainFalsePos,trainFalseNeg,testFalsePos,testFalseNeg] = fold_7_window_3_haca_1;
tFp_w3_haca_1 = [tFp_w3_haca_1, trainFalsePos];
tFn_w3_haca_1 = [tFn_w3_haca_1, trainFalseNeg];
hFp_w3_haca_1 = [hFp_w3_haca_1, testFalsePos];
hFn_w3_haca_1 = [hFn_w3_haca_1, testFalseNeg];

[trainFalsePos,trainFalseNeg,testFalsePos,testFalseNeg] = fold_8_window_3_haca_1;
tFp_w3_haca_1 = [tFp_w3_haca_1, trainFalsePos];
tFn_w3_haca_1 = [tFn_w3_haca_1, trainFalseNeg];
hFp_w3_haca_1 = [hFp_w3_haca_1, testFalsePos];
hFn_w3_haca_1 = [hFn_w3_haca_1, testFalseNeg];

[trainFalsePos,trainFalseNeg,testFalsePos,testFalseNeg] = fold_9_window_3_haca_1;
tFp_w3_haca_1 = [tFp_w3_haca_1, trainFalsePos];
tFn_w3_haca_1 = [tFn_w3_haca_1, trainFalseNeg];
hFp_w3_haca_1 = [hFp_w3_haca_1, testFalsePos];
hFn_w3_haca_1 = [hFn_w3_haca_1, testFalseNeg];


tErr_w3_haca_1 = [tFp_w3_haca_1;tFn_w3_haca_1];
hErr_w3_haca_1 = [hFp_w3_haca_1;hFn_w3_haca_1];


%w4_haca_1%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
tFp_w4_haca_1 = [];
tFn_w4_haca_1 = [];
hFp_w4_haca_1 = [];
hFn_w4_haca_1 = [];

[trainFalsePos,trainFalseNeg,testFalsePos,testFalseNeg] = fold_0_window_4_haca_1;
tFp_w4_haca_1 = [tFp_w4_haca_1, trainFalsePos];
tFn_w4_haca_1 = [tFn_w4_haca_1, trainFalseNeg];
hFp_w4_haca_1 = [hFp_w4_haca_1, testFalsePos];
hFn_w4_haca_1 = [hFn_w4_haca_1, testFalseNeg];

[trainFalsePos,trainFalseNeg,testFalsePos,testFalseNeg] = fold_1_window_4_haca_1;
tFp_w4_haca_1 = [tFp_w4_haca_1, trainFalsePos];
tFn_w4_haca_1 = [tFn_w4_haca_1, trainFalseNeg];
hFp_w4_haca_1 = [hFp_w4_haca_1, testFalsePos];
hFn_w4_haca_1 = [hFn_w4_haca_1, testFalseNeg];

[trainFalsePos,trainFalseNeg,testFalsePos,testFalseNeg] = fold_2_window_4_haca_1;
tFp_w4_haca_1 = [tFp_w4_haca_1, trainFalsePos];
tFn_w4_haca_1 = [tFn_w4_haca_1, trainFalseNeg];
hFp_w4_haca_1 = [hFp_w4_haca_1, testFalsePos];
hFn_w4_haca_1 = [hFn_w4_haca_1, testFalseNeg];

[trainFalsePos,trainFalseNeg,testFalsePos,testFalseNeg] = fold_3_window_4_haca_1;
tFp_w4_haca_1 = [tFp_w4_haca_1, trainFalsePos];
tFn_w4_haca_1 = [tFn_w4_haca_1, trainFalseNeg];
hFp_w4_haca_1 = [hFp_w4_haca_1, testFalsePos];
hFn_w4_haca_1 = [hFn_w4_haca_1, testFalseNeg];

[trainFalsePos,trainFalseNeg,testFalsePos,testFalseNeg] = fold_4_window_4_haca_1;
tFp_w4_haca_1 = [tFp_w4_haca_1, trainFalsePos];
tFn_w4_haca_1 = [tFn_w4_haca_1, trainFalseNeg];
hFp_w4_haca_1 = [hFp_w4_haca_1, testFalsePos];
hFn_w4_haca_1 = [hFn_w4_haca_1, testFalseNeg];

[trainFalsePos,trainFalseNeg,testFalsePos,testFalseNeg] = fold_5_window_4_haca_1;
tFp_w4_haca_1 = [tFp_w4_haca_1, trainFalsePos];
tFn_w4_haca_1 = [tFn_w4_haca_1, trainFalseNeg];
hFp_w4_haca_1 = [hFp_w4_haca_1, testFalsePos];
hFn_w4_haca_1 = [hFn_w4_haca_1, testFalseNeg];

[trainFalsePos,trainFalseNeg,testFalsePos,testFalseNeg] = fold_6_window_4_haca_1;
tFp_w4_haca_1 = [tFp_w4_haca_1, trainFalsePos];
tFn_w4_haca_1 = [tFn_w4_haca_1, trainFalseNeg];
hFp_w4_haca_1 = [hFp_w4_haca_1, testFalsePos];
hFn_w4_haca_1 = [hFn_w4_haca_1, testFalseNeg];

[trainFalsePos,trainFalseNeg,testFalsePos,testFalseNeg] = fold_7_window_4_haca_1;
tFp_w4_haca_1 = [tFp_w4_haca_1, trainFalsePos];
tFn_w4_haca_1 = [tFn_w4_haca_1, trainFalseNeg];
hFp_w4_haca_1 = [hFp_w4_haca_1, testFalsePos];
hFn_w4_haca_1 = [hFn_w4_haca_1, testFalseNeg];

[trainFalsePos,trainFalseNeg,testFalsePos,testFalseNeg] = fold_8_window_4_haca_1;
tFp_w4_haca_1 = [tFp_w4_haca_1, trainFalsePos];
tFn_w4_haca_1 = [tFn_w4_haca_1, trainFalseNeg];
hFp_w4_haca_1 = [hFp_w4_haca_1, testFalsePos];
hFn_w4_haca_1 = [hFn_w4_haca_1, testFalseNeg];

[trainFalsePos,trainFalseNeg,testFalsePos,testFalseNeg] = fold_9_window_4_haca_1;
tFp_w4_haca_1 = [tFp_w4_haca_1, trainFalsePos];
tFn_w4_haca_1 = [tFn_w4_haca_1, trainFalseNeg];
hFp_w4_haca_1 = [hFp_w4_haca_1, testFalsePos];
hFn_w4_haca_1 = [hFn_w4_haca_1, testFalseNeg];


tErr_w4_haca_1 = [tFp_w4_haca_1;tFn_w4_haca_1];
hErr_w4_haca_1 = [hFp_w4_haca_1;hFn_w4_haca_1];

