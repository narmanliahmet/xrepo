clear all
close all
clc

I = imread('directory/to/image.jpeg');

I = imresize(I,[400,400]);

for n = 1:1600
    if n<401
    I_1(:,n,:) = improfile(I,[200,1+n-1],[200,1],1600);
    elseif n<801
        I_1(:,n,:) = improfile(I,[200,400],[200,1+n-1-400],1600);
    elseif n<1201
        I_1(:,n,:) = improfile(I,[200,400-(n-800)-1],[200,400],1600);
    elseif n<1601
        I_1(:,n,:) = improfile(I,[200,1],[200,400-(n-1200)-1],1600);
    end
end
I_1 = rot90(I_1,2);
figure();
imshow(I);
figure();
imshow(uint8(I_1));
