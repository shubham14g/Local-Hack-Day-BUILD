#random number generating script without direct use of random function

print(set(map(str,range(int(input('Enter the lower bound: ')),int(input('Enter the higher bound: '))+1))).pop())
