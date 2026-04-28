# Signal Anomaly Detection 🚨

This project demonstrates anomaly detection in signals using
Digital Signal Processing (DSP) techniques combined with
machine learning.

The objective is to distinguish between normal and abnormal
signal behavior based on statistical and spectral features.

---

## Project Overview

A synthetic sinusoidal signal is generated and corrupted with
different noise levels to simulate normal and abnormal conditions.
Relevant features are extracted from both the time and frequency
domains and used to train a machine learning classifier.

---

## Signal Model

- Base signal: Sinusoidal waveform
- Normal condition: Signal + moderate noise
- Abnormal condition: Signal + higher noise
- Sampling frequency ensures no aliasing

---

## Extracted Features

### Time-Domain Features
- Mean
- RMS (Root Mean Square)
- Energy
- Standard Deviation (STD)

### Frequency-Domain Features
- Dominant Frequency
- Spectral Energy
- Spectral Centroid

These features capture both signal strength and spectral behavior.

---

## Machine Learning Model

- Classifier: Random Forest
- Training/Test split with stratification
- Evaluation metrics:
  - Accuracy
  - Confusion Matrix
  - Precision, Recall, and F1-score
  - Feature Importance analysis

---

## Results

- Realistic classification performance with overlapping classes
- High precision for abnormal detection
- Feature importance shows that variability and energy-based
  features are the most influential
- Frequency-based features provide additional discrimination

---

## Tools and Libraries

- Python
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn

---

## Project Structure

Signal-Anomaly-Detection/
│
├── anomaly_detection.ipynb
├── README.md

---

## Key Learning Outcomes

- Practical DSP-based feature extraction
- Understanding class overlap and model errors
- Interpreting confusion matrices and classification reports
- Explaining model decisions using feature importance

---

## Notes

This project focuses on interpretability and signal understanding
rather than achieving perfect accuracy. The dataset is intentionally
designed to be challenging and realistic.

---

## Author

Signal Processing Portfolio Project


