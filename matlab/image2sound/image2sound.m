clear all
close all
clc

image1 = imread('directory/to/image1.jpeg');
image1 = imresize(image1,[962,1880]);
image2 = imread('directory/to/image2.jpeg');
image2 = imresize(image2,[1253,1880]);
image3 = imread('directory/to/image3.jpeg');
phase1 = zeros(962,1880);
for j = 1:1880
for i = 1:962
phase1(i,j) = std(double((reshape(image1(i,j,:),1,3))));
end
end

phase2 = zeros(1253,1880);
for j = 1:1880
for i = 1:1253
phase2(i,j) = std(double((reshape(image2(i,j,:),1,3))));
end
end

phase3 = zeros(1058,1880);
for j = 1:1880
for i = 1:1058
phase3(i,j) = std(double((reshape(image2(i,j,:),1,3))));
end
end

phase1n = 2*pi*(phase1-min(min(phase1)))/(max(max(phase1))-min(min(phase1)));
phase2n = 2*pi*(phase2-min(min(phase1)))/(max(max(phase2))-min(min(phase2)));
phase3n = 2*pi*(phase3-min(min(phase1)))/(max(max(phase3))-min(min(phase3)));

mag1 = sqrt(double(rgb2gray(image1)));
mag2 = sqrt(double(rgb2gray(image2)));
mag3 = sqrt(double(rgb2gray(image3)));

phase1n = [phase1n , phase1n];
phase2n = [phase2n , phase2n];
phase3n = [phase3n , phase3n];

mag1 = [mag1,mag1(end:-1:1,:)];
mag2 = [mag2,mag2(end:-1:1,:)];
mag3 = [mag3,mag3(end:-1:1,:)];


X1 = mag1.*exp(1i*phase1n);
X2 = mag2.*exp(1i*phase2n);
X3 = mag3.*exp(1i*phase3n);
win = rectwin(962);
noverlap=0;
fftlen = 962;
sound1x = istft(X1,2e+3,'Window',win,'OverlapLength',noverlap,'FFTLength',fftlen);
win = rectwin(1253);
noverlap=0;
fftlen = 1253;
sound2x = istft(X2,2e+3,'Window',win,'OverlapLength',noverlap,'FFTLength',fftlen);
win = rectwin(1058);
noverlap=0;
fftlen = 1058;
sound3x = istft(X3,2e+3,'Window',win,'OverlapLength',noverlap,'FFTLength',fftlen);
sound1 = zeros(1,962*1880);
sound2 = zeros(1,1253*1880);
sound3 = zeros(1,1058*1880);
for n=1:1880*2
    sound1(1,962*n-961:962*n) = ifft(X1(:,n));
    sound2(1,1253*n-1252:1253*n) = ifft(X2(:,n));
    sound3(1,1058*n-1057:1058*n) = ifft(X3(:,n));
end
sound1n = sound1(abs(sound1)<0.2);
sound1n = sound1(abs(sound1n)>0.1);
sound(real(sound1n(1:15000)),1500)
pause(10)
sound2n = sound2(abs(sound2)<0.2);
sound2n = sound2(abs(sound2n)>0.1);
sound(real(sound2n(1:20000)),2000)
pause(10)
sound3n = sound3(abs(sound3)<0.2);
sound3n = sound3(abs(sound3n)>0.1);
sound(real(sound3n(1:20000)),2000)
pause(10)
sound(real(sound1x(1:15000)),1500)
pause(10)
sound(real(sound2x(1:15000)),1500)
pause(10)
sound(real(sound3x(1:15000)),1500)
