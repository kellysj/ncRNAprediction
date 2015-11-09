
%%BATCHNAME%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
tFp_%BATCHNAME% = [];
tFn_%BATCHNAME% = [];
hFp_%BATCHNAME% = [];
hFn_%BATCHNAME% = [];

[trainFalsePos,trainFalseNeg,testFalsePos,testFalseNeg] = %FUNCTIONNAME%;tFp_%BATCHNAME% = [tFp_%BATCHNAME%, trainFalsePos];tFn_%BATCHNAME% = [tFn_%BATCHNAME%, trainFalseNeg];hFp_%BATCHNAME% = [hFp_%BATCHNAME%, testFalsePos];hFn_%BATCHNAME% = [hFn_%BATCHNAME%, testFalseNeg];

tErr_%BATCHNAME% = [tFp_%BATCHNAME%;tFn_%BATCHNAME%];
hErr_%BATCHNAME% = [hFp_%BATCHNAME%;hFn_%BATCHNAME%];

