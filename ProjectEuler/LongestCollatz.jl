
function main()
@everywhere function wrapCollatz(n)
    length = 0
    function collatz(n)
        length += 1
        if n == 1
            return 1
        end

        if n % 2 == 0

            return collatz(n/2)

        end

        return collatz(3n + 1)

    end

    collatz(n)

    return length 

end



maxLength = @parallel (max) for i = 1:500000
    
            wrapCollatz(2i + 1)

            
            end


println(maxLength)
end

@time(main())
