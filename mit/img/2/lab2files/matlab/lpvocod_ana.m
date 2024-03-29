function [coeff, gain, pitch] = lpvocod_ana(x,p)
%LPVOCOD_ANA  Speech waveform analyzer template
%   [COEFF,GAIN,PITCH] = LPVOCOD_ANA(X,P) analyzes the speech waveform using an
%   LP vocoder. Input X is the speech waveform vector, and input P is the order
%   of the LPC model. The speech vector is split into 30 ms frames, with 50%
%   overlap between frames. Output COEFF is the matrix of LP coefficients, where
%   each column index is a frame number, and each row index is a coefficent
%   number. GAIN is a vector of gain values (one per frame). PITCH is a vector
%   of pitch values (one per frame), where 0 = unvoiced.
%
%   You are responsible for updating this function to make it fully operational.

% Last Modified: 3/22/06, Eric Weiss (formatting updated)

% Make x a column vector just to be sure.
x = x(:);

% Initialize variables for loop.
Fs = 8000;			        % sampling frequency
frlen = floor(0.03*Fs);	    % length of each data frame, 30ms
noverlap = floor(frlen/2);  % overlap of successive frames, half of frlen
hop = frlen-noverlap;	    % amount to advance for next data frame
nx = length(x);	            % length of input vector
len = fix((nx - (frlen-hop))/hop);	%length of output vector = total frames

% preallocate outputs for speed
[gain, pitch] = deal(zeros(1,len));
coeff = zeros(p+1, len);

% Design (but do not yet apply) a lowpass filter with 500 Hz cutoff
% frequency, since we're interested in pitch, which is 80-320 Hz for
% adult voices. Make the filter length substantially shorter than the
% frame length...


% Here's the loop. Each iteration processes one frame of data.

for i = 1:len
    % Get the next segment/frame of the unfiltered input signal.
    % The indexing has been done for you.
    seg = x(((i-1)*hop+1):((i-1)*hop+frlen));

    % Compute the LPC coefficients and gain of the windowed segment ('lpcoef')
    % and store in coeff matrix and gain vector...

    % Compute the LP error signal

    % Detect voicing and pitch for this frame by applying 500 Hz lowpass filter
    % to error signal and then calling your pitch detector...

end;  		% end for loop

% Remove spurious values from pitch signal with median filter...

