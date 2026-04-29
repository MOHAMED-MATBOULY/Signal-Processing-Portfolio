import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from scipy.signal import butter, filtfilt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


# ======================================================
# Reproducibility
# ======================================================
np.random.seed(42)


# ======================================================
# Signal generation
# ======================================================
fs = 150
t = np.arange(0, 5, 1/fs)

f1, f2, f3 = 30, 45, 60

signal1 = 2 * np.sin(2 * np.pi * f1 * t + np.pi)
signal2 = 3 * np.sin(2 * np.pi * f2 * t + (5 * np.pi / 8))
signal3 = 7 * np.sin(2 * np.pi * f3 * t + (3 * np.pi / 2))

signal = signal1 + signal2 + signal3


# ======================================================
# Butterworth Low-pass Filter
# ======================================================
order = 4
cut_off = 40
norm_freq = cut_off / (fs / 2)

b, a = butter(order, norm_freq, btype="low")


# ======================================================
# Dataset construction
# ======================================================
features = []
labels = []

# -------- Normal signals (filtered) --------
for _ in range(70):
    noise = 1.6 * np.random.randn(len(signal))
    noisy_signal = signal + noise
    clean_signal = filtfilt(b, a, noisy_signal)

    fft_vals = np.fft.fft(clean_signal)
    mag = np.abs(fft_vals) / len(fft_vals)
    freq = np.fft.fftfreq(len(mag), 1/fs)

    pos_mag = mag[freq >= 0]
    pos_freq = freq[freq >= 0]

    dom_freq = pos_freq[np.argmax(pos_mag)]
    spec_energy = np.sum(pos_mag**2)
    spec_centroid = np.sum(pos_freq * pos_mag) / np.sum(pos_mag)

    energy = np.sum(clean_signal**2)
    mean = np.mean(clean_signal)
    rms = np.sqrt(np.mean(clean_signal**2))
    std = np.std(clean_signal)

    features.append([
        dom_freq, spec_energy, spec_centroid,
        energy, mean, rms, std
    ])
    labels.append(0)  # Normal


# -------- Abnormal signals (noisy) --------
for _ in range(70):
    noise = 1.6 * np.random.randn(len(signal))
    noisy_signal = signal + noise

    fft_vals = np.fft.fft(noisy_signal)
    mag = np.abs(fft_vals) / len(fft_vals)
    freq = np.fft.fftfreq(len(mag), 1/fs)

    pos_mag = mag[freq >= 0]
    pos_freq = freq[freq >= 0]

    dom_freq = pos_freq[np.argmax(pos_mag)]
    spec_energy = np.sum(pos_mag**2)
    spec_centroid = np.sum(pos_freq * pos_mag) / np.sum(pos_mag)

    energy = np.sum(noisy_signal**2)
    mean = np.mean(noisy_signal)
    rms = np.sqrt(np.mean(noisy_signal**2))
    std = np.std(noisy_signal)

    features.append([
        dom_freq, spec_energy, spec_centroid,
        energy, mean, rms, std
    ])
    labels.append(1)  # Abnormal


X = np.array(features)
y = np.array(labels)


# ======================================================
# Visualization (Feature space)
# ======================================================
plt.figure(figsize=(8, 6))
plt.scatter(X[y == 0, 0], X[y == 0, 5], label="Normal", alpha=0.7)
plt.scatter(X[y == 1, 0], X[y == 1, 5], label="Abnormal", alpha=0.7)

plt.xlabel("Dominant Frequency")
plt.ylabel("RMS")
plt.title("Normal vs Abnormal Signal Features")
plt.legend()
plt.grid(True)
plt.savefig("figures/feature_scatter.png", dpi=120, bbox_inches="tight")
plt.close()


# ======================================================
# Train / Test split
# ======================================================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, stratify=y, random_state=42
)


# ======================================================
# Feature Scaling
# ======================================================
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


# ======================================================
# Model training
# ======================================================
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train_scaled, y_train)


# ======================================================
# Evaluation
# ======================================================
y_pred = model.predict(X_test_scaled)

accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.savefig("figures/confusion_matrix.png", dpi=120, bbox_inches="tight")
plt.close()

print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))


# ======================================================
# Feature Importance
# ======================================================
feature_names = [
    "Dominant Frequency",
    "Spectral Energy",
    "Spectral Centroid",
    "Energy",
    "Mean",
    "RMS",
    "STD"
]

importances = model.feature_importances_

print("\nFeature Importance:")
for name, value in zip(feature_names, importances):
    print(f"{name}: {value:.4f}")
