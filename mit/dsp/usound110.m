%
% USOUND110(input)
%
%   Plays contents of vector 'input' on UNIX machines at a
%     sample rate of 11025 Hz.  Values can range from -1 to
%     +1 but may cause the (rather cheap) speaker in your
%     Sun machine to distort unless 'input' is scaled down
%     further.
%
%   Note: this will not work unless you have access to the
%     locker 'infoagents'.  If you don't, add the line
%       add infoagents
%     to your .environment file, log out, and log in again.
%
%   Also note that this function will create a temporary
%     file called 'temp341.au' and will by default over-
%     write any existing file with that name each time it
%     is called.
%

function usound110(ins)

auwrite(ins,11025,16,'linear','temp341.au');
!audioplay temp341.au
