#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
VERIFICADOR EXHAUSTIVO DE AGENDA
================================

Este script verifica meticulosamente que cada cita programada
corresponda exactamente a las preferencias solicitadas.

Autor: Sistema de Agenda
Fecha: 2024
"""

import json
import csv
from collections import defaultdict
import sys

def cargar_preferencias_desde_archivo(archivo_csv):
    """
    Carga las preferencias desde el archivo CSV de manera exhaustiva
    """
    preferencias = {}  # vendedor -> set de compradores solicitados
    
    print(f"📋 Cargando preferencias desde: {archivo_csv}")
    
    try:
        with open(archivo_csv, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            
            for row_num, row in enumerate(reader, start=2):  # Start at 2 because row 1 is header
                # Intentar diferentes nombres de columnas o usar las primeras dos columnas
                keys = list(row.keys())
                if len(keys) >= 2:
                    vendedor = row.get('Vendedor', row.get('Nombre_Vendedor', row.get(keys[0], ''))).strip()
                    comprador = row.get('Comprador', row.get('Comprador_Preferido', row.get(keys[1], ''))).strip()
                else:
                    vendedor = comprador = ''
                
                if not vendedor or not comprador:
                    # Solo reportar las primeras 5 líneas vacías para no saturar el log
                    if row_num <= 6:
                        print(f"⚠️  Fila {row_num}: Datos vacíos - saltando")
                    continue
                
                if vendedor not in preferencias:
                    preferencias[vendedor] = set()
                
                preferencias[vendedor].add(comprador)
                print(f"✓ Preferencia cargada: {vendedor} → {comprador}")
        
        print(f"\n📊 RESUMEN DE PREFERENCIAS CARGADAS:")
        print(f"   • Total vendedores: {len(preferencias)}")
        total_preferencias = sum(len(comps) for comps in preferencias.values())
        print(f"   • Total preferencias: {total_preferencias}")
        
        return preferencias
        
    except FileNotFoundError:
        print(f"❌ ERROR: No se encontró el archivo {archivo_csv}")
        return {}
    except Exception as e:
        print(f"❌ ERROR al leer el archivo: {e}")
        return {}

def cargar_agenda_generada(archivo_json):
    """
    Carga la agenda generada desde el archivo JSON
    """
    print(f"\n📋 Cargando agenda desde: {archivo_json}")
    
    try:
        with open(archivo_json, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        agenda = data.get('agenda', {})
        print(f"✓ Agenda cargada: {len(agenda)} slots de tiempo")
        
        return agenda
        
    except FileNotFoundError:
        print(f"❌ ERROR: No se encontró el archivo {archivo_json}")
        return {}
    except Exception as e:
        print(f"❌ ERROR al leer el archivo: {e}")
        return {}

def extraer_todas_las_citas(agenda):
    """
    Extrae todas las citas de la agenda en formato lista
    """
    todas_las_citas = []
    
    for horario, citas in agenda.items():
        for cita in citas:
            comprador = cita.get('comprador')
            vendedores = cita.get('vendedores', [])
            
            # Crear una cita individual para cada vendedor
            for vendedor in vendedores:
                todas_las_citas.append({
                    'horario': horario,
                    'comprador': comprador,
                    'vendedor': vendedor,
                    'tipo': 'individual'
                })
    
    return todas_las_citas

def verificar_citas_vs_preferencias(preferencias, todas_las_citas):
    """
    Verifica exhaustivamente cada cita contra las preferencias
    """
    print(f"\n🔍 INICIANDO VERIFICACIÓN EXHAUSTIVA")
    print("=" * 80)
    
    citas_correctas = []
    citas_incorrectas = []
    vendedores_sin_preferencias = set()
    compradores_encontrados = set()
    
    # Contadores para estadísticas
    total_citas = len(todas_las_citas)
    
    print(f"📊 ESTADÍSTICAS INICIALES:")
    print(f"   • Total citas a verificar: {total_citas}")
    print(f"   • Total vendedores con preferencias: {len(preferencias)}")
    
    print(f"\n🔎 VERIFICANDO CITA POR CITA...")
    print("-" * 80)
    
    for i, cita in enumerate(todas_las_citas, 1):
        vendedor = cita['vendedor']
        comprador = cita['comprador']
        horario = cita['horario']
        
        print(f"\n[{i:3}/{total_citas}] Verificando: {vendedor} → {comprador} ({horario})")
        
        # Registrar comprador encontrado
        compradores_encontrados.add(comprador)
        
        # Verificar si el vendedor tiene preferencias registradas
        if vendedor not in preferencias:
            print(f"❌ PROBLEMA: '{vendedor}' no tiene preferencias registradas")
            vendedores_sin_preferencias.add(vendedor)
            citas_incorrectas.append({
                **cita,
                'problema': 'Vendedor sin preferencias registradas'
            })
            continue
        
        # Verificar si el comprador está en las preferencias del vendedor
        compradores_preferidos = preferencias[vendedor]
        
        if comprador in compradores_preferidos:
            print(f"✅ CORRECTO: Cita válida")
            citas_correctas.append(cita)
        else:
            print(f"❌ INCORRECTO: '{vendedor}' NO solicitó cita con '{comprador}'")
            print(f"   Compradores solicitados por '{vendedor}': {sorted(list(compradores_preferidos))}")
            citas_incorrectas.append({
                **cita,
                'problema': f'Vendedor no solicitó este comprador',
                'compradores_solicitados': sorted(list(compradores_preferidos))
            })
    
    return citas_correctas, citas_incorrectas, vendedores_sin_preferencias, compradores_encontrados

def generar_reporte_detallado(preferencias, citas_correctas, citas_incorrectas, vendedores_sin_preferencias, compradores_encontrados):
    """
    Genera un reporte detallado de la verificación
    """
    print(f"\n" + "=" * 80)
    print("📊 REPORTE DETALLADO DE VERIFICACIÓN")
    print("=" * 80)
    
    total_citas = len(citas_correctas) + len(citas_incorrectas)
    
    # Estadísticas generales
    print(f"\n📈 ESTADÍSTICAS GENERALES:")
    print(f"   • Total citas verificadas: {total_citas}")
    print(f"   • Citas CORRECTAS: {len(citas_correctas)} ({len(citas_correctas)/total_citas*100:.1f}%)")
    print(f"   • Citas INCORRECTAS: {len(citas_incorrectas)} ({len(citas_incorrectas)/total_citas*100:.1f}%)")
    print(f"   • Vendedores sin preferencias: {len(vendedores_sin_preferencias)}")
    
    # Detalles de citas incorrectas
    if citas_incorrectas:
        print(f"\n❌ CITAS INCORRECTAS DETALLADAS:")
        print("-" * 60)
        
        for i, cita in enumerate(citas_incorrectas, 1):
            print(f"\n{i}. PROBLEMA EN CITA:")
            print(f"   Vendedor: {cita['vendedor']}")
            print(f"   Comprador asignado: {cita['comprador']}")
            print(f"   Horario: {cita['horario']}")
            print(f"   Problema: {cita['problema']}")
            
            if 'compradores_solicitados' in cita:
                print(f"   Compradores que SÍ solicitó: {cita['compradores_solicitados']}")
    
    # Vendedores sin preferencias
    if vendedores_sin_preferencias:
        print(f"\n⚠️  VENDEDORES SIN PREFERENCIAS REGISTRADAS:")
        print("-" * 60)
        for vendedor in sorted(vendedores_sin_preferencias):
            print(f"   • {vendedor}")
    
    # Análisis de cumplimiento por vendedor
    print(f"\n📋 ANÁLISIS POR VENDEDOR:")
    print("-" * 60)
    
    vendedores_con_citas = defaultdict(int)
    vendedores_con_correctas = defaultdict(int)
    
    for cita in citas_correctas + citas_incorrectas:
        vendedores_con_citas[cita['vendedor']] += 1
    
    for cita in citas_correctas:
        vendedores_con_correctas[cita['vendedor']] += 1
    
    for vendedor in sorted(preferencias.keys()):
        total_citas_vendedor = vendedores_con_citas.get(vendedor, 0)
        correctas_vendedor = vendedores_con_correctas.get(vendedor, 0)
        
        if total_citas_vendedor > 0:
            porcentaje = correctas_vendedor / total_citas_vendedor * 100
            estado = "✅" if porcentaje == 100 else "⚠️" if porcentaje > 0 else "❌"
            print(f"   {estado} {vendedor}: {correctas_vendedor}/{total_citas_vendedor} correctas ({porcentaje:.1f}%)")
        else:
            print(f"   ⭕ {vendedor}: Sin citas asignadas")
    
    # Compradores encontrados
    print(f"\n🏢 COMPRADORES DETECTADOS EN LA AGENDA:")
    print("-" * 60)
    for comprador in sorted(compradores_encontrados):
        print(f"   • {comprador}")
    
    return len(citas_incorrectas) == 0

def main():
    """
    Función principal del verificador
    """
    print("🔍 VERIFICADOR EXHAUSTIVO DE AGENDA")
    print("=" * 50)
    print("Este script verificará cada cita contra las preferencias originales")
    print("para garantizar que no hay asignaciones incorrectas.\n")
    
    # Archivos a verificar
    archivo_preferencias = "preferencias_multiples.csv"
    archivo_agenda = "agenda_completa.json"
    
    # Cargar datos
    preferencias = cargar_preferencias_desde_archivo(archivo_preferencias)
    if not preferencias:
        print("❌ No se pudieron cargar las preferencias. Abortando verificación.")
        return False
    
    agenda = cargar_agenda_generada(archivo_agenda)
    if not agenda:
        print("❌ No se pudo cargar la agenda. Abortando verificación.")
        return False
    
    # Extraer todas las citas
    todas_las_citas = extraer_todas_las_citas(agenda)
    print(f"📊 Total de citas extraídas: {len(todas_las_citas)}")
    
    # Verificar citas
    citas_correctas, citas_incorrectas, vendedores_sin_preferencias, compradores_encontrados = verificar_citas_vs_preferencias(preferencias, todas_las_citas)
    
    # Generar reporte
    agenda_valida = generar_reporte_detallado(
        preferencias, 
        citas_correctas, 
        citas_incorrectas, 
        vendedores_sin_preferencias,
        compradores_encontrados
    )
    
    # Resultado final
    print(f"\n" + "=" * 80)
    if agenda_valida:
        print("🎉 RESULTADO: ✅ AGENDA VÁLIDA - Todas las citas son correctas")
    else:
        print("⚠️  RESULTADO: ❌ AGENDA INVÁLIDA - Se encontraron citas incorrectas")
        print("    → Revisa los detalles arriba y corrige las preferencias o la lógica del generador")
    
    print("=" * 80)
    
    return agenda_valida

if __name__ == "__main__":
    main()