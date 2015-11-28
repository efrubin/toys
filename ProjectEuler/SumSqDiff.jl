
N = 100
sumSq = sum([i^2 for i = 1:N])
sqSum = ((N)*(N+1)/2)^2

println(round(Int64,(sqSum - sumSq)))