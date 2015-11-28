start = time()
N = Float64(1e10)
@everywhere function oneGame()
    S = 0
    p1num = 0
    p2num = 0
    while S < 1
        p1num = rand(1,1)[1]
        S += p1num
        p2num = rand(1,1)[1]
        S += p2num
    end
    if p2num > p1num
        return 1
    end

    return 0
end

accum= @parallel (+) for i=1:N
    oneGame()
 
end

finish = time()

println(accum/N)
println(finish-start)