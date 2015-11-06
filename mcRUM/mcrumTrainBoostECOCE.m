function model = mcrumTrainBoostECOCE(X, T, C, M, U, theta, nbag, ...
                                      bagfrac, useBias, MAX_ITER, EPS)
    % Default parameters
    default('nbag', 5);
    default('bagfrac', 1.0);
    default('useBias', true);
    default('EPS', 1e-3);  % for convergence
    default('MAX_ITER', 1000);

    % Initialize variables
    Nc = size(T, 2); % number of classes
    Np = size(C, 2); % number of binary predictors
    model.W = zeros(M, Np, nbag);
    model.b = zeros(nbag, Np);
    model.alpha = zeros(Np, nbag);
    model.r = 0;
    model.Nc = Nc;
    model.C = C;
    model.n = zeros(1, Np);
    model.U = U;
    model.theta = theta;
    model.balp = zeros(nbag, Np);
    K = cRumKernelMatrixE(X, U, theta, useBias);
    
    % Train individual binary CRUMs
    for i = 1:Np        
        pos_class = find(C(:, i) == 1);
        neg_class = find(C(:, i) == -1);
        Xp = [];
        Kp = [];
        Xn = [];
        Kn = [];
        
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
        
        bmodel = binCrumBoostTrainE([Xp; Xn], [Kp; Kn], t, M, U, theta, ...
            nbag, bagfrac, useBias, MAX_ITER, EPS);
        model.W(:, i, :) = bmodel.W;
        model.b(:, i) = bmodel.b;
        model.alpha(i, :) = bmodel.alpha;
        model.n(i) = size(t, 1);
        model.balp(:, i) = bmodel.balp;
        %save temp_mcrum model;
    end
end