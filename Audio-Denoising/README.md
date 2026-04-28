# Audio Denoising Using FFT and Digital Filtering 🎧

This project demonstrates practical Digital Signal Processing (DSP) techniques
applied to an audio signal using Python.

The goal is to analyze an audio signal in both the time and frequency domains,
reduce noise using a digital filter, and save the cleaned audio output.

---

## Project Features
- Load and analyze a WAV audio file
- Convert stereo audio to mono
- Time-domain signal visualization
- Frequency-domain analysis using FFT
- Noise reduction using a Butterworth low-pass filter
- Audio normalization and safe saving

---

## Project Structure

Audio-Denoising-Project/
│
├── audio.wav               # Original audio file
├── clean_audio.wav         # Filtered audio output
├── audio_denoising.ipynb   # Python notebook with full processing steps
├── README.md
└── figures/                # Plots and figures 

---

## Tools and Libraries

- Python 3
- NumPy
- SciPy
- Matplotlib

---

## Methodology

### 1. Audio Loading
- Read the WAV audio file
- Extract the sampling rate
- Convert stereo audio to a single mono channel

### 2. Time Domain Analysis
- Create a time axis using the sampling rate
- Plot audio amplitude versus time

### 3. Frequency Domain Analysis
- Apply Fast Fourier Transform (FFT)
- Compute the magnitude spectrum
- Identify dominant frequency components

### 4. Digital Filter Design
- Design a Butterworth low-pass digital filter
- Select an appropriate cutoff frequency

### 5. Filtering
- Apply zero-phase filtering using `filtfilt`
- Reduce high-frequency noise while preserving signal shape

### 6. Normalization and Saving
- Normalize the filtered signal to prevent clipping
- Convert the signal to 16-bit format
- Save the processed audio as a WAV file

---

## Results

- High-frequency noise is significantly reduced
- Main audio components are preserved
- Frequency spectrum shows clear attenuation after filtering
- The filtered audio sounds cleaner and more stable

---

## How to Run

Install required libraries:

```bash
pip install numpy scipy matplotlib

Run the notebook or script:

python audio_denoising.py

Notes

The original audio file is stereo and converted to mono before processing
Filtering is performed in the frequency domain
Normalization is required before saving audio files


Conclusion
This project demonstrates how FFT and digital filtering techniques can be
effectively used to analyze and clean audio signals. It provides a solid
foundation for further exploration in audio processing and DSP applications.

This project is intended for learning and demonstration purposes.


