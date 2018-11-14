s = str(input("Enter a string: "))
n = int(input("Enter a number: "))
l = len(s)

#Right rotation
a = s[:n]
b = s[n:]
res_r = b+a

#Left Rotation
a = s[:l-n]
b = s[l-n:]
res_l = b + a

print("Right (clockwise) rotation: ", res_r)
print("Left (anticlockwise) rotation: ", res_l)
