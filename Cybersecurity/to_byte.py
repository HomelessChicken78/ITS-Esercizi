n=3512

# with open("numero1.dat", "wb") as f:
#     f.write(n.to_bytes(4, byteorder="little"))

# with open("numero2.dat", "wb") as f:
#     f.write(n.to_bytes(4, byteorder="big"))

# xxd numero1.dat
# xxd numero2.dat

s="Ciao"
with open("numero3.dat", "w") as f:
    f.write(s)