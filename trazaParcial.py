#Autor: Jesus Rodriguez

def getBases(num_sitios, pos_bases):
    '''
    Funcion para obtener las bases donde se traceara parcialmente
    
    Parameters
    ----------
    num_sitios: int
        Numero de sitios en el lattice
    pos_bases: array[1D]
        posicion (indice) de las bases
    '''
    b = []
    for i in range(0, pow(2, num_sitios)):
        b_row = []
        for j, v in enumerate(f"{i:b}".zfill(5)):
            if j in pos_bases:
                b_row.append(v)
            else:
                b_row.append("-")
        b.append(str().join(b_row))
    return b

def compareBases(b1, b2, pos_bases):
    '''
    Funcion para comparar las bases con las que se traceara parcialmente
    
    Parameters
    ----------
    b1: str
        Base 1
    b1: str
        Base 2
    pos_bases: array[1D]
        posicion (indices) de las bases
    '''
    count = 0
    for i in pos_bases:
        if b1[i] == b2[i]:
            count += 1    
    return True if count == len(pos_bases) else False

def compareAntibase(b1, b2, sitios):
    '''
    Funcion para comparar la parte que no es base con la que se traceara parcialmente
    
    Parameters
    ----------
    b1: str
        Base 1
    b1: str
        Base 2
    pos_bases: array[1D]
        posicion (indices) de las bases
    '''
    count = 0
    for i in sitios:
        if b1[i-1] == b2[i-1]:
            count += 1
    return True if count == len(sitios) else False
    
def parcialTrace(m, num_sitios, *sitios):
    '''
    Funcion para realizar traza parcial y generar matriz de densidad reducida
    
    Parameters
    ----------
    m: array[N][N]
        Matriz de densidad
    num_sitios: int
        Numero de sitios en el lattice
    sitios: *int 
        sitios sobre los cuales se hara la traza parcial
    '''
    mr = []
    num_bases = num_sitios - len(sitios)
    pos_bases = []
    for j in range(0, num_sitios):
        if j+1 not in sitios:
            pos_bases.append(j)
    
    bases = [f"{i:b}".zfill(num_bases) for i in range(0, pow(2,num_bases))]
    #bases = getBases(num_sitios, pos_bases)
    od = OrderedDict((i, OrderedDict((j, 0) for j in bases)) for i in bases)
    for i, f in od.items():
        mr_row = []
        for j, v in f.items():
            suma = 0
            for k, f in enumerate(m):
                for l, v in enumerate(f):
                    base_row_m = f"{k:b}".zfill(num_sitios)
                    base_col_m = f"{l:b}".zfill(num_sitios)
                    if compareBases(base_row_m, i, pos_bases) and compareBases(base_col_m, j, pos_bases):
                        if compareAntibase(base_row_m, base_col_m, sitios):
                            suma += v                    
            mr_row.append(suma)
        mr.append(mr_row)
    return np.array(mr)
