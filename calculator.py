d1 = float(input("D1 = "))
d2 = float(input("D2 = "))
d3 = float(input("D3 = "))

c1 = float(input("C1 = "))
c2 = float(input("C2 = "))
c3 = float(input("C3 = "))

dt1 = ((1-d1)*((30*24)))
dt2 = ((1-d2)*((30*24)))
dt3 = ((1-d3)*((30*24)))

print(dt1, dt2, dt3)

# c ** 2 = a ** 2 + b ** 2
h1 = pow(((c1 ** 2) + (d1 ** 2)), 1/2)
h2 = pow(((c2 ** 2) + (d2 ** 2)), 1/2)
h3 = pow(((c3 ** 2) + (d3 ** 2)), 1/2)

print(h1, h2, h3)

