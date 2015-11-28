# computes in parallel the sum of all multiples of 3 or 5 between the bounds

start = time()

@everywhere function pf(i)
    
    if i % 3 == 0 || i % 5 == 0
        return i
    end 

    return 0
end

accum = @parallel (+) for i = 1:1e9
    pf(i)
end

finish = time()
println("$accum in $(finish - start)")