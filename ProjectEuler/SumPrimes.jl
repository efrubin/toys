#Find the sum of all primes less than two million
N = 20
sieve = trues(N)

for i = 2:round(Int,sqrt(N))
    if sieve[i] == true
        sieve  = sieve[(i^2 + n*i) < N for n=0:N]    
        end
    end
end

println(sieve)