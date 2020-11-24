clear all
close all
clc
bist = csvread("bist-30.csv");
Ya = autocorr(bist(1:end-337),'NumLags',200,'NumSTD',5);
stand = std(bist(end-337-5-4:end-337-5));
meand = mean(bist(end-337-5-4:end-337-5));
next = zeros(1,5);
next(1) = bist(end-337-5);

while ~(abs(corr(next',bist(end-337-5-4:end-337-5))-Ya(2))<2e-2)
    next(2:5) = stand.*randn(1,4)/2+ meand;
    disp(abs(corr(next',bist(end-337-5-4:end-337-5))-Ya(2)));
end

figure();
plot(bist(end-337-4:end-337));
hold on;
plot(next);
legend("Real","Predicted");