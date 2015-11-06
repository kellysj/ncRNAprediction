totalErr_cd_1_k3_10f = [];

[errTest_cd_1_k3_10f_10fh0,errTrain_cd_1_k3_10f_10fh0] = cd_1_k3_10f_10fh0();
totalErr_cd_1_k3_10f= [totalErr_cd_1_k3_10f;[errTest_cd_1_k3_10f_10fh0,errTrain_cd_1_k3_10f_10fh0]];
[errTest_cd_1_k3_10f_10fh1,errTrain_cd_1_k3_10f_10fh1] = cd_1_k3_10f_10fh1();
totalErr_cd_1_k3_10f= [totalErr_cd_1_k3_10f;[errTest_cd_1_k3_10f_10fh1,errTrain_cd_1_k3_10f_10fh1]];
[errTest_cd_1_k3_10f_10fh2,errTrain_cd_1_k3_10f_10fh2] = cd_1_k3_10f_10fh2();
totalErr_cd_1_k3_10f= [totalErr_cd_1_k3_10f;[errTest_cd_1_k3_10f_10fh2,errTrain_cd_1_k3_10f_10fh2]];
[errTest_cd_1_k3_10f_10fh3,errTrain_cd_1_k3_10f_10fh3] = cd_1_k3_10f_10fh3();
totalErr_cd_1_k3_10f= [totalErr_cd_1_k3_10f;[errTest_cd_1_k3_10f_10fh3,errTrain_cd_1_k3_10f_10fh3]];
[errTest_cd_1_k3_10f_10fh4,errTrain_cd_1_k3_10f_10fh4] = cd_1_k3_10f_10fh4();
totalErr_cd_1_k3_10f= [totalErr_cd_1_k3_10f;[errTest_cd_1_k3_10f_10fh4,errTrain_cd_1_k3_10f_10fh4]];
[errTest_cd_1_k3_10f_10fh5,errTrain_cd_1_k3_10f_10fh5] = cd_1_k3_10f_10fh5();
totalErr_cd_1_k3_10f= [totalErr_cd_1_k3_10f;[errTest_cd_1_k3_10f_10fh5,errTrain_cd_1_k3_10f_10fh5]];
[errTest_cd_1_k3_10f_10fh6,errTrain_cd_1_k3_10f_10fh6] = cd_1_k3_10f_10fh6();
totalErr_cd_1_k3_10f= [totalErr_cd_1_k3_10f;[errTest_cd_1_k3_10f_10fh6,errTrain_cd_1_k3_10f_10fh6]];
[errTest_cd_1_k3_10f_10fh7,errTrain_cd_1_k3_10f_10fh7] = cd_1_k3_10f_10fh7();
totalErr_cd_1_k3_10f= [totalErr_cd_1_k3_10f;[errTest_cd_1_k3_10f_10fh7,errTrain_cd_1_k3_10f_10fh7]];
[errTest_cd_1_k3_10f_10fh8,errTrain_cd_1_k3_10f_10fh8] = cd_1_k3_10f_10fh8();
totalErr_cd_1_k3_10f= [totalErr_cd_1_k3_10f;[errTest_cd_1_k3_10f_10fh8,errTrain_cd_1_k3_10f_10fh8]];
[errTest_cd_1_k3_10f_10fh9,errTrain_cd_1_k3_10f_10fh9] = cd_1_k3_10f_10fh9();
totalErr_cd_1_k3_10f= [totalErr_cd_1_k3_10f;[errTest_cd_1_k3_10f_10fh9,errTrain_cd_1_k3_10f_10fh9]];


fprintf('Train Error: %.2f%%\n', mean(totalErr_cd_1_k3_10f(:,2)));
fprintf('Test Error: %.2f%%\n', mean(totalErr_cd_1_k3_10f(:,1)));