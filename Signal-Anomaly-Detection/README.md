Signal Anomaly Detection Using DSP and Machine Learning 🚨 

This project demonstrates signal anomaly detection using a combination of Digital Signal Processing (DSP) techniques and machine learning. The goal is to distinguish between normal (clean) and abnormal (noisy) signals by extracting meaningful features from both the time domain and frequency domain, followed by classification using a Random Forest model. 

 

📌 Project Overview 

In many real-world systems (e.g., vibration monitoring, sensor networks, industrial machines), signals are often corrupted by noise or abnormal behavior. This project simulates such a scenario by: 

Generating a multi-frequency signal 

Injecting controlled noise 

Applying digital filtering to recover normal behavior 

Extracting discriminative features 

Training a machine learning classifier to detect anomalies 

The project focuses on interpretability and engineering intuition, not just accuracy. 

 

🔊 Signal Model 

Base signal: Sum of three sinusoidal components with different frequencies and phases 

Sampling frequency: 150 Hz 

Normal signals: Noisy signal passed through a Butterworth low-pass filter 

Abnormal signals: Noisy signal without filtering 

This setup emulates practical scenarios such as sensor noise and vibration disturbances. 

 

🧠 Feature Extraction 

Features are extracted from each signal instance to characterize its behavior. 

Time-Domain Features 

Mean 

Root Mean Square (RMS) 

Energy 

Standard Deviation (STD) 

Frequency-Domain Features 

Dominant Frequency 

Spectral Energy 

Spectral Centroid 

These features capture both signal strength and spectral structure, which are essential for anomaly detection. 

 

📊 Feature Visualization 

To gain intuition before applying machine learning, a feature-space visualization is used: 

Dominant Frequency vs RMS 

This scatter plot highlights the separation between normal and abnormal signals and provides a clear justification for using a classifier. 

Saved figures: 

figures/feature_scatter.png 

 

🤖 Machine Learning Model 

Classifier: Random Forest 

Train/Test split: 70% / 30% (stratified) 

Feature scaling: StandardScaler (fit on training data only) 

Although tree-based models do not strictly require feature scaling, it is included as a best practice and to keep the pipeline extensible to other models. 

 

📈 Evaluation Metrics 

The model performance is evaluated using: 

Accuracy 

Confusion Matrix 

Precision, Recall, and F1-score 

Feature Importance 

Saved figures: 

figures/confusion_matrix.png 

Feature importance analysis shows that noise-related features (RMS, energy, spectral energy) play a dominant role in distinguishing abnormal signals. 

 

📂 Project Structure 

1     Signal-Anomaly-Detection/ 

2     │ 

3     ├── signal_anomaly_detection.py 

4     ├── figures/ 

5     │   ├── feature_scatter.png 

6     │   └── confusion_matrix.png 

7     ├── README.md 

8     └── requirements.txt 

9      

 

🛠️ Requirements 

Install the required Python libraries using: 

1     pip install -r requirements.txt 

2      

requirements.txt: 

1     numpy 

2     scipy 

3     matplotlib 

4     seaborn 

5     scikit-learn 

6      

 

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

 

📬 Feel free to explore, reuse, or extend this project for learning or practical applications. 
