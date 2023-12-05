print('@@@ @  @@@ @@@@   @   @ @ @@@@@@     @@@')
print('@ @ @ @  @ @   @  @   @ @ @     @   @   @')
print("@ @ @ @@@@ @  @   @@@@@ @ @@@@@@    @@@@@")
print("@ @@@ @  @ @@     @   @ @ @    @    @   @")

def hitung(liststring):
    count = 0
    for string in liststring:
        if len(string) >= 2 and string[0] == string[-1]:
            count += 1
            print(f"-{string}")
    return count


my_list = ['xyx', 'cac', 'z', 'duit', 'test']
print(my_list)
result = hitung(my_list)

print(f"terdapat {result} yang memenuhi syarat")
