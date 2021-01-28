% This script gets filter coefficients for sensing the cube for the mercury
% 2020 challenge.

clear
close all

% General variables
%samplingFreq = 500; % Sample at 500Hz
samplingFreq = 500/2; % Sample at 500Hz
Fs = samplingFreq; % Easy shorthand

%% Generate the lower frequency pass band
passBandLowerThresh = 1; % 1Hz
passBandUpperThresh = 8; % 8Hz

stopBandLowerThresh = 0.5; % 0Hz
stopBandUpperThresh = 9; % 9Hz
[order, cutoffs] = buttord(...
    [passBandLowerThresh passBandUpperThresh]/Fs, ...
    [stopBandLowerThresh stopBandUpperThresh]/Fs, ...
    3, ... % 3 dB in pass band
    9);   % 40 dB in stop band
[z, p, k] = butter(order, cutoffs);
sos = zp2sos(z, p, k);
[H,w] = freqz(sos, 128, Fs*2);

% Plot the filter
figure
plot(w, abs(H));
xlabel('Frequency (Hz)')
ylabel('Magnitude')

%% Generate the higher frequency pass band
passBandLowerThresh = 9; % 1Hz
passBandUpperThresh = 11; % 8Hz

stopBandLowerThresh = 8; % 0Hz
stopBandUpperThresh = 12; % 9Hz
[order, cutoffs] = buttord(...
    [passBandLowerThresh passBandUpperThresh]/Fs, ...
    [stopBandLowerThresh stopBandUpperThresh]/Fs, ...
    3, ... % 3 dB in pass band
    9);   % 40 dB in stop band
[z, p, k] = butter(order, cutoffs);
sos = zp2sos(z, p, k);
[H,w] = freqz(sos, 128, Fs*2);

% Plot the filter
figure
plot(w, abs(H));
xlabel('Frequency (Hz)')
ylabel('Magnitude')


%% Test both filters
% Generate square waves
% We want 0.5Hz resolution, so we need to sample for 2 seconds
t = 1:1/(Fs*2):2;
freq = 1; % 10 Hz
duty = 50;
% x = square(2*pi*t*freq, duty);
x = sin(2 * pi * freq * t);

figure
plot(t, x)

X = fft(x);
figure
plot(abs(X))
