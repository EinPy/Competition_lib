def precompute_factorials(max_n, mod):
    """ Precomputes factorials and modular inverses of factorials up to max_n under mod. """
    fact = [1] * (max_n + 1)
    ifact = [1] * (max_n + 1)
    for i in range(2, max_n + 1):
        fact[i] = fact[i - 1] * i % mod
    
    ifact[max_n] = pow(fact[max_n], mod - 2, mod)  # Using Fermat's little theorem for modular inverse
    for i in range(max_n - 1, 0, -1):
        ifact[i] = ifact[i + 1] * (i + 1) % mod
    
    return fact, ifact

def modular_combinations(n, k, fact, ifact, mod):
    """ Returns n choose k % mod using precomputed factorials and inverse factorials. """
    if k > n:
        return 0
    return fact[n] * ifact[k] % mod * ifact[n - k] % mod

# Constants
MOD = 1000000007
MAXN = 100000  # Depending on the problem statement, adjust this accordingly

# Precomputations
fact, ifact = precompute_factorials(MAXN, MOD)

# Input processing
input_list = [2, 2, 3, 4, 4, 5]  # Example input, replace with reading from stdin or other sources
k = 3

# Sort the list
input_list.sort()

# Compute the result
result_sum = 0
n = len(input_list)
for i in range(k - 1, n):
    count_combinations = modular_combinations(i, k - 1, fact, ifact, MOD)
    result_sum = (result_sum + count_combinations * input_list[i] % MOD) % MOD

# Output the result
print(result_sum)
