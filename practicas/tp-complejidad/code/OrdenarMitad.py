

def OrdenarMitad(A:list):
	Asorted=[]
	Asorted=A.copy()
	Asorted.sort()
	mid=round((len(Asorted)-1)/2)
	quad=round((mid)/2)
	for i in range(1,mid-quad+1):
		Asorted[mid-i], Asorted[mid+i] = Asorted[mid+i], Asorted[mid-i]
	return Asorted



""" a = [2,5,3,6,7,8,56,4,1]

a = OrdenarMitad(a)

print(a) """