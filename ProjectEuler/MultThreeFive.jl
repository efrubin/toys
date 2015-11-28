# Find the sum of all multiples of 3 or 5 between 1 and 1000

start = time()

a = 0
for i = 1:1e9
    if i % 5 == 0 || i % 3 == 0
        a += i
    end
end

finish = time()
println("$a in $(finish - start)")