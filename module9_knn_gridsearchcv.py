import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

def collect_data(N):
    input_data = np.zeros(N)
    input_labels = np.zeros(N, dtype=int)
    for i in range(N):
        x = float(input(f"Enter the input feature for data point {i+1}: "))
        y = int(input(f"Enter the class label for data point {i+1}: "))
        input_data[i] = x
        input_labels[i] = y
    return input_data.reshape(-1, 1), input_labels

def main():
    try:
        # Collect data for training
        N = int(input("Enter the number of data points (N): "))
        if N <= 0:
            raise ValueError("N must be a positive integer.")
        x_train, y_train = collect_data(N)

        # Collect data for testing
        M = int(input("Enter the number of test data points (M): "))
        if M <= 0:
            raise ValueError("M must be a positive integer.")
        X_test, y_test = collect_data(M)

        # Find the best k using k-NN from k=1 to k=10
        best_k = None
        best_accuracy = 0
        max_k = min(N, 10)  # Ensure k does not exceed the number of training samples

        for k in range(1, max_k+1):  # Check k from 1 to 10
            knn = KNeighborsClassifier(n_neighbors=k)
            knn.fit(x_train, y_train)
            y_pred = knn.predict(X_test)
            accuracy = accuracy_score(y_test, y_pred)
            print(f"Accuracy for k={k}: {accuracy:.4f}")
            
            if accuracy > best_accuracy:
                best_accuracy = accuracy
                best_k = k

        # Output the best k and its corresponding accuracy
        print(f"The best k is {best_k} with a test accuracy of {best_accuracy:.4f}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()