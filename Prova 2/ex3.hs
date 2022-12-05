a = [100,96..50]
multiply x = (x*x) -1
mappedFunction = map multiply a
d = reverse mappedFunction
main = do

    print(a)
    print(mappedFunction)
    print(d)