function [errsTest,errsTrain] = cd_1_k4_10f_10fh1()
% Initial values
%tic;
M = 200;



[tX,tT,tH] = FEAT_cd_1_k4_10f_10fh1_4_all_train();
[hX,hT,hH] = FEAT_cd_1_k4_10f_10fh1_4_all_hold();

trainset = cell2mat(tX);%converting to matricies
train_t = cell2mat(tT);
testset = cell2mat(hX);
test_t = cell2mat(hT);

N = length(train_t);
Nt = length(test_t);

[trainset, mu, sig] = zscore(trainset);
testset = (testset - repmat(mu, Nt, 1)) ./ repmat(sig, Nt, 1) ;

% Estimate
%profile on -history -timer 'real'
model = cRumTrainKMeansMAP(trainset, train_t, M, true, 2, 10, 1000000, 1e-03);
%profile viewer
%toc;

y = cRumClassify(model, trainset);
errsTrain = sum(y(train_t == 0) > 0.5) + sum(y(train_t == 1) <= 0.5);
fprintf('M: %d\n', M);
fprintf('CRUM CLASSIFICATION train error: %.2f%%\n', errsTrain / N *100);

% Test
y = cRumClassify(model, testset);
errsTest = sum(y(test_t == 0) > 0.5) + sum(y(test_t == 1) <= 0.5);
fprintf('CRUM CLASSIFICATION test error: %.2f%%\n', errsTest / Nt *100);

end