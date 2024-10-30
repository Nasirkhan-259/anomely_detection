import numpy as np
import matplotlib.pyplot as plt


# Anomaly Detection using Z-Score Method
# The Z-Score method is effective for detecting anomalies based on standard deviations from the mean.
# It adapts well to concept drift as it recalculates the mean and standard deviation on the fly.

def generate_data_stream(n=1000, anomaly_rate=0.01):
    # Validate inputs
    if n <= 0:
        raise ValueError("n must be a positive integer")
    if not (0 <= anomaly_rate <= 1):
        raise ValueError("anomaly_rate must be between 0 and 1")

    time = np.arange(n)

    # Regular pattern (sinusoidal)
    signal = 10 * np.sin(2 * np.pi * time / 50)

    # Seasonal component (cosine wave)
    seasonal = 5 * np.cos(2 * np.pi * time / 200)

    # Random noise
    noise = np.random.normal(0, 1, n)

    # Combine to create the data stream
    data_stream = signal + seasonal + noise

    # Introduce anomalies
    num_anomalies = int(n * anomaly_rate)
    anomaly_indices = np.random.choice(n, num_anomalies, replace=False)
    data_stream[anomaly_indices] += np.random.normal(20, 5, num_anomalies)  # Large spikes

    return data_stream


def detect_anomalies(data_stream, threshold=3):
    mean = np.mean(data_stream)
    std_dev = np.std(data_stream)

    anomalies = []
    for i, value in enumerate(data_stream):
        z_score = (value - mean) / std_dev
        if abs(z_score) > threshold:
            anomalies.append((i, value))  # Store index and value of anomaly

    return anomalies


def visualize_stream(data_stream, anomalies):
    plt.figure(figsize=(10, 6))
    plt.plot(data_stream, label='Data Stream', color='blue')

    if anomalies:
        anomaly_indices, anomaly_values = zip(*anomalies)
        plt.scatter(anomaly_indices, anomaly_values, color='orange', label='Anomalies')

    plt.title('Data Stream with Anomalies')
    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.legend()
    plt.show()


def main():
    # Generate data stream
    data_stream = generate_data_stream(n=500, anomaly_rate=0.05)

    # Detect anomalies
    anomalies = detect_anomalies(data_stream, threshold=3)

    # Visualize results
    visualize_stream(data_stream, anomalies)


if __name__ == "__main__":
    main()
