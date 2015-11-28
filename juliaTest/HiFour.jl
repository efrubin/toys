# HiFour.jl - a program to take N command line arguments and return a
# sentence greeting them in reverse order.

N = length(ARGS)
str = "Hi"
for i = 0:N-2
    str = "$str $(ARGS[N-i])," 
end
str = "$str and $(ARGS[1])."
println(str)
