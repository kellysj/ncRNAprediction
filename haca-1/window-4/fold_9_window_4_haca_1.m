function [errsTrainFalsePos,errsTrainFalseNeg,errsTestFalsePos,errsTestFalseNeg] = fold_9_window_4_haca_1()
% Initial values
%tic;
M = 200;



[tX,tT,tH] = FEAT_fold_9_window_4_haca_1_train();
[hX,hT,hH] = FEAT_fold_9_window_4_haca_1_hold();

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
%save fold_9_window_4_haca_1_model model

y = cRumClassify(model, trainset);
errsTrainFalsePos = sum(y(train_t == 0) > 0.5); 
errsTrainFalseNeg = sum(y(train_t == 1) <= 0.5);
fprintf('M: %d\n', M);
fprintf('CRUM CLASSIFICATION train error: %.2f%%\n', errsTrainFalsePos / N *100);
fprintf('CRUM CLASSIFICATION train error: %.2f%%\n', errsTrainFalseNeg / N *100);
% Test
y = cRumClassify(model, testset);
errsTestFalsePos = sum(y(test_t == 0) > 0.5);
errsTestFalseNeg = sum(y(test_t == 1) <= 0.5);
fprintf('CRUM CLASSIFICATION test error: %.2f%%\n', errsTestFalsePos / Nt *100);
fprintf('CRUM CLASSIFICATION test error: %.2f%%\n', errsTestFalseNeg / Nt *100);

end