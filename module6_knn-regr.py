import numpy as np

class KNNRegression:
    def __init__(self, k):
        self.k = k
        self.points = np.empty((0, 2), float)
    
    def add_point(self, x, y):
        new_point = np.array([[x, y]])
        self.points = np.append(self.points, new_point, axis = 0)
    
    def predict(self, X):
        distances = np.abs(self.points[:, 0] - X)
        k_nearest_indices = np.argsort(distances)[:self.k]
        k_nearest_points = self.points[k_nearest_indices]
        return np.mean(k_nearest_points[:, 1])

def main():
    try:
        N = int(input("Enter the number of elements (N - positive integer): "))
        k = int(input("Enter the number of nearest neighbors (k <= " + str(N) + "): "))
        
        if k > N:
            print("Error: k cannot be greater than N.")
            return
        
        knn_regressor = KNNRegression(k)
        
        for i in range(N):
            x = float(input(f"Enter x value for point {i+1}: "))
            y = float(input(f"Enter y value for point {i+1}: "))
            knn_regressor.add_point(x, y)
        
        X = float(input("Enter the X value to predict Y: "))
        prediction = knn_regressor.predict(X)
        print(f"The predicted Y value for X = {X} is: {prediction}")
    
    except ValueError as e:
        print(f"Invalid input: {e}")

if __name__ == "__main__":
    main()
