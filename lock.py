from sys import argv

N, a, b , c = int(argv[1]), int(argv[2]), int(argv[3]), int(argv[4])
print ((N * 3) + a + (a - b) % N + (c - b) % N)