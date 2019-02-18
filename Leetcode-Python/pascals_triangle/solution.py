class Solution:
    def generate(self, numRows):

        if not numRows or numRows == 0:
            return []

        tri = [[1]]

        for i in range(1, numRows):
            prev_row = tri[i - 1]
            row = [1]

            for j in range(1, i):
                row[j].append(prev_row[j] + prev_row[j - 1])

            row.append(1)
            tri.append(row)

        return tri