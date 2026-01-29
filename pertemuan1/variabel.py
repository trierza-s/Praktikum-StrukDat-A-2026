#membuat variabel
x = 5
y = "John"
print(x)
print(y)

#Variabel tidak perlu dideklarasikan dengan tipe tertentu,dan bahkan bisa berubah tipe setelah ditetapkan.
x = 4       # x ini tipe integer
x = "Sally" # x ini sekarang tipe string
print(x)

#Jika kita ingin menentukan tipe data dari sebuah variabel, hal ini bisa dilakukan dengan casting.
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

#kita bisa memperoleh tipe data dari sebuah variabel dengan fungsi type().
x = 5
y = "John"
print(type(x))
print(type(y))

#nama variabel hanya bisa seperti ini
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"