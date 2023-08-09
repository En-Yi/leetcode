class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        to_fill = [[sr,sc]] # consist item to fill
        to_append = [] # item to append to to_fill
        row = len(image)
        col = len(image[0])
        raw = image[sr][sc]
        image[sr][sc] = color
        
        if raw == color:
            return image
        while len(to_fill) > 0:
            for i in to_fill:
                # fill 4-direction
                if (i[0]-1 >= 0) and (image[i[0]-1][i[1]] == raw):
                    image[i[0]-1][i[1]] = color
                    to_append.append([i[0]-1,i[1]])
                if (i[0]+1 < row) and (image[i[0]+1][i[1]] == raw):
                    image[i[0]+1][i[1]] = color
                    to_append.append([i[0]+1,i[1]])
                if (i[1]-1 >= 0) and (image[i[0]][i[1]-1] == raw):
                    image[i[0]][i[1]-1] = color
                    to_append.append([i[0],i[1]-1])      
                if (i[1]+1 < col) and (image[i[0]][i[1]+1] == raw):
                    image[i[0]][i[1]+1] = color
                    to_append.append([i[0],i[1]+1])
                
            to_fill = []
            to_fill.extend(to_append)
            to_append = []
        return image