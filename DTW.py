import numpy as np
import matplotlib.pyplot as plt


class DTW:
    def __init__(self, signal_1, signal_2):
        """
        Initialize the class DTW with signal_1 and signal_2
        """
        self.signal_1 = signal_1
        self.signal_2 = signal_2
        self.N = len(self.signal_1)
        self.M = len(self.signal_2)


    def d_matrix(self):
        """
        Construct D matrix with the cost of correlation for each pair of points in signal_1 and signal_2
        """
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

        D = np.delete(D, 0, 0)
        D = np.delete(D, 0, 1)

        return D
    
    def correlation(self):
        """
        map signal_1 to signal_2
        """
        N = self.N
        M = self.M

        D = self.d_matrix(self.signal_1, self.signal_2)

        map = np.zeros(M)

        map[-1] = M

        for i in range(N,0, -1):
            for j in range(M,0, -1):
                dij = D[i,j]

        #still have to finish this method

    
    def plot(self):
        pass



if __name__ == '__main__':
    x = [1,1,1,3,5,2,3,1,2,1,1]
    y = [1,1,3,3,3,2,1,2,1]


    dtw = DTW(x, y)
    D = dtw.d_matrix()
    print(D)
    plt.imshow(D)
    plt.show()