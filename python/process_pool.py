import multiprocessing

# Funcția care calculează pătratul unui număr
def function_square(data):
    result = data * data
    return result

# Punctul de intrare al programului
if __name__ == '__main__':
    # Creăm o listă de numere de la 0 la 99
    inputs = list(range(0, 100))

    # Creăm un pool cu 4 procese
    pool = multiprocessing.Pool(processes=4)

    # Mapăm funcția 'function_square' pe lista de intrări
    pool_outputs = pool.map(function_square, inputs)

    # Închidem pool-ul și așteptăm finalizarea tuturor proceselor
    pool.close()
    pool.join()

    # Afișăm rezultatele
    print('Pool :', pool_outputs)
