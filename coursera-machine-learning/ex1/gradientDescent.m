function [theta, J_history] = gradientDescent(X, y, theta, alpha, num_iters)
%GRADIENTDESCENT Performs gradient descent to learn theta
%   theta = GRADIENTDESCENT(X, y, theta, alpha, num_iters) updates theta by 
%   taking num_iters gradient steps with learning rate alpha

% Initialize some useful values
m = length(y); % number of training examples
J_history = zeros(num_iters, 1);
if (size(X,2)==1)
    X = [ones(m,1),X];
end
for iter = 1:num_iters

    % ====================== YOUR CODE HERE ======================
    % Instructions: Perform a single gradient step on the parameter vector
    %               theta. 
    %
    % Hint: While debugging, it can be useful to print out the values
    %       of the cost function (computeCost) and gradient here.
    %
    
    theta = theta - alpha/m * [ones(1,m)*(X*theta-y);ones(1,m)*((X*theta-y).*X(:,2))];
%     theta(1) = theta(1) - alpha/m * sum(theta(1)+theta(2)*X(:,2)-y);
%     theta(2) = theta(2) - alpha/m * sum((theta(1)+theta(2)*X(:,2)-y).*X(:,2));


    % ============================================================

    % Save the cost J in every iteration    
    J_history(iter) = computeCost(X, y, theta); 
    %disp(J_history(iter))

end
end
