function fat (n)
      if n == 0 then
        return 1
      else
        return n * fat(n-1)
      end
    end
    
    print("Entre com um numero:")
    a = io.read()
    print(fat(a))