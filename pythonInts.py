from sayFullName import sayFullName as sn
from sayFullName import commaNumber as cn

'''This is intended to print the largest possible int for each length int list from 1 to MAX_LEN
'''

MAX_LEN = 10

def main(mode = ''):
    if mode not in ('','C','W','P'):
        print(f"Mode: {mode} is not an accepted mode\nAccepted modes are '' (for default), 'C', 'M', and 'P'")
        return
    for power in range(10):
        if mode == '':
            print(f"int list of length {power+1}, {['int '+str(power-significance) for significance in range(power + 1)]}, has MAX_INT: {2**(30*(power+1))-1}")
        elif mode == 'C':
            print(f"int list of length {power+1}, {['int '+str(power-significance) for significance in range(power + 1)]}, has MAX_INT: {cn(2**(30*(power+1))-1)}")
        elif mode == 'W':
            print(f"int list of length {power+1}, {['int '+str(power-significance) for significance in range(power + 1)]}, has MAX_INT: {sn(2**(30*(power+1))-1)}")
        elif mode == 'P':
            print(f"int list of length {power+1}, {['int '+str(power-significance) for significance in range(power + 1)]}, has MAX_INT:  2^{30*(power+1)} - 1")

# Example Usage:
# main()
# main('C')
# main('W')
# main('P')


