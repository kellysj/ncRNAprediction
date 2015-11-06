function k = cRumRbfRow(X, u, gamma, kernelType)
    default('kernelType', 2);
    if kernelType == 1 %not really ever used
        d = pdist2(X, u', 'cityblock');
        k = exp(-gamma .* d);
    else
        D = bsxfun(@minus, X', u);
        
%     Example code:
%           A = [1 2 10; 1 4 20;1 6 15] ;
%         C = bsxfun(@minus, A, mean(A))
% 
%         C =
% 
%          0    -2    -5
%          0     0     5
%          0     2     0

        k = exp(-gamma * dot(D, D));
    end
end