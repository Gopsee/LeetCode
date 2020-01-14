class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        triangle = []
        
        for y in range(rowIndex+1):
            row = [None for _ in range(y+1)]
            row[0], row[-1] = 1, 1
            
            for x in range(1, len(row)-1):
                row [x] = triangle[y-1][x-1] + triangle[y-1][x]
                
            triangle.append(row)
                
        return triangle[rowIndex]
        