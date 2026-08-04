"""
=============================================================================
PROYECTO: Análisis Exploratorio de Datos (EDA) y Segmentación Comercial
AUTOR: Perfil Profesional en Análisis de Datos
DESCRIPCIÓN: Script completo de limpieza, transformación, análisis estadístico 
y generación de insights de negocio sobre un dataset de transacciones de retail.
=============================================================================
"""

import numpy as np
import pandas as pd

# =============================================================================
# 1. CARGA Y SIMULACIÓN DE DATOS (Simulando un entorno real de producción)
# =============================================================================
print(">[1/4] Cargando datos y generando entorno de análisis...")

np.random.seed(42)  # Para reproducibilidad de los datos aleatorios
n_filas = 1000

data = {
    'ID_Transaccion': range(5000, 5000 + n_filas),
    'Fecha': pd.date_range(start='2025-01-01', periods=n_filas, freq='h'),
    'Categoria': np.random.choice(
        ['Tecnología', 'Hogar', 'Indumentaria', 'Alimentos'], n_filas
    ),
    'Region': np.random.choice(['Norte', 'Sur', 'Este', 'Oeste'], n_filas),
    'Cantidad': np.random.randint(1, 5, n_filas),
    'Precio_Unitario': np.random.uniform(50, 1500, n_filas).round(2),
}

df = pd.DataFrame(data)

# Introducimos intencionalmente algunos valores nulos y duplicados (Realidad del Data Cleaning)
df.loc[10:15, 'Precio_Unitario'] = np.nan
df = pd.concat([df, df.iloc[0:5]], ignore_index=True)  # Duplicados intencionales

# =============================================================================
# 2. LIMPIEZA Y PREPARACIÓN DE DATOS (Data Cleaning)
# =============================================================================
print(">[2/4] Ejecutando procesos de Data Cleaning...")

# A. Conteo de nulos iniciales y tratamiento
nulos_antes = df.isnull().sum().sum()
# Imputamos los valores nulos con la mediana de la columna Precio_Unitario
mediana_precio = df['Precio_Unitario'].median()
df['Precio_Unitario'] = df['Precio_Unitario'].fillna(mediana_precio)

# B. Eliminación de registros duplicados
duplicados_antes = df.duplicated().sum()
df = df.drop_duplicates()

# C. Creación de Columnas Calculadas (Feature Engineering)
df['Ingreso_Total'] = (df['Cantidad'] * df['Precio_Unitario']).round(2)
# Simulamos costo estimado (60% del precio) para calcular margen
df['Costo_Total'] = (df['Ingreso_Total'] * 0.60).round(2)
df['Ganancia'] = (df['Ingreso_Total'] - df['Costo_Total']).round(2)
df['Margen_Pct'] = ((df['Ganancia'] / df['Ingreso_Total']) * 100).round(2)

print(f"   - Valores nulos tratados: {nulos_antes}")
print(f"   - Duplicados eliminados: {duplicados_antes}")
print(f"   - Dataset limpio resultante: {df.shape[0]} filas y {df.shape[1]} columnas.")

# =============================================================================
# 3. ANÁLISIS EXPLORATORIO Y MÉTRICAS DE NEGOCIO (KPIs)
# =============================================================================
print(">[3/4] Calculando KPIs y métricas clave...")

# Facturación total y ganancia neta global
facturacion_total = df['Ingreso_Total'].sum()
ganancia_total = df['Ganancia'].sum()

print(f"\n--- REPORTE EJECUTIVO ---")
print(f"Facturación Total Global: ${facturacion_total:,.2f}")
print(f"Ganancia Neta Global:     ${ganancia_total:,.2f}")

# Agrupamiento por Categoría
resumen_categoria = (
    df.groupby('Categoria')
    .agg(
        Total_Ventas=('Ingreso_Total', 'sum'),
        Promedio_Margen=('Margen_Pct', 'mean'),
        Transacciones=('ID_Transaccion', 'count'),
    )
    .reset_index()
    .sort_values(by='Total_Ventas', ascending=False)
)

print("\n--- Rendimiento por Categoría de Producto ---")
print(resumen_categoria.to_string(index=False))

# Agrupamiento por Región
resumen_region = (
    df.groupby('Region')['Ingreso_Total']
    .sum()
    .reset_index()
    .sort_values(by='Ingreso_Total', ascending=False)
)

print("\n--- Facturación por Región Geográfica ---")
print(resumen_region.to_string(index=False))

print(
    "\n>[4/4] Análisis completado con éxito. Generando recomendaciones de negocio..."
)
print("FIN DEL SCRIPT.")
