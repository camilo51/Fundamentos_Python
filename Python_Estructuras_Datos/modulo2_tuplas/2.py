ubicaciones = {
    (40.7128, -74.0060): "Nueva York",
    (34.0522, -118.2437): "Los Ángeles"
}

print(f"Ubicación: {ubicaciones[(40.7128, -74.0060)]}")

try:
    d = {[40.71, -74.00]: "NY"}
except TypeError as e:
    print(f"Error: {e}")