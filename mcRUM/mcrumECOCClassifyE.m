% assuming b is row vector
function [p y] = mcrumECOCClassifyE(model, X, kernelType)
    default('kernelType', 1);
    
    n = size(X, 1);
    nc = model.Nc;
    np = size(model.C, 2);
    p = zeros(n, nc);
    K = cRumKernelMatrixE(X, model.U, model.theta, false, kernelType);
    
    % softmax needs activation values for all classes per datapoint
    for i = 1:n
        y = K(i, :) * model.W + model.b;
        p1 = cRumSigmoidE(y);
        p2 = zeros(1, nc);
        
        for j = 1:np
            pos_class = find(model.C(:, j) == 1);
            neg_class = find(model.C(:, j) == -1);
            
            for k = 1:size(pos_class, 2)
                p2(1, pos_class(k)) = p2(1, pos_class(k)) + log(p1(j));
            end
            
            for k = 1:size(neg_class, 2)
                p2(1, neg_class(k)) = p2(1, neg_class(k)) + log(1 - p1(j));
            end
        end
        
        p2 = exp(p2);
        p(i, :) = p2 ./ sum(p2);
    end
end