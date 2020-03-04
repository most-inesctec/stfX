function [Transform, C]=prlgdemo()
clear;
close;
clc;

warning('off', 'all');
disp("THIS IS A DEMOOOOO")

addpath('./CPD');
addpath('./SC');
addpath('./data');

% Loading the point sets and assigning them to X and Y (target)
load data/save_fish_def_5_1.mat
X = x1;
Y = y2a;
disp(X)
disp(Y)

% Algorithm configurations
opt.outliers = 0.5;
opt.viz = 1;
% Has no default value: confidence of featurs correspondence
opt.t = 0.9;
opt.sparse = 0;
opt.nsc = 5;
% opt.normalize = 0;
% opt.beta = 2;
% opt.lambda = 3;
% opt.tol = 1e-10;

% Applying Point Set Registration
[Transform, C]=prgls_register(Y, X, opt);
V = Transform.Y;

disp(Transform)
figure,cpd_plot_iter(X, Y); axis off; title('Before');
figure,cpd_plot_iter(Transform.Y, y2a); axis off; title('After registering Y to X');
