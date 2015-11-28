function fac(n)
    n = BigInt(n)
    if n == 1
        return 1
    end

    return n * fac(n-1)
end

fac100 = fac(100)

function sumDigits(number)
    # Takes a number and sums the digits

    str = string(number)
    accum = 0
    for i in 1:length(str)
        accum += parse(Int,str[i:i])
    end
    return accum
end

println(sumDigits(fac100))