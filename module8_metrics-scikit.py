import numpy as np
from sklearn.metrics import precision_score, recall_score

def main():
    try:
        N = int(input("Enter the number of data points (N): "))
        if N <= 0:
            raise ValueError("N must be a positive integer.")

        # Initialize arrays to hold the true and predicted labels
        true_labels = np.zeros(N, dtype=int)
        predicted_labels = np.zeros(N, dtype=int)

        # Collecting data from the user
        for i in range(N):
            x = int(input(f"Enter the ground truth class label for point {i+1} (0 or 1): "))
            y = int(input(f"Enter the predicted class label for point {i+1} (0 or 1): "))
            if x not in [0, 1] or y not in [0, 1]:
                raise ValueError("Labels must be either 0 or 1.")
            true_labels[i] = x
            predicted_labels[i] = y

        # Calculating precision and recall
        precision = precision_score(true_labels, predicted_labels)
        recall = recall_score(true_labels, predicted_labels)

        # Outputting the results
        print(f"Precision: {precision:.4f}")
        print(f"Recall: {recall:.4f}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
