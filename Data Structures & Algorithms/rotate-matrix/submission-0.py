import numpy as np
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        matrix[:]=np.rot90(np.asarray(matrix),-1).tolist()