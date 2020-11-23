clear all
close all
clc

bist = csvread("bist-30.csv");
coef = polyfit(1200:1337-100, bist(1200:1337-100), 2); % Do a linear fit
pred = polyval(coef, 1337-100+1);

disp(bist(1337-100+1));
disp(pred);