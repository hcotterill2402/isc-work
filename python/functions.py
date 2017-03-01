#playing around with functions

#1

def double_it(number): #a function to double a number
    return number*2

print double_it(2)
print double_it(3.5)
print double_it('two')

#2

def calc_hypo(a,b):
    if type(a) not in (int, float) or type(b) not in (int,float):
        print "Bad arguements"
        return False
    if a <= 0 or b <= 0:
        print "Bad arguements: inputs must be positive"
        return False
    else:
        hypo=(a**2 + b**2)**(0.5)
        return hypo

print calc_hypo(89,78)



