clear all
close all
clc

load projIB.mat
Wp = 2500/(fs/2);
Ws = 4000/(fs/2);
Rp = 40-37;
Rs = -55;
[n, Wn] = buttord(Wp, Ws, Rp, Rs);

[b,a] = butter(n, Wn, 'low');
freqz(b,a)

out = filter(b, a, noisy);
t = linspace(0,round(length(noisy)/fs),length(noisy));

figure();
subplot(2,1,1);
plot(t, noisy)
ylabel("Noisy")
subplot(2,1,2);
plot(t, out)
ylabel("Filtered")