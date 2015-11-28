
accum = 0

function evenFib(upper)
    scr = 0
    current = 1
    old = 0
    accum = 0
    while old < upper
        scr = current
        current += old
        old = scr
        if current % 2 == 0
            accum += current
        end
        

    end


    return accum

end

println(evenFib(4000000))