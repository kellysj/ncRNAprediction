function [model, likelihood, aic, bic, iter] = ...
    binCrumTrainE(X, K, t, M, U, theta, useBias, MAX_ITER, EPS)
    
    default('useBias', true);
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
    %alpha = 0.00001;

    converged = 0;
    t = logical(t);
    %t = gpuArray(t);
    %gK = gpuArray(K);
    
    iter = 0;
    while ~converged && iter < MAX_ITER
        iter = iter + 1;

        %if (mod(iter, 100) == 0)
            fprintf('Iteration: %d \n', iter)
        %end

        % Update old values
        alphaOld = alpha;

        % Estimate w
        R = cRumEstimateW(25);
        %cRumEstimateW2(25);

        % Estimate alpha using new w (RVM eqn, uninformative prior)
        cRumEstimateAlpha(R);
        %cRumEstimateAlpha2();
        
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

        fprintf('Convergence: %d\n', dAlpha)

        if dAlpha < EPS
            converged = 1;
        end
    end

    % Adapted from Tipping's RVM code
    function R = cRumEstimateW(its)
        %fprintf('\tEsimating W\n')
        % Parameters for Newton-Raphson
        gradStop = 1e-6;
        lamdaMin= 2^(-8);

        A = diag(alpha * ones(Mb, 1));
        y = cRumSigmoid(K * w);
        %gA = gpuArray(diag(alpha * ones(Mb, 1)));
        %gw = gpuArray(w);
        %y = cRumSigmoid(gK * gw);
        
        err = cRumEstimateWError(w, y) + (alpha'*(w.^2)) / 2;
        %err = cRumEstimateWError(gw, y) + (alpha'*(gw.^2)) / 2;
        %err = gather(err);
        
        for i = 1:its
            errOld = err;
            wOld = w;

            % Gradient and Hessian
            grad = K' * (t - y) - alpha .* wOld;
            B = K .* ((y .* (1 - y)) * ones(1, Mb));
            H = B' * K + A;
            %grad = gK' * (t - y) - alpha .* wOld;
            %B = gK .* ((y .* (1 - y)) * ones(1, Mb));
            %H = B' * gK + gA;
            
            % Cholesky decomposition, H = R'R
            [R, pdErr] = chol(H);
            
            if pdErr
                error('Ill-conditioned Hessian, quitting!');
            end

            % delta = inv(H) * grad
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

        fprintf('Estimated w with %d iterations\n', i)
    end

    function R = cRumEstimateW2(its)
        %fprintf('\tEsimating W\n')
        % Parameters for Newton-Raphson
        gradStop = 1e-6;
        lamdaMin= 2^(-8);
        
        y = cRumSigmoid(K * w);        
        err = cRumEstimateWError(w, y) + (alpha'*(w.^2)) / 2;
        
        for i = 1:its
            errOld = err;
            wOld = w;

            % Gradient
            grad = K' * (t - y) - alpha .* wOld;
            delta = grad;
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

        fprintf('Estimated w with %d iterations\n', i)
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

    function cRumEstimateAlpha2()
        %fprintf('\tEsimating alpha\n')
        A = diag(alpha * ones(Mb, 1));
        y = cRumSigmoid(K * w);
        B = K .* ((y .* (1 - y)) * ones(1, Mb));
        H = B' * K + A;
        [R, pdErr] = chol(H);
        
        if pdErr
            error('Ill-conditioned Hessian, quitting!');
        end
        
        Ri = inv(R);
        S = Ri * Ri';
        gamma = M - alpha .* trace(S);
        alpha = gamma ./ dot(w, w);
    end
end
