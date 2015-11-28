#SumThree.jl - Takes 3 integer values from command line and prints them
# as well as their sum

a = ones(Int64, 3)

for i = 1:3
    a[i] = parse(Int64, ARGS[i])
    print("$(a[i]) ")

end

println("$(a[1] + a[2] + a[3])")