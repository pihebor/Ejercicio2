def distance(strand_a, strand_b):
    if len(strand_a) == len(strand_b):
        contador = 0
        print (" ")
        for x in range(0, len(strand_b)):
            if strand_a[x] != strand_b[x]:
                contador = contador+1
        return contador  
    else:
        raise ValueError("Value Error")