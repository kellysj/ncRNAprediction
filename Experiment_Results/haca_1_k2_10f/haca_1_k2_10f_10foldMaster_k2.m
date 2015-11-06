totalErr_haca_1_k2_10f = [];

[errTest_haca_1_k2_10f_10fh0,errTrain_haca_1_k2_10f_10fh0] = haca_1_k2_10f_10fh0();
totalErr_haca_1_k2_10f= [totalErr_haca_1_k2_10f;[errTest_haca_1_k2_10f_10fh0,errTrain_haca_1_k2_10f_10fh0]];
[errTest_haca_1_k2_10f_10fh1,errTrain_haca_1_k2_10f_10fh1] = haca_1_k2_10f_10fh1();
totalErr_haca_1_k2_10f= [totalErr_haca_1_k2_10f;[errTest_haca_1_k2_10f_10fh1,errTrain_haca_1_k2_10f_10fh1]];
[errTest_haca_1_k2_10f_10fh2,errTrain_haca_1_k2_10f_10fh2] = haca_1_k2_10f_10fh2();
totalErr_haca_1_k2_10f= [totalErr_haca_1_k2_10f;[errTest_haca_1_k2_10f_10fh2,errTrain_haca_1_k2_10f_10fh2]];
[errTest_haca_1_k2_10f_10fh3,errTrain_haca_1_k2_10f_10fh3] = haca_1_k2_10f_10fh3();
totalErr_haca_1_k2_10f= [totalErr_haca_1_k2_10f;[errTest_haca_1_k2_10f_10fh3,errTrain_haca_1_k2_10f_10fh3]];
[errTest_haca_1_k2_10f_10fh4,errTrain_haca_1_k2_10f_10fh4] = haca_1_k2_10f_10fh4();
totalErr_haca_1_k2_10f= [totalErr_haca_1_k2_10f;[errTest_haca_1_k2_10f_10fh4,errTrain_haca_1_k2_10f_10fh4]];
[errTest_haca_1_k2_10f_10fh5,errTrain_haca_1_k2_10f_10fh5] = haca_1_k2_10f_10fh5();
totalErr_haca_1_k2_10f= [totalErr_haca_1_k2_10f;[errTest_haca_1_k2_10f_10fh5,errTrain_haca_1_k2_10f_10fh5]];
[errTest_haca_1_k2_10f_10fh6,errTrain_haca_1_k2_10f_10fh6] = haca_1_k2_10f_10fh6();
totalErr_haca_1_k2_10f= [totalErr_haca_1_k2_10f;[errTest_haca_1_k2_10f_10fh6,errTrain_haca_1_k2_10f_10fh6]];
[errTest_haca_1_k2_10f_10fh7,errTrain_haca_1_k2_10f_10fh7] = haca_1_k2_10f_10fh7();
totalErr_haca_1_k2_10f= [totalErr_haca_1_k2_10f;[errTest_haca_1_k2_10f_10fh7,errTrain_haca_1_k2_10f_10fh7]];
[errTest_haca_1_k2_10f_10fh8,errTrain_haca_1_k2_10f_10fh8] = haca_1_k2_10f_10fh8();
totalErr_haca_1_k2_10f= [totalErr_haca_1_k2_10f;[errTest_haca_1_k2_10f_10fh8,errTrain_haca_1_k2_10f_10fh8]];
[errTest_haca_1_k2_10f_10fh9,errTrain_haca_1_k2_10f_10fh9] = haca_1_k2_10f_10fh9();
totalErr_haca_1_k2_10f= [totalErr_haca_1_k2_10f;[errTest_haca_1_k2_10f_10fh9,errTrain_haca_1_k2_10f_10fh9]];


fprintf('Train Error: %.2f%%\n', mean(totalErr_haca_1_k2_10f(:,2)));
fprintf('Test Error: %.2f%%\n', mean(totalErr_haca_1_k2_10f(:,1)));