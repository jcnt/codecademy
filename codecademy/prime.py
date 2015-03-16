def is_prime(x):
    if x < 2:
        return False
    if x == 2:
        return True
    for i in range(2, x-1):
        if x % i == 0:
            print "False"
	    break
    else:
        print "True"

is_prime(int(raw_input("enter a number: ")))


