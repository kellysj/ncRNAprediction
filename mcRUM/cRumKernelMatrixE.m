% Assuming Gaussian RBF kernel with parameter theta
% TODO: add kernel options
% X - training, each observation a row
% U - matrix of M units, column by column
% theta - parameter for RBF kernel
% useBias - true/false to add extra column of ones
function K = cRumKernelMatrixE(X, U, theta, useBias, kernelType)
    default('useBias', false);
    default('kernelType', 1);
    
    M = size(U, 2);
    N = size(X, 1);
    
    if useBias
        K = ones(N, M + 1);
    else
        K = ones(N, M);
    end

    for m = 1:M
        K(:, m) = cRumRbfRowE(X, U(:, m), theta, kernelType);
    end
end