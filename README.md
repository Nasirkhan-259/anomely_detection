# Efficient Data Stream Anomaly Detection

## Project Overview

This project implements a anomaly detection system for a simulated continuous data stream using Python. The goal is to identify unusual patterns in real-time sequences of floating-point numbers, which may represent various metrics such as financial transactions or system performence metrics.

## Objectives

- **Algorithm Selection:** Implement a suitable algorithm for anomaly detection capable of adapting to concept drift and seasonal variation.
- **Data Stream Simulation:** Emulate a data stream with regular patterns, seasonal elements, and random noise.
- **Anomaly Detection:** Create a real-time mechanism to accurately flag anomalies as the data streamed.
- **Optimization:** Ensure the algorithm is optimized for speed and efficency.
- **Visualization:** Provide a straightforward visualization tool to display both the data stream and any detected anomalys.

## Algorithm Used

### Z-Score Method

The anomaly detection algorithm used in this project is based on the **Z-Score method**. This statistical method calculates how many standard deviations a data point is from the mean of the data set. The formula for calculating the Z-Score is:

\[ Z = \frac{(X - \mu)}{\sigma} \]

Where:
- \( X \) is the value of the data point
- \( \mu \) is the mean of the data stream
- \( \sigma \) is the standard deviation of the data stream

#### Why Z-Score?

- **Simplicity:** The Z-Score method is easy to understand and implement, making it a good choice for initial anomaly detections.
- **Adaptability:** It adapt well to data distributions that are approximately normal, making it effective for many real-world applications.
- **Dynamic Calculation:** The algorithm recalculates the mean and standard deviation dynamicly, allowing it to adapt to concept drift over time.

## Data Stream Simulation

The data stream is generated using the following components:
- **Regular Pattern:** A sinusoidal wave to simulate periodic behavior.
- **Seasonal Component:** A cosine wave to introduce seasonal variation.
- **Random Noise:** Gaussian noise is added to create a realistic data stream.
- **Anomalies:** Randomly introduced spikes to simulate anomalous behaviors in the data.

## Requirements

- Python 3.x
- NumPy
- Matplotlib

You can install the required libraries using:

```bash
pip install numpy matplotlib
```
- developed by nasir.developer259@gmail.com for Assesment Purpose only