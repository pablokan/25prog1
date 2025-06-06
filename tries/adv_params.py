# funciona pero no es recomendable porque dificulta la percepción del orden
def foo2(a, b, n1="ene uno", *args, **kwargs):
    print('foo2')
    print(a, b, args, n1, kwargs)
foo2(1, 2, 3, 4, 5, k='k')
