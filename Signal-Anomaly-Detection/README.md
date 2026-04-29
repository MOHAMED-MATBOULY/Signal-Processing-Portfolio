# Signal Anomaly Detection Using DSP and Machine Learning 🚨

This project demonstrates **signal anomaly detection** using a combination of
**Digital Signal Processing (DSP)** techniques and **machine learning**.
The goal is to distinguish between **normal (clean)** and **abnormal (noisy)**
signals based on time-domain and frequency-domain features.

---

## 📌 Project Overview

In many real-world applications such as vibration monitoring, sensor networks,
and industrial machines, signals are often corrupted by noise or abnormal behavior.

This project simulates such a scenario by:
- Generating a multi-frequency signal
- Injecting controlled noise
- Applying digital filtering to recover normal behavior
- Extracting meaningful features
- Training a machine learning model to detect anomalies

The focus is on **engineering intuition and interpretability**, not just accuracy.

---

## 🔊 Signal Model

- **Base signal**: Sum of three sinusoidal components with different frequencies and phases
- **Sampling frequency**: 150 Hz
- **Normal signals**: Noisy signal passed through a Butterworth low-pass filter
- **Abnormal signals**: Noisy signal without filtering

This setup mimics realistic sensor noise and fault conditions.

---

## 🧠 Feature Extraction

Each signal instance is represented using a set of discriminative features.

### Time-Domain Features
- Mean
- Root Mean Square (RMS)
- Energy
- Standard Deviation (STD)

### Frequency-Domain Features
- Dominant Frequency
- Spectral Energy
- Spectral Centroid

These features capture both **signal strength** and **spectral behavior**, which
are critical for anomaly detection.

---

## 📊 Feature Space Visualization

Before applying machine learning, a feature-space visualization is used to
build intuition:

- **Dominant Frequency vs RMS**

This scatter plot highlights the separation between normal and abnormal signals
and justifies the use of a classifier.

Saved figure:
- `figures/feature_scatter.png`

---

## 🤖 Machine Learning Model

- **Classifier**: Random Forest
- **Train/Test split**: 70% / 30% (stratified)
- **Feature scaling**: StandardScaler (fit on training data only)

Although tree-based models do not strictly require feature scaling, it is applied
as a **best practice** and to keep the pipeline extensible to other models.

---

## 📈 Evaluation Metrics

Model performance is evaluated using:
- Accuracy
- Confusion Matrix
- Precision, Recall, and F1-score
- Feature Importance

Saved figure:
- `figures/confusion_matrix.png`

Feature importance analysis shows that **noise-related features (RMS, energy,
spectral energy)** play a dominant role in distinguishing abnormal signals.

---

## 📂 Project Structure

Signal-Anomaly-Detection/
│
├── signal_anomaly_detection.py
├── figures/
│   ├── feature_scatter.png
│   └── confusion_matrix.png
├── README.md
└── requirements.txt
---

## 🛠️ Requirements

Install the required Python libraries using:

```bash
pip install -r requirements.txt

requirements.txt
numpy
scipy
matplotlib
seaborn
scikit-learn

✅ Key Takeaways

DSP-based features provide strong physical interpretability
Visualization helps validate feature usefulness before ML
Machine learning complements signal processing, not replaces it
Avoiding data leakage is critical for reliable evaluation


📌 Notes
This project is designed to be:

Educational
Interpretable
Portfolio-ready
Suitable for real-world sensor anomaly detection tasks


👤 Author
Signal Processing Portfolio Project
