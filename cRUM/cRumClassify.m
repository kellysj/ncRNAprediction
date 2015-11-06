% Assuming Gaussian RBF kernel with parameter theta
% model - cRUM model
% X - data to classify, each observation a row
function [p, y] = cRumClassify(model, X, kernelType)
    default('kernelType', 2);
    K = cRumKernelMatrix(X, model.U, model.theta, false, kernelType);
    y = K * model.w + model.b;
    p = cRumSigmoid(y);
end