from module5_mod import InputNum
def main():
    numberInput = InputNum()
    # Read N from the user
    N = int(input("Enter the number of elements (N - positive integer): "))
    
    # List to store the N numbers
    numbers = []
    
    # Reading N numbers from the user
    for i in range(1, N + 1):
        num = int(input(f"Enter number {i}: "))
        numberInput.add_number(num)
    
    # Read X from the user
    X = int(input("Enter the number (X) to search for: "))
    
    # Search for X in the list and output the index or -1 if not found
    index = numberInput.find_index(X) # index from 1-N
    print(index)


if __name__ == "__main__":
    main()
