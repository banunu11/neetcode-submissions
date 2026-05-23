class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check vert
            for j in range(len(board)):
                nums = set()
                for i in range(len(board[j])):
                    if board[i][j] in nums and board[i][j] != ".":
                        return False
                    else:
                        nums.add(board[i][j])
                    # print(board[i][j], nums)


        # check box
            for box in range(9):
                nums = set()
                for i in range(3):
                    for j in range(3):
                        row = (box//3) * 3 + i
                        col = (box % 3) * 3 + j
                        if board[row][col] in nums and board[row][col] != ".":
                            return False
                        else:
                            nums.add(board[row][col])

        # check hor
            for i in range(len(board)):
                nums = set()
                for j in range(len(board[i])):
                    if board[i][j] in nums and board[i][j] != ".":
                        return False
                    else:
                        nums.add(board[i][j])
                    # print(board[i][j], nums)
            return True


