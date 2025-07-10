import numpy as np

def input_matrix(name):
    print(f"\nEnter dimensions for {name} (rows cols): ", end="")
    rows, cols = map(int, input().split())
    print(f"Enter the elements of {name} row by row, separated by spaces:")
    matrix = []
    for i in range(rows):
        row = list(map(float, input(f"Row {i+1}: ").split()))
        if len(row) != cols:
            print(f"Error: Expected {cols} values.")
            return None
        matrix.append(row)
    return np.array(matrix)

def print_matrix(mat, name="Result"):
    print(f"\n{name}:")
    print(mat)

def main():
    print("""
Matrix Operations Tool (NumPy)
-----------------------------
1. Addition
2. Subtraction
3. Multiplication
4. Transpose
5. Determinant
6. Exit
""")
    while True:
        choice = input("Select operation (1-6): ")
        if choice == '1':
            A = input_matrix("Matrix A")
            B = input_matrix("Matrix B")
            if A is not None and B is not None and A.shape == B.shape:
                print_matrix(A + B, "A + B")
            else:
                print("Error: Matrices must have the same dimensions.")
        elif choice == '2':
            A = input_matrix("Matrix A")
            B = input_matrix("Matrix B")
            if A is not None and B is not None and A.shape == B.shape:
                print_matrix(A - B, "A - B")
            else:
                print("Error: Matrices must have the same dimensions.")
        elif choice == '3':
            A = input_matrix("Matrix A")
            B = input_matrix("Matrix B")
            if A is not None and B is not None and A.shape[1] == B.shape[0]:
                print_matrix(np.dot(A, B), "A x B")
            else:
                print("Error: Number of columns of A must equal number of rows of B.")
        elif choice == '4':
            A = input_matrix("Matrix")
            if A is not None:
                print_matrix(A.T, "Transpose")
        elif choice == '5':
            A = input_matrix("Matrix (square)")
            if A is not None and A.shape[0] == A.shape[1]:
                print(f"\nDeterminant: {np.linalg.det(A):.2f}")
            else:
                print("Error: Matrix must be square.")
        elif choice == '6':
            print("Exiting.")
            break
        else:
            print("Invalid choice. Please select 1-6.")

if __name__ == "__main__":
    main() 