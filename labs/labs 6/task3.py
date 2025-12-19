def simple_number(start, end):
    simple_numbers = []
      
    def is_simple(num):
        if num <2:
                return False       
        for i in range(2, int(num**0.5)+1):
            if num%i == 0:
                return False
        return True
    
    for n in range(start, end + 1):
        if is_simple(n):
            simple_numbers.append(n)
    return simple_numbers
       
print(simple_number(1,100))


                

