function [C, maxCD] = ...
    cRumKMeansE(X, M, nrep, MAX_ITER)
    
    default('nrep', 1);
    default('MAX_ITER', 1000);

    options = statset('MaxIter', MAX_ITER, 'UseParallel', 'always');
    [~, centers] = kmeans(X, M, 'options', options, ...
            'onlinephase', 'off', 'Replicates', nrep, 'distance', 'cityblock');
    
    C = centers';
    pD = pdist(centers);
    maxCD = max(pD);
end