"""
Solution 1: Brute Force
Time: O(n * k)
Space: O(k)
"""


class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:

        while N:

            newCells = []

            N -= 1

            newCells.append(0)

            for i in range(1, 7):
                if cells[i - 1] == cells[i + 1]:
                    newCells.append(1)
                else:
                    newCells.append(0)

            newCells.append(0)

            cells = newCells

        return cells


"""
Solution 2: Cycle HashMap
Time: O(n * k)
Space: O(k)
"""


class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:

        seen = {}

        while N:

            newCells = []

            seen[str(cells)] = N
            N -= 1

            newCells.append(0)

            for i in range(1, 7):
                if cells[i - 1] == cells[i + 1]:
                    newCells.append(1)
                else:
                    newCells.append(0)

            newCells.append(0)

            cells = newCells

            if str(cells) in seen:
                N %= seen[str(cells)] - N

        return cells
