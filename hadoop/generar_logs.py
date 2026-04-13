# -*- coding: utf-8 -*-
import sys
import random
from faker import Faker

fake = Faker()

CATEGORIAS = ['Electronica', 'Ropa', 'Hogar', 'Juguetes', 'Deportes']
NUM_REGISTROS = 500000 

print(f"Generando {NUM_REGISTROS} registros...")

counts = {c: 0 for c in CATEGORIAS}

with open('ventas_gigantes.csv', 'w', encoding='utf-8') as f:
    f.write("id,producto,categoria,monto,pais\n")
    for i in range(NUM_REGISTROS):
        cat = random.choice(CATEGORIAS)
        counts[cat] += 1
        monto = round(random.uniform(10.0, 500.0), 2)
        f.write(f"{i},{fake.word()},{cat},{monto},{fake.country()}\n")

with open('control_counts.txt', 'w', encoding='utf-8') as f:
    f.write("=== CONTADORES LOCALES SECRETOS ===\n")
    for cat, count in counts.items():
        f.write(f"{cat}: {count}\n")

print("Generación terminada (revisa archivos locales).")