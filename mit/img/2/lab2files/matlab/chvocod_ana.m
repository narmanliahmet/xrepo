function [band_envelopes,pitch] = chvocod_ana(x,D,N_bands)
%CHVOCOD_ANA Channel vocoder analyzer template
%   [BAND_ENVELOPES,PITCH] = CHVOCOD_ANA(X,DECIMATE,N_BANDS) analyzes the speech
%   waveform by means of a channel vocoder. The speech signal X is split into
%   overlapping 30 ms frames. Each frame is split into a N_BANDS frequency bands,
%   enveloped, lowpass filtered, and decimated by decimation factor DECIMATE.
%   These decimated band envelope values are returned in the output 
%   BAND_ENVELOPES, which is matrix with size num_frames by N_BANDS (where
%   num_frames is the number of data frames dividing the signal). The
%   pitch of each frame is detected by the pitch detector, and the pitch outputs
%   are returned in the output variable PITCH.

%   This code template has two separate stages, corresponding to the
%   source-filter model of speech production:
%   (1) The first stage involves characterizing the "source" by pitch detection.
%       Pitch detection is accomplished by breaking up the original signal
%       into frames and then determining if each frame is is voiced or unvoiced.
%       If the frame is voiced, then we also estimate the fundamental frequency
%       of the glottal source.
%   (2) The second stage involves characterizing the "filter", that is
%       determining the band envelope values.  This is accomplished by filtering
%       the original signal into frequency bands, determining the envelope of
%       each band and decimating.
%
%   You are responsible for updating this function to make it fully operational.

% Last Modified: 3/8/06, Eric Weiss


% Constants
%----------
Fs = 8000;			               % sampling frequency
frame_length = floor(0.030 * Fs);  % use 30 ms frame length
num_frames = ceil(length(x)/D);    % total number of frames
% (Note that the number of frames depends on the decimation rate. 
%  Try to understand why.)


% Initializations
%----------------
x = x(:);  % Make x a column vector just to be sure.
pitch = zeros(num_frames, 1);   % preallocate outputs for speed
band_envelope = zeros(num_frames,N_bands);


%------------------------------------------
% Get "source parameters" (pitch detection)
%------------------------------------------
% First, lowpass filter the signal with 500 Hz cutoff frequency,
% since we're interested in pitch, which is 80-320 Hz for adult voices.
% Be careful: the lowpass filtered signal should be used as the input
% to the pitch detector, but not to the filter bank!

xlpf =


% Here's the loop. Each iteration processes one frame of data.

for i = 1:num_frames

    % Get the next segment.  The indexing has been done for you.
    startseg = (i-1)*D+1;
    endseg = startseg + frame_length - 1;
    if endseg > length(xlpf)
        endseg = length(xlpf);
    end
    seg = xlpf(startseg:endseg);

    % Call your pitch detector...
    pitch(i) =

end;

% Remove spurious values from pitch signal with median filter...


%---------------------------------------------------------
% Get "filter" parameters (determine band envelope values)
%---------------------------------------------------------
% Compute FIR coefficients for filter bank (using 65-point filters).
% The variable bank should be a 65xN matrix with each column containing
% the impulse response of one filter

bank = myownfilt_bank(N_bands,65);

% Apply the filterbank to the input signal, x . . .
% Please be sure that you understand why you shouldn't apply
% the filterbank to the lowpass filtered signal, xlpf

% In loop, process each band:
for i = 1:N_bands
    %	Apply filter for this band (bank(:,i)) to input x (not xlpf)...

    % 	Take magnitude of signal and decimate.
    % 	(The matlab function 'decimate.m' includes lowpass filtering)...

end
