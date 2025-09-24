from rendering import *

sep = "\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n"

q1: Quadrato = Quadrato(4)
q1.render()
print(f"L'area di questo quadrato vale: {q1.getArea()}")

print(sep)

q2: Quadrato = Quadrato(8)
q2.render()
print(f"L'area di questo quadrato vale: {q2.getArea()}")

print(sep)

r1: Rettangolo = Rettangolo(8, 4)
r1.render()
print(f"L'area di questo rettangolo vale: {r1.getArea()}")

print(sep)

r2: Rettangolo = Rettangolo(5, 9)
r2.render()
print(f"L'area di questo rettangolo vale: {r2.getArea()}")

print(sep)

t1: Triangolo = Triangolo(4)
t1.render()
print(f"L'area di questo triangolo vale: {t1.getArea()}")

print(sep)

t2: Triangolo = Triangolo(8)
t2.render()
print(f"L'area di questo triangolo vale: {t2.getArea()}")