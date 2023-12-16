# julia matrices are column-major. this means you iterate over columns then rows
# the indexing is still the same as mathematics, A_1,2 == A[1][2] is still the element in the first row and second column
# vcat - dims = 1 : vertical concatenation along columns (adds rows)
# hcat - dims = 2 : horizontal concatenation along rows (adds columns)
# dims 1 = along cols, dims 2 = along rows, dims 3 = along depth, etc...
A = [
    9 8 7
    5 3 2
    6 6 7
]

max = [9 5 7]' # max of each row
min = [5 3 2]  # min of each col

# find the saddle points of a matrix
function saddlepoints(M)
    if isempty(M)
        return []
    end

    # find the indices of the minimum of each column
    col_min = findall(M .== minimum(M, dims=1))
    # find the indices of the maximum of each row
    row_max = findall(M .== maximum(M, dims=2))

    # find the intersection of the two sets
    return [(c[1], c[2]) for c in row_max ∩ col_min]
end





