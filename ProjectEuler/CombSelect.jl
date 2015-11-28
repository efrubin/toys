

function fastFac(n)
    fac = BigInt(1)
    for i = 1:n
        fac *= i
    end

    return fac

end

function choose(n,k)
    top = fastFac(n)
    bottom = fastFac(k) * fastFac(n-k)
    return top/bottom
end

accum = 0
for i = 1:100
    for j = 1:100
        if choose(i,j) >= 1000000
            accum += 1
        end
    end
end

println(accum)

#println(choose(10,10))