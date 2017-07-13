i	=	8
if(i%2):
	print	"odd number"
else:
	print "Even number"
	
#Since i is initialized to 8, and if 2 can go into 8 
#completely without any number left , then it print
# Even number , but if the number would go in and 
#get other number left for instant 3 into 8,
#definitely 2 will be left so, it would print Odd Number.

#1: % is modulo ,  i % 2 means 8 modulo 2.So 2 can go into 8
#completely and it will print out Even.

print"\n"


def is_even(i):
	return i%2==0
	
	nums=[1,2,3,4]
	
def sum_evens():
	nums=[1,2,3,4,16,18,19,14,20,10,8]
	
	sum=0+2+4+16+18+14+20+10+8
	goma="You are a google administrator"
	
	
	print nums
	print sum
	print goma
	
sum_evens()

print"\n"
def trustgoma():
	mylist=[1,2,3,4,5,6,7,8,9,10]
	i	=	0
	for trust in mylist:
		if not trust%2:
			i	=+trust
			
     print i
trustgoma() 
trustgoma()
