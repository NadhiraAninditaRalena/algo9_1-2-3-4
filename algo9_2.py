print('@@@ @  @@@ @@@@   @   @ @ @@@@@@     @@@')
print('@ @ @ @  @ @   @  @   @ @ @     @   @   @')
print("@ @ @ @@@@ @  @   @@@@@ @ @@@@@@    @@@@@")
print("@ @@@ @  @ @@     @   @ @ @    @    @   @")

def calculate_averages(nested_tuple):
    # Menggunakan list comprehension untuk menghitung rata-rata
    averages = [sum(tup) / len(tup) if tup else 0 for tup in nested_tuple]
    return averages

# berisi beberapa tuple
sample_tuple = ((5, 37, 44), (40, 50, 78), (45, 81, 20))

# Menghitung rata-rata tuple
result_averages = calculate_averages(sample_tuple)

print(sample_tuple)
print("Rata-rata setiap tuple:")
print(result_averages)

