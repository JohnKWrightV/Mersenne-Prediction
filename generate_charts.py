import matplotlib.pyplot as plt

# Data for Ranking of Mersenne Primes against n Values
ranks = list(range(9, 53))
n_values = [4.0000000, 6.4450000, 7.6400000, 8.7850000, 21.4200000, 23.2950000, 34.6800000, 46.0000000,
            46.8350000, 55.8650000, 64.4050000, 65.6900000, 97.7250000, 99.0000000, 105.2050000,
            140.5850000, 146.6750000, 151.7050000, 210.3450000, 293.1054000, 331.7923000, 362.8659000,
            464.3125000, 869.5234175, 926.1978810, 1121.2158930, 1181.6680105, 1724.1136085, 1737.7305070,
            2639.0964910, 3667.5247980, 4581.9129485, 4902.2020145, 5095.0750125, 5512.8849420, 5707.6126240,
            6094.7110000, 6528.6330000, 6563.4175000, 7607.5570000, 8614.3052960, 8785.0148940, 9087.1337100,
            11673.6300000]
plt.figure(figsize=(10, 6))
plt.scatter(ranks, n_values, color='blue')
plt.plot(ranks, [283.87895421 * r - 3431.35587902 for r in ranks], color='red', linestyle='--', label='Fit: y = 283.88x - 3431.36')
plt.xlabel('Rank')
plt.ylabel('n Value')
plt.title('Ranking of Mersenne Primes (9 to 52) against n Values')
plt.legend()
plt.savefig('ranking_n_values.png')
plt.close()

# Data for Comparison between C(n) n Values and Mersenne Exponents
exponents = [61, 89, 107, 127, 521, 607, 1279, 2203, 2281, 3217, 4253, 4423, 9689, 9941, 11213, 19937,
             21701, 23209, 44497, 86243, 110503, 132049, 216091, 756839, 859433, 1257787, 1398269, 2976211,
             3021377, 6972593, 13466917, 20996011, 24036583, 25964951, 30402457, 32582657, 37156667, 42643801,
             43112609, 57885161, 74207281, 77232917, 82589933, 136279841]
plt.figure(figsize=(10, 6))
plt.scatter(n_values, exponents, color='green')
plt.plot(n_values, [283.87895421 * n - 3431.35587902 for n in n_values], color='orange', linestyle='--', label='Fit: y = 283.88x - 3431.36')
plt.xlabel('n Value')
plt.ylabel('Mersenne Exponent')
plt.title('Comparison between C(n) n Values and Mersenne Exponents (9 to 52)')
plt.legend()
plt.savefig('comparison_c_n_mersenne.png')
plt.close()