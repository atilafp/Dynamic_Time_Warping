import numpy as np


class DTW:
    def __init__(self, signal_1, signal_2):
        self.signal_1 = signal_1
        self.signal_2 = signal_2
        self.N = len(self.signal_1)
        self.M = len(self.signal_2)


    def d_matrix(self):
        N = self.N
        M = self.M
        D = np.zeros((N, M))

        for i in range(1,N):
            D[i,0] = np.inf
        for j in range(1,M):
            D[0,j] = np.inf

        for i in range(1,N):
            for j in range(1,M):
                distance = abs(self.signal_1[i] - self.signal_2[j])

                candidates = [D[i-1,j-1], D[i-1,j], D[i, j-1]]
                Dij_min = min(candidates)

                Dij = distance + Dij_min

                D[i,j] = Dij

        return D


if __name__ == '__main__':
    x = [1,1,1,3,5,2,3,1,2,1,1]
    y = [1,1,3,3,3,2,1,2,1]

    dtw = DTW(x, y)
    D = dtw.d_matrix()
    print(D)
