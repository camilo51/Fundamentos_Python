ventas_por_region = {
    "Norte": {
        "Q1": 12000,
        "Q2": 15000,
        "Q3": 14000,
        "Q4": 16000
    },
    "Sur": {
        "Q1": 10000,
        "Q2": 11000,
        "Q3": 13000,
        "Q4": 12000
    },
    "Centro": {
        "Q1": 18000,
        "Q2": 17000,
        "Q3": 19000,
        "Q4": 20000
    }
}

total_por_region = {}

for region, ventas in ventas_por_region.items():
    total_por_region[region] = sum(ventas.values())

print(f"Total por región: {total_por_region}")

region_mayor = max(total_por_region, key=lambda region: total_por_region[region])

print(f"Región con mayores ventas: {region_mayor}")

ventas_trimestre = {
    "Q1": 0,
    "Q2": 0,
    "Q3": 0,
    "Q4": 0
}

for ventas in ventas_por_region.values():
    for trimestre, valor in ventas.items():
        ventas_trimestre[trimestre] += valor

print(f"Ventas por trimestre: {ventas_trimestre}")

gran_total = sum(total_por_region.values())

porcentajes = {
    region: round(total / gran_total * 100, 2)
    for region, total in total_por_region.items()
}

print(f"Porcentajes: {porcentajes}")

print("\nReporte de ventas")

for region, total in sorted(
    total_por_region.items(),
    key=lambda elemento: elemento[1],
    reverse=True
):
    print(f"{region}: ${total} ({porcentajes[region]}%)")