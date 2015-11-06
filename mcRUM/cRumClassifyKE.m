function [p, y] = cRumClassifyKE(model, K)
    y = K * model.w + model.b;
    p = cRumSigmoidE(y);
end