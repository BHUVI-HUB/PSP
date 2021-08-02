# To find NUmerical Aperture

import optical_fibre
D= float(input("Enter the value of D:"))
L = float(input("Enter the value of L:"))
NA =float(optical_fibre.Numerical_Aperture(D,L))

print("The Numerical Aperture is :%f" %(NA))
