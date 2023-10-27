class Solution(object):
    def updateMatrix(self, mat):
        r = len(mat)
        c = len(mat[0])
        out = mat
        for i in range(r):
            for j in range(c):
                if mat[i][j]:
                    if (i != 0 and mat [i-1][j] == 0) or (i != r-1 and mat [i+1][j] == 0):
                        break
                    if (j != 0 and mat [i][j-1] == 0) or (j != c-1 and mat [i][j+1] == 0):
                        break
                    d = r+c-2
                    for k in range(r):
                        left = i - k
                        right = i + k
                        # if j==6:
                        #     print(left,right)
                        if k >= d:
                            break
                        for l in range(c):
                            a = d
                            a1 = a
                            a2 = (j-l) if (j-l) > 0 else -(j-l)
                            # print(left,right)
                            if (left >= 0 and not mat[left][l]):
                                a1 = (i - left)
                                a1 = a1 if a1 > 0 else -a1
                                # print(a1,i,left,a2)
                                a = a1 + a2
                                d = a if a < d else d
                                # print(left,l,i,j)

                            if (right < r and not mat[right][l]):
                                a1 = (i - right)
                                a1 = a1 if a1 > 0 else -a1
                                a = a1 + a2
                                # if j==6:
                                #     print(right,l)
                                d = a if a < d else d
                            # print(a, d)
                    out[i][j] = d
        return out
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
print(Solution.updateMatrix(1,[[1],[1],[1],[1],[1],[0],[1],[0],[0],[1],[1],[0],[1],[1],[1],[1],[1],[0],[0],[0],[0],[0],[1],[0],[0],[1],[0],[0]]))
