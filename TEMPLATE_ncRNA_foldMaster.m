%ERRNAME% = [];

%FUNCTIONBATCH%

fprintf('Train Error: %.2f%%\n', mean(%ERRNAME%(:,2)));
fprintf('Test Error: %.2f%%\n', mean(%ERRNAME%(:,1)));