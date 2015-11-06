function model = ...
    cRumTrainKMeansMAP(X, t, M, useBias, kernelType, nrep, MAX_ITER, EPS)
    
    default('useBias', true);
    default('kernelType', 2);
    default('nrep', 1);
    default('EPS', 1e-3);  % for convergence
    default('MAX_ITER', 1000);

    % Initial values
    [N, q]= size(X); % number and dimension of data
    Mb = M;
    if useBias
        Mb = M + 1;
    end
    
    w = zeros(Mb, 1);
    alpha = (1 / (M + 1)^2);
    
    % Use K-means to estimate U
    %fprintf('K-means...\n')
    [U, maxCD] = cRumKMeans(X, M, kernelType, nrep); 
    theta = 1 / (2 * maxCD^2);

    converged = 0;
    t = logical(t);
    K = cRumKernelMatrix(X, U, theta, useBias, kernelType);
    
    iter = 0;
    while ~converged && iter < MAX_ITER
        iter = iter + 1;

        if (mod(iter, 100) == 0)
            fprintf('Iteration: %d \n', iter)
        end

        % Update old values
        alphaOld = alpha;

        % Estimate w
        R = cRumEstimateW(2000);

        % Estimate alpha using new w (RVM eqn, uninformative prior)
        cRumEstimateAlpha(R);
        
        % Save model in case of error
        if useBias
            model.b = w(Mb);
        end
        model.w = w(1:M);
        model.U = U;
        model.theta = theta;
        model.alpha = alpha;
        %save temp_model model
        
        % Check if converged
        dAlpha = max(abs(log(alpha) - log(alphaOld)));

        %fprintf('Convergence: %d\n', dAlpha)

        if dAlpha < EPS
            converged = 1;
        end
    end

    % Adapted from Tipping's RVM code
    function R = cRumEstimateW(its)
        %fprintf('\tEsimating W\n')
        gradStop = 1e-6;
        lamdaMin= 2^(-8);
        A = diag(alpha * ones(Mb, 1));
        y = cRumSigmoid(K * w);
        err = cRumEstimateWError(w, y) + (alpha'*(w.^2)) / 2;
        
        for i = 1:its
            errOld = err;
            wOld = w;
            grad = K' * (t - y) - alpha .* wOld;
            B = K .* ((y .* (1 - y)) * ones(1, Mb));
            H = B' * K + A;
            [R, pdErr] = chol(H);
            
            if pdErr
                error('Ill-conditioned Hessian, quitting!');
            end

            delta = R \ (R' \ grad);
            lamda = 1;

            while lamda > lamdaMin
                w = wOld + lamda * delta;
                y = cRumSigmoid(K * w);        
                err = cRumEstimateWError(w, y) + (alpha'*(w.^2)) / 2;
                err = gather(err);

                % Reduce lamda if error increased
                if err > errOld
                    lamda	= lamda/2;
                else
                    break;
                end
            end
            
            % Convergence
            %if norm(grad) / M < gradStop
            if all(abs(grad) < gradStop)
                break;
            end
            
            %fprintf('\tIteration: %d, Norm grad: %d\n', i, norm(grad))
        end

        %fprintf('Estimated w with %d iterations\n', i)
    end

    function err = cRumEstimateWError(w, y)
        y0 = (y == 0);
        y1 = (y == 1);
        if any(y0(t>0)) || any(y1(t<1))
            err = inf;
        else
            err	= -(t(~y0)'*log(y(~y0)) + (1-t(~y1))'*log(1-y(~y1)));
        end
    end

    function cRumEstimateAlpha(R)
        %fprintf('\tEsimating alpha\n')
        Ri = inv(R);
        S = Ri * Ri';
        gamma = M - alpha .* trace(S);
        alpha = gamma ./ dot(w, w);
    end
end
