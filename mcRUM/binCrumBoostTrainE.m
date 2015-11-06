function model = ...
    binCrumBoostTrainE(X, K, t, M, U, theta, nbag, bagfrac, useBias, ...
                       MAX_ITER, EPS)
    
    default('nbag', 5);
    default('bagfrac', 1.0);
    default('useBias', true);
    default('EPS', 1e-3);  % for convergence
    default('MAX_ITER', 1000);
    
    [N, q]= size(X); % number and dimension of data
    bw = ones(N, 1) ./ N;
    %bw = log(ones(N, 1) ./ N);
    
    for i = 1:nbag
        trainsample = randsample(N, ceil(N * bagfrac), true, bw);
        %trainsample = randsample(N, ceil(N * bagfrac), true, exp(bw));
        trainX = X(trainsample, :);
        trainK = K(trainsample, :);
        train_t = t(trainsample, :);

        bmodel = binCrumTrainE(trainX, trainK, train_t, M, U, theta, ...
                useBias, MAX_ITER, EPS);
            
        % Adjust weights
        [p, ~] = cRumClassifyE(bmodel, X);
        class = round(p);
        %ep = 0;
        %for j = 1:N
        %    if class(j) ~= t(j)
        %        ep = ep + exp(bw(j));
        %    end
        %end
        %ep = ep / sum(bw);
        %ep = ep / sum(exp(bw));
        %balp = 0.5 * log((1-ep)/ep);
        balp = 1;
        
        %if balp < 0
        %    balp = 0;
        %end
        
        for j = 1:N
            %if class(j) ~= t(j)
            %    %bw(j) = bw(j) * exp(balp);
            %    bw(j) = bw(j) + balp;
            %else
            %    %bw(j) = bw(j) * exp(-balp);
            %    bw(j) = bw(j) - balp;
            %end
            
            t1 = 2 * t(j) - 1;
            bw(j) = bw(j) * exp(-t1 * (2*p(j) - 1));
        end
        %bw = log(exp(bw) ./ sum(exp(bw)));
        bw = bw ./ sum(bw);
        
        model.W(:, i) = bmodel.w;
        model.b(i) = bmodel.b;
        model.alpha(i) = bmodel.alpha;
        model.balp(i) = balp;
    end
end
