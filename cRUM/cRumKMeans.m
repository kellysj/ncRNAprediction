function [C, maxCD] = ...
    cRumKMeans(X, M, kernelType, nrep, MAX_ITER)
    default('kernelType', 2);
    default('nrep', 1);
    default('MAX_ITER', 1000);
    options = statset('MaxIter', MAX_ITER, 'UseParallel', 'always');
    if kernelType == 1
        [~, centers] = kmeans(X, M, 'options', options, ...
            'onlinephase', 'off', 'Replicates', nrep, ...
            'distance', 'cityblock');
    else
        [~, centers] = kmeans(X, M, 'options', options, ...
            'onlinephase', 'off', 'Replicates', nrep);
    end
    C = centers';
    pD = pdist(centers);
    maxCD = max(pD);
end