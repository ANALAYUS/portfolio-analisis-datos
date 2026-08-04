-- =====================================================
-- PROYECTO: Auditoría de Clientes y Transacciones
-- HERRAMIENTA: SQL Server / PostgreSQL
-- DESCRIPCIÓN: Consultas orientadas a la segmentación de 
-- clientes y análisis de comportamiento de pagos.
-- =====================================================

-- 1. Vista general uniendo Clientes y Transacciones
SELECT 
    c.ID_Cliente,
    c.Nombre AS Cliente,
    c.Ciudad,
    t.ID_Transaccion,
    t.Monto,
    t.Fecha
FROM clientes c
INNER JOIN transacciones t ON c.ID_Cliente = t.ID_Cliente;

-- 2. Identificar clientes VIP que superan el promedio general de compras
SELECT 
    c.Nombre,
    COUNT(t.ID_Transaccion) AS Total_Compras,
    SUM(t.Monto) AS Monto_Total_Gastado
FROM clientes c
INNER JOIN transacciones t ON c.ID_Cliente = t.ID_Cliente
GROUP BY c.Nombre
HAVING SUM(t.Monto) > (SELECT AVG(Monto) FROM transacciones)
ORDER BY Monto_Total_Gastado DESC;
