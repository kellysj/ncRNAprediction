function k = cRumRbfRowE(X, u, gamma, kernelType)
    default('kernelType', 1);
    
    %D = bsxfun(@minus, X', u);
    %d = dot(D, D);
    %d = sum(abs(D));
    %d = sum(abs(D)) .^ 2;
    %normX = sqrt(sum(X .^ 2, 2));
    %normu = sqrt(sum(u .^ 2, 1));
    %d = 1 - bsxfun(@rdivide, bsxfun(@rdivide, X * u, normX), normu);
    %d = pdist2(X, u', 'cosine');
    %d = pdist2(X, u', 'cityblock');
    %k = exp(-gamma .* d .^ 2);
    %k = exp(-gamma .* d);
    
    if kernelType == 1
        d = pdist2(X, u', 'cityblock');
        k = exp(-gamma .* d);
    else
        D = bsxfun(@minus, X', u);
        k = exp(-gamma * dot(D, D));
    end
end