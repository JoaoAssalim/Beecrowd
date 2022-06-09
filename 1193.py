for i in range(int(input())):
    num, base = map(str, input().split())
    print(f'Case {i+1}:')
    if base == 'bin':
        hexa = hex(int(num, 2))
        print(f'{int(num, 2)} dec')
        print(f'{hexa[2:]} hex')
    elif base == 'dec':
        hexa = hex(int(num))
        bina = bin(int(num))
        print(f'{hexa[2:]} hex')
        print(f'{bina[2:]} bin')
    elif base == 'hex':
        inta = int(num, base=16)
        bina = bin(int(inta))
        print(f'{inta} dec')
        print(f'{bina[2:]} bin')
    print()