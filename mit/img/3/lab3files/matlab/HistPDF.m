function [pdf,x] = HistPDF(data, num_bins, min_max)
%HISTPDF  Create a PDF from input data using a histogram approach (template)
%   [PDF,X] = HISTPDF(DATA,NUMBINS,MIN_MAX) estimates the probability density
%   function for input vector DATA using a histogram approach with the number of
%   histogram bins set by NUM_BINS. The optional input MIN_MAX is a size-two
%   vector that specifies the minimum and maximum allowable data range to
%   include in the histogram estimation, i.e. [MIN,MAX]. The default value for
%   MIN_MAX is the minimum/maximum values of the range of input DATA.
%
%   The output PDF is a probability density (mass) function that sums to 1. The
%   output X are the corresponding range values, such that PDF = pdf(X). You can
%   subsequently plot your pdf by: plot(x,pdf).
%
%   You are responsible for updating this function to make it fully operational.

% Last Modified: 4/06/06, Eric Weiss


% Input argument checking
%------------------------
if nargin < 2
    error('HISTPDF: You must enter data and number of bins.');
end;
if nargin < 3
    min_max = [min(data),max(data)];
end;

% Specify bin centers
%--------------------
% bin_centers is a vector of length num_bins that specifies the centers of all
% histogram bins. This will be one of your inputs to hist.m.
bin_centers = 

% Call the HIST function
%-----------------------
%  bin_counts is a vector that holds the number of data values that correspond
%  to each bin
bin_counts = hist(...);

% Normalization factor
%---------------------
% Establish a normalization factor so that the returned PDF integrates (sums) to
% one
normalization =

% Return PDF and X
%-----------------
% Normalize your pdf, and specify your pdf range X.
pdf = ...
x = ...
