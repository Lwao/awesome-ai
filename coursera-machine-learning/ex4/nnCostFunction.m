function [J grad] = nnCostFunction(nn_params, ...
                                   input_layer_size, ...
                                   hidden_layer_size, ...
                                   num_labels, ...
                                   X, y, lambda)
%NNCOSTFUNCTION Implements the neural network cost function for a two layer
%neural network which performs classification
%   [J grad] = NNCOSTFUNCTON(nn_params, hidden_layer_size, num_labels, ...
%   X, y, lambda) computes the cost and gradient of the neural network. The
%   parameters for the neural network are "unrolled" into the vector
%   nn_params and need to be converted back into the weight matrices. 
% 
%   The returned parameter grad should be a "unrolled" vector of the
%   partial derivatives of the neural network.
%

% Reshape nn_params back into the parameters Theta1 and Theta2, the weight matrices
% for our 2 layer neural network
Theta1 = reshape(nn_params(1:hidden_layer_size * (input_layer_size + 1)), ...
                 hidden_layer_size, (input_layer_size + 1));

Theta2 = reshape(nn_params((1 + (hidden_layer_size * (input_layer_size + 1))):end), ...
                 num_labels, (hidden_layer_size + 1));

% Setup some useful variables
m = size(X, 1);
         
% You need to return the following variables correctly 
J = 0;
Theta1_grad = zeros(size(Theta1));
Theta2_grad = zeros(size(Theta2));


% ====================== YOUR CODE HERE ======================
% Instructions: You should complete the code by working through the
%               following parts.
%
% Part 1: Feedforward the neural network and return the cost in the
%         variable J. After implementing Part 1, you can verify that your
%         cost function computation is correct by verifying the cost
%         computed in ex4.m
%
% Part 2: Implement the backpropagation algorithm to compute the gradients
%         Theta1_grad and Theta2_grad. You should return the partial derivatives of
%         the cost function with respect to Theta1 and Theta2 in Theta1_grad and
%         Theta2_grad, respectively. After implementing Part 2, you can check
%         that your implementation is correct by running checkNNGradients
%
%         Note: The vector y passed into the function is a vector of labels
%               containing values from 1..K. You need to map this vector into a 
%               binary vector of 1's and 0's to be used with the neural network
%               cost function.
%
%         Hint: We recommend implementing backpropagation using a for-loop
%               over the training examples if you are implementing it for the 
%               first time.
%
% Part 3: Implement regularization with the cost function and gradients.
%
%         Hint: You can implement this around the code for
%               backpropagation. That is, you can compute the gradients for
%               the regularization separately and then add them to Theta1_grad
%               and Theta2_grad from Part 2.

% for c = 1:num_labels
%     J = J + sum(-(y==c).*log(h(:,c)) - (1-(y==c)).*log(1-h(:,c)))/m;
% end
% J = J + lambda/(2*m) * (sum(reshape(Theta1(:,2:end).^2,[],1)) + sum(reshape(Theta2(:,2:end).^2,[],1)));


%+ lambda/(2*m)*sum(theta(2:end).^2);
% grad = X'*(sigmoid(X*theta)-y)/m;
% grad(2:end) = grad(2:end) + lambda/m*theta(2:end);



D_acc{2} = zeros(m, size(Theta2,2));
D_acc{1} = zeros(m, size(Theta1,2));

% step 1
% FP
a{1} = [ones(m,1) X];
z{2} = a{1}*Theta1';
a{2} = [ones(m,1) sigmoid(z{2})];
z{3} = a{2}*Theta2';
a{3} = sigmoid(z{3});
h = a{3};

% step 2
% map y to binary vector
out = zeros(m,num_labels);
for t = 1:m out(t,y(t)) = 1; end
% compute delta of the third layer
delta{3} = h-out;

% step 3
% compute delta of the second layer
delta{2} = delta{3}*Theta2(:,2:end).*sigmoidGradient(z{2});

% step 4
D_acc{2} = Theta2_grad;
D_acc{1} = Theta1_grad;
D_acc{2} = D_acc{2} + delta{3}'*a{2};
D_acc{1} = D_acc{1} + delta{2}'*a{1};

% step 5
Theta2_grad = D_acc{2}/m;
Theta1_grad = D_acc{1}/m;

% extra step - regularization

Theta2_grad(:,2:end) = D_acc{2}(:,2:end)/m + lambda/m * Theta2(:,2:end);
Theta1_grad(:,2:end) = D_acc{1}(:,2:end)/m + lambda/m * Theta1(:,2:end);

    

for c = 1:num_labels
    J = J + sum(-(y==c).*log(h(:,c)) - (1-(y==c)).*log(1-h(:,c)))/m;
end
J = J + lambda/(2*m) * (sum(reshape(Theta1(:,2:end).^2,[],1)) + sum(reshape(Theta2(:,2:end).^2,[],1)));





% -------------------------------------------------------------

% =========================================================================

% Unroll gradients
grad = [Theta1_grad(:) ; Theta2_grad(:)];


