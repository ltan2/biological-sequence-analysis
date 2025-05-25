def needleman_wunsch(seq1, seq2):
    m, n = len(seq1), len(seq2)
    gap = -2
    mismatch = -1
    match = 1

    matrix = [[0] * (n + 1) for _ in range(m + 1)] 

    # Fill in the first row and column
    # first elem is 0
    for i in range(1, m + 1):
        matrix[i][0] = matrix[i - 1][0] + gap
    for j in range(1, n + 1):
        matrix[0][j] = matrix[0][j - 1] + gap

    # Fill up matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            diag = matrix[i - 1][j - 1] + (match if seq1[i-1] == seq2[j-1] else mismatch)
            up = matrix[i - 1][j] + gap
            left = matrix[i][j - 1] + gap

            matrix[i][j] = max(diag, up, left)

    # traceback
    aligned_seq1 = ""
    aligned_seq2 = ""
    while i > 0 or j > 0:
        if i > 0 and j > 0 and matrix[i][j] == matrix[i - 1][j - 1] + (match if seq1[i - 1] == seq2[j - 1] else mismatch):
            aligned_seq1 = seq1[i - 1] + aligned_seq1
            aligned_seq2 = seq2[j - 1] + aligned_seq2
            i -= 1
            j -= 1
        elif i > 0 and matrix[i][j] == matrix[i - 1][j] + gap:
            aligned_seq1 = seq1[i - 1] + aligned_seq1
            aligned_seq2 = "-" + aligned_seq2
            i -= 1
        else:
            aligned_seq2 = seq2[j - 1] + aligned_seq2
            aligned_seq1 = "-" + aligned_seq1
            j -= 1

    return aligned_seq1, aligned_seq2, matrix[m][n]


seq1, seq2, score = needleman_wunsch("AAGC", "AGT")
print(seq1, seq2)
print(score)
