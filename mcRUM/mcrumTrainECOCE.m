function model = mcrumTrainECOCE(X, T, C, M, useBias, NREP, MAX_ITER, EPS, kernelType)
    % Default parameters
    default('useBias', true);
    default('NREP', 1); % for k-means
    default('EPS', 1e-3);  % for convergence
    default('MAX_ITER', 1000);
    default('kernelType', 1);

    % Initialize variables
    [N, q] = size(X); % number and dimension of data
    Nc = size(T, 2); % number of classes
    Np = size(C, 2); % number of binary predictors
    model.W = zeros(M, Np);
    model.b = zeros(1, Np);
    model.alpha = zeros(Np, 1);
    model.r = 0;
    model.Nc = Nc;
    model.C = C;
    model.n = zeros(1, Np);
    
    % Use K-means to estimate U
    %fprintf('K-means...\n')
    [U, maxCD] = cRumKMeansE(X, M, NREP);
    %[U, maxCD] = cRumLiteKMeansE(X, M, NREP); 
    theta = 1 / (2 * maxCD^2);
    K = cRumKernelMatrixE(X, U, theta, useBias, kernelType);
    model.U = U;
    model.theta = theta;
    
    % Train individual binary CRUMs
    for i = 1:Np        
        pos_class = find(C(:, i) == 1);
        neg_class = find(C(:, i) == -1);
        Xp = [];
        Kp = [];
        Xn = [];
        Kn = [];
        t = [];
        
        % Build positive data
        for j = 1:size(pos_class, 1)
            Xp = [Xp; X(T(:, pos_class(j)) == 1, :)];
            Kp = [Kp; K(T(:, pos_class(j)) == 1, :)];
        end
        
        % Build negative data
        for j = 1:size(neg_class, 1)
            Xn = [Xn; X(T(:, neg_class(j)) == 1, :)];
            Kn = [Kn; K(T(:, neg_class(j)) == 1, :)];
        end
        
        t = [ones(size(Xp, 1), 1); zeros(size(Xn, 1), 1)];
        
        bmodel = binCrumTrainE([Xp; Xn], [Kp; Kn], t, M, U, theta, useBias, ...
            MAX_ITER, EPS);
        %model.W(:, i) = bmodel.w;
        %model.b(i) = bmodel.b;
        %model.alpha(i) = bmodel.alpha;
        model.W(:, i) = gather(bmodel.w);
        model.b(i) = gather(bmodel.b);
        model.alpha(i) = gather(bmodel.alpha);
        model.n(i) = size(t, 1);
        %save temp_mcrum model;
    end
end