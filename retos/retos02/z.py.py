def foo(*args):
    print(args)
    print(*args)
    a, b, *_, d = args
    print(a, b, d)
foo(1, 2, 3, 4, 5, 6, 7, 8)