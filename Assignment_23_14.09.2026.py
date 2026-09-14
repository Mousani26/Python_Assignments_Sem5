'''
Define two matrices (A,B) of order 3 x 3 using numpy. Perform the following operations of the following matrices :
1. Find out inverse of matrix A.
2. Find out the determinant of matrix A.
3. Print the result of (A. A ^ -1)
'''
import numpy as np

A = np.array([[1,2,3],
             [0,1,4],
             [5,6,0]]
             )

B = np.array([[2, 1, 3],
              [1, 0, 2],
              [4, 1, 1]])

A_inverse = np.linalg.inv(A)
print("Inverse of matrix A :")
print(A_inverse)

A_det = np.linalg.det(A)
print("Determinant of A :")
print(A_det)

result = np.dot(A, A_inverse)
print ("A * A^- 1 : \n")
print(result)
