def edit_distance(str1, str2):
    a = len(str1)
    b = len(str2)
    string_matrix = [[0 for i in range(b+1)] for i in range(a+1)]

    for i in range(a+1):
        for j in range(b+1):

            if i == 0:
                string_matrix[i][j] = j   

            elif j == 0:
                string_matrix[i][j] = i   

            elif str1[i-1] == str2[j-1]:
                string_matrix[i][j] = string_matrix[i-1][j-1]  

            else:
                string_matrix[i][j] = 1 + min(string_matrix[i][j-1],  string_matrix[i-1][j], string_matrix[i-1][j-1])    

    return string_matrix[a][b]
    

if __name__ == "__main__":
    print(edit_distance(input(), input()))
