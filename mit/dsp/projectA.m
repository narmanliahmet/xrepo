clear all
close all
clc

load projIA.mat

y = filter(b, a ,speech);
t = linspace(0,length(speech)/fs, length(speech));
figure();
subplot(2,1,1);
plot(t, speech)
xlabel('Time(s)')
subplot(2,1,2)
plot(t, y)
xlabel('Time(s)')