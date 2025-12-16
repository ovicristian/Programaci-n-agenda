# Instrucciones de uso para la Agenda de Rueda de Negocios

## Descripción del programa

Este programa organiza automáticamente una rueda de negocios con las siguientes características:

- **25 vendedores** y **10 compradores**
- **Horario**: 10:15 AM - 1:00 PM (2 horas 45 minutos)
- **Duración de cada cita**: 15 minutos
- **Formato de citas**: 4 vendedores se reúnen con 1 comprador por cita
- **Máximo 4 citas por vendedor**
- **NUEVO**: Cada vendedor puede tener múltiples compradores preferidos

## Cómo usar el archivo de preferencias

### Paso 1: Preparar el archivo de preferencias

1. Abre el archivo `ejemplo_preferencias.csv` que se generó automáticamente
2. Edítalo con los nombres reales de tus vendedores y compradores
3. **IMPORTANTE**: Cada vendedor puede aparecer en múltiples filas con diferentes compradores
4. Guárdalo como `preferencias_multiples.csv` o `preferencias_citas.csv` en la misma carpeta

### Formato del archivo CSV (NUEVO):

```
Nombre_Vendedor,Comprador_Preferido
Juan Pérez,Empresa ABC
Juan Pérez,Empresa XYZ      ← Mismo vendedor, otro comprador preferido
Juan Pérez,Empresa 123      ← Mismo vendedor, otro comprador preferido
María González,Empresa ABC
María González,Empresa DEF
```

### Paso 2: Ejecutar el programa

1. Ejecuta: `python agenda_rueda_negocios.py`
2. El programa automáticamente:
   - Carga las preferencias del archivo (múltiples por vendedor)
   - Agrupa a los vendedores que quieren reunirse con el mismo comprador
   - Crea citas de 4 vendedores + 1 comprador
   - Intenta cumplir el máximo número de preferencias posibles
   - Llena los slots restantes con citas adicionales

## Archivos generados

1. **agenda_rueda_negocios.csv**: Agenda completa en formato tabla
2. **resumen_vendedores.csv**: Resumen individual por vendedor con **contador de preferencias cumplidas**
3. **agenda_completa.json**: Datos completos en formato JSON
4. **ejemplo_preferencias.csv**: Plantilla para tus preferencias (formato nuevo)
5. **INSTRUCCIONES.md**: Esta guía de uso

## Características del algoritmo (MEJORADO)

- ✅ **NUEVO**: Maneja múltiples compradores por vendedor
- ✅ Respeta las preferencias de citas especificadas
- ✅ Agrupa automáticamente vendedores que quieren el mismo comprador
- ✅ **NUEVO**: Cuenta y reporta preferencias cumplidas individualmente
- ✅ Distribuye equitativamente las citas entre todos los participantes
- ✅ Maximiza el uso del tiempo disponible
- ✅ Respeta el límite de 4 citas por vendedor

## Ejemplo de uso (NUEVO FORMATO)

Si un vendedor quiere reunirse con múltiples empresas:

```
Vendedor_A,Empresa_1
Vendedor_A,Empresa_2    ← Mismo vendedor, otra empresa
Vendedor_A,Empresa_3    ← Mismo vendedor, otra empresa
Vendedor_B,Empresa_1
Vendedor_C,Empresa_1
Vendedor_D,Empresa_1
```

El programa automáticamente:

1. Creará: `Empresa_1 ↔ [Vendedor_A, Vendedor_B, Vendedor_C, Vendedor_D]`
2. Buscará otras oportunidades para que Vendedor_A se reúna con Empresa_2 y Empresa_3
3. Reportará cuántas preferencias se cumplieron por vendedor (ej: "3/3" si se cumplieron las 3)

## Beneficios del nuevo sistema

- 🎯 **Mayor flexibilidad**: Los vendedores pueden expresar múltiples intereses
- 📊 **Mejor seguimiento**: Cada vendedor ve exactamente cuántas de sus preferencias se cumplieron
- 🔄 **Optimización inteligente**: El algoritmo maximiza el número total de preferencias cumplidas
- 📈 **Mejor utilización**: Aproveha mejor las oportunidades de conexión
