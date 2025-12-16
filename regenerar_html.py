#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script para regenerar los archivos HTML con los datos actualizados del JSON
"""

import json
from datetime import datetime

def cargar_datos_json():
    """Cargar los datos desde agenda_completa.json"""
    try:
        with open('agenda_completa.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print("❌ Error: No se encontró el archivo agenda_completa.json")
        return None

def regenerar_matriz_compradores():
    """Regenerar matriz_compradores_horarios.html"""
    datos = cargar_datos_json()
    if not datos:
        return
        
    agenda = datos['agenda']
    
    # Obtener todos los compradores y horarios únicos
    compradores = set()
    horarios = list(agenda.keys())
    
    for horario, citas in agenda.items():
        for cita in citas:
            compradores.add(cita['comprador'])
    
    compradores = sorted(list(compradores))
    
    # Crear matriz
    matriz = {}
    for comprador in compradores:
        matriz[comprador] = {horario: [] for horario in horarios}
    
    # Llenar matriz con vendedores
    for horario, citas in agenda.items():
        for cita in citas:
            comprador = cita['comprador']
            vendedores = cita['vendedores']
            matriz[comprador][horario] = vendedores
    
    # Generar HTML
    html_content = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>📊 Matriz Compradores-Horarios | Rueda de Negocios</title>
    <style>
        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }}

        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
        }}

        .header {{
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            padding: 15px 25px;



            border-bottom: 1px solid rgba(255, 255, 255, 0.2);
        }}

        .home-button {{
            position: absolute;
            top: 25px;
            left: 25px;
            background: rgba(255, 255, 255, 0.2);
            backdrop-filter: blur(8px);
            border: 1px solid rgba(255, 255, 255, 0.3);
            padding: 8px 16px;
            border-radius: 20px;
            text-decoration: none;
            color: white;
            font-size: 18px;
            font-weight: 600;
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
        }}

        .home-button:hover {{
            background: rgba(255, 255, 255, 0.3);
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(0, 0, 0, 0.15);
        }}

        .header-content {{
            text-align: center;
            padding-left: 60px;
        }}

        .header h1 {{
            color: white;
            font-size: 2.2em;
            margin-bottom: 8px;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
        }}

        .header p {{
            color: rgba(255, 255, 255, 0.9);
            font-size: 1.1em;
            margin-bottom: 15px;
        }}

        .stats {{
            display: flex;
            justify-content: center;
            gap: 30px;
            flex-wrap: wrap;
        }}

        .stat-item {{
            background: rgba(255, 255, 255, 0.15);
            padding: 8px 16px;
            border-radius: 15px;
            backdrop-filter: blur(5px);
            border: 1px solid rgba(255, 255, 255, 0.2);
        }}

        .stat-number {{
            display: block;
            font-size: 1.4em;
            font-weight: bold;
            color: #FFD700;
        }}

        .stat-label {{
            font-size: 0.9em;
            color: rgba(255, 255, 255, 0.8);
        }}

        .container {{
            padding: 30px;
            max-width: 100%;
            margin: 0 auto;
        }}

        .table-container {{
            background: white;
            border-radius: 20px;
            padding: 25px;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.1);
            overflow-x: auto;
            border: 1px solid #e0e6ed;
        }}

        .matrix-table {{
            width: 100%;
            border-collapse: collapse;
            font-size: 0.85em;
            min-width: 1200px;
        }}

        .matrix-table th {{
            background: linear-gradient(135deg, #4CAF50, #45a049);
            color: white;
            padding: 12px 8px;
            text-align: center;
            font-weight: 600;
            border: 1px solid #45a049;
            white-space: nowrap;
            font-size: 0.8em;
        }}

        .matrix-table th:first-child {{
            background: linear-gradient(135deg, #2196F3, #1976D2);
            border-color: #1976D2;
            z-index: 11;
            min-width: 200px;
        }}

        .buyer-name {{
            background: linear-gradient(135deg, #f8f9fa, #e9ecef);
            font-weight: 600;
            padding: 12px;
            border: 1px solid #dee2e6;
            text-align: left;
            color: #2196F3;
            white-space: nowrap;
            min-width: 200px;
        }}

        .vendor-cell {{
            padding: 8px;
            border: 1px solid #dee2e6;
            text-align: center;
            vertical-align: top;
            background-color: #fafafa;
            min-width: 100px;
        }}

        .vendor-name {{
            display: inline-block;
            background: linear-gradient(135deg, #FF6B6B, #FF5252);
            color: white;
            padding: 4px 8px;
            border-radius: 12px;
            margin: 2px;
            font-size: 0.75em;
            font-weight: 500;
            box-shadow: 0 2px 4px rgba(255, 107, 107, 0.3);
            white-space: nowrap;
        }}

        .empty-cell {{
            color: #999;
            font-style: italic;
            padding: 12px;
        }}

        @media (max-width: 768px) {{
            .container {{
                padding: 15px;
            }}

            .header h1 {{
                font-size: 1.8em;
            }}

            .stats {{
                gap: 15px;
            }}

            .matrix-table {{
                font-size: 0.75em;
            }}

            .home-button {{
                font-size: 16px;
                padding: 6px 12px;
                top: 20px;
                left: 20px;
            }}

            .header-content {{
                padding-left: 50px;
            }}
        }}
    </style>
</head>
<body>
    <div class="header">
        <a href="index.html" class="home-button">🏠 Inicio</a>
        <div class="header-content">
            <h1>📊 Matriz Compradores-Horarios</h1>
            <p>Vista completa de la agenda - Compradores como filas, horarios como columnas</p>
            <div class="stats">
                <div class="stat-item">
                    <span class="stat-number">{sum(len(citas) for citas in agenda.values())}</span>
                    <span class="stat-label">Citas Programadas</span>
                </div>
                <div class="stat-item">
                    <span class="stat-number">{len(compradores)}</span>
                    <span class="stat-label">Compradores</span>
                </div>
                <div class="stat-item">
                    <span class="stat-number">{len(horarios)}</span>
                    <span class="stat-label">Franjas Horarias</span>
                </div>
                <div class="stat-item">
                    <span class="stat-number">{datetime.now().strftime('%d/%m/%Y')}</span>
                    <span class="stat-label">Última Actualización</span>
                </div>
            </div>
        </div>
    </div>

    <div class="container">
        <div class="table-container">
            <table class="matrix-table">
                <thead>
                    <tr>
                        <th>🏢 COMPRADOR</th>"""
    
    # Agregar encabezados de horarios
    for horario in horarios[:12]:  # Limitar a los primeros 12 horarios para evitar tabla muy ancha
        html_content += f'\n                        <th>⏰ {horario}</th>'
    
    html_content += """
                    </tr>
                </thead>
                <tbody>"""
    
    # Agregar filas de compradores
    for comprador in compradores:
        html_content += f'\n                  <tr>\n                    <td class="buyer-name">🏢 {comprador}</td>'
        
        for horario in horarios[:12]:  # Limitar a los primeros 12 horarios
            vendedores = matriz[comprador][horario]
            if vendedores:
                html_content += f'\n                    <td class="vendor-cell">'
                for vendedor in vendedores:
                    # Abreviar nombres inteligentemente
                    if len(vendedor) > 20:
                        # Para nombres muy largos, usar abreviación
                        palabras = vendedor.split()
                        if len(palabras) > 3:
                            nombre_display = f"{palabras[0]} {palabras[1]}..."
                        else:
                            nombre_display = vendedor[:15] + "..."
                    else:
                        # Mantener nombres completos para casos como "FLOR A FRUTO"
                        nombre_display = vendedor
                    html_content += f'\n                      <span class="vendor-name">{nombre_display}</span>'
                html_content += '\n                    </td>'
            else:
                html_content += '\n                    <td class="vendor-cell empty-cell">-</td>'
        
        html_content += '\n                  </tr>'
    
    html_content += """
                </tbody>
            </table>
        </div>
    </div>
</body>
</html>"""

    # Guardar el archivo
    with open('matriz_compradores_horarios.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"✅ matriz_compradores_horarios.html regenerado correctamente")
    print(f"   - {len(compradores)} compradores")
    print(f"   - {sum(len(citas) for citas in agenda.values())} citas totales")


def regenerar_matriz_vendedores():
    """Regenerar matriz_vendedores_horarios.html"""
    datos = cargar_datos_json()
    if not datos:
        return
        
    agenda = datos['agenda']
    
    # Obtener todos los vendedores y horarios únicos
    vendedores = set()
    horarios = list(agenda.keys())
    
    for horario, citas in agenda.items():
        for cita in citas:
            for vendedor in cita['vendedores']:
                vendedores.add(vendedor)
    
    vendedores = sorted(list(vendedores))
    
    # Crear matriz
    matriz = {}
    for vendedor in vendedores:
        matriz[vendedor] = {horario: [] for horario in horarios}
    
    # Llenar matriz con compradores
    for horario, citas in agenda.items():
        for cita in citas:
            comprador = cita['comprador']
            for vendedor in cita['vendedores']:
                matriz[vendedor][horario].append(comprador)
    
    # Generar HTML similar al de compradores pero con colores rojos
    html_content = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🏪 Matriz Vendedores-Horarios | Rueda de Negocios</title>
    <style>
        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }}

        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            background: linear-gradient(135deg, #ff6b6b 0%, #ee5a24 100%);
            min-height: 100vh;
        }}

        .header {{
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            padding: 15px 25px;



            border-bottom: 1px solid rgba(255, 255, 255, 0.2);
        }}

        .home-button {{
            position: absolute;
            top: 25px;
            left: 25px;
            background: rgba(255, 255, 255, 0.2);
            backdrop-filter: blur(8px);
            border: 1px solid rgba(255, 255, 255, 0.3);
            padding: 8px 16px;
            border-radius: 20px;
            text-decoration: none;
            color: white;
            font-size: 18px;
            font-weight: 600;
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
        }}

        .home-button:hover {{
            background: rgba(255, 255, 255, 0.3);
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(0, 0, 0, 0.15);
        }}

        .header-content {{
            text-align: center;
            padding-left: 60px;
        }}

        .header h1 {{
            color: white;
            font-size: 2.2em;
            margin-bottom: 8px;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
        }}

        .header p {{
            color: rgba(255, 255, 255, 0.9);
            font-size: 1.1em;
            margin-bottom: 15px;
        }}

        .stats {{
            display: flex;
            justify-content: center;
            gap: 30px;
            flex-wrap: wrap;
        }}

        .stat-item {{
            background: rgba(255, 255, 255, 0.15);
            padding: 8px 16px;
            border-radius: 15px;
            backdrop-filter: blur(5px);
            border: 1px solid rgba(255, 255, 255, 0.2);
        }}

        .stat-number {{
            display: block;
            font-size: 1.4em;
            font-weight: bold;
            color: #FFD700;
        }}

        .stat-label {{
            font-size: 0.9em;
            color: rgba(255, 255, 255, 0.8);
        }}

        .container {{
            padding: 30px;
            max-width: 100%;
            margin: 0 auto;
        }}

        .table-container {{
            background: white;
            border-radius: 20px;
            padding: 25px;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.1);
            overflow-x: auto;
            border: 1px solid #e0e6ed;
        }}

        .matrix-table {{
            width: 100%;
            border-collapse: collapse;
            font-size: 0.85em;
            min-width: 1200px;
        }}

        .matrix-table th {{
            background: linear-gradient(135deg, #e74c3c, #c0392b);
            color: white;
            padding: 12px 8px;
            text-align: center;
            font-weight: 600;
            border: 1px solid #c0392b;



            white-space: nowrap;
            font-size: 0.8em;
        }}

        .matrix-table th:first-child {{
            background: linear-gradient(135deg, #d32f2f, #b71c1c);
            border-color: #b71c1c;


            z-index: 11;
            min-width: 200px;
        }}

        .vendor-name {{
            background: linear-gradient(135deg, #f8f9fa, #e9ecef);
            font-weight: 600;
            padding: 12px;
            border: 1px solid #dee2e6;
            text-align: left;
            color: #d32f2f;



            white-space: nowrap;
            min-width: 200px;
        }}

        .buyer-cell {{
            padding: 8px;
            border: 1px solid #dee2e6;
            text-align: center;
            vertical-align: top;
            background-color: #fafafa;
            min-width: 100px;
        }}

        .buyer-name {{
            display: inline-block;
            background: linear-gradient(135deg, #2196F3, #1976D2);
            color: white;
            padding: 4px 8px;
            border-radius: 12px;
            margin: 2px;
            font-size: 0.75em;
            font-weight: 500;
            box-shadow: 0 2px 4px rgba(33, 150, 243, 0.3);
            white-space: nowrap;
        }}

        .empty-cell {{
            color: #999;
            font-style: italic;
            padding: 12px;
        }}

        @media (max-width: 768px) {{
            .container {{
                padding: 15px;
            }}

            .header h1 {{
                font-size: 1.8em;
            }}

            .stats {{
                gap: 15px;
            }}

            .matrix-table {{
                font-size: 0.75em;
            }}

            .home-button {{
                font-size: 16px;
                padding: 6px 12px;
                top: 20px;
                left: 20px;
            }}

            .header-content {{
                padding-left: 50px;
            }}
        }}
    </style>
</head>
<body>
    <div class="header">
        <a href="index.html" class="home-button">🏠 Inicio</a>
        <div class="header-content">
            <h1>🏪 Matriz Vendedores-Horarios</h1>
            <p>Vista complementaria - Vendedores como filas, horarios como columnas</p>
            <div class="stats">
                <div class="stat-item">
                    <span class="stat-number">{sum(len(citas) for citas in agenda.values())}</span>
                    <span class="stat-label">Citas Programadas</span>
                </div>
                <div class="stat-item">
                    <span class="stat-number">{len(vendedores)}</span>
                    <span class="stat-label">Vendedores</span>
                </div>
                <div class="stat-item">
                    <span class="stat-number">{len(horarios)}</span>
                    <span class="stat-label">Franjas Horarias</span>
                </div>
                <div class="stat-item">
                    <span class="stat-number">{datetime.now().strftime('%d/%m/%Y')}</span>
                    <span class="stat-label">Última Actualización</span>
                </div>
            </div>
        </div>
    </div>

    <div class="container">
        <div class="table-container">
            <table class="matrix-table">
                <thead>
                    <tr>
                        <th>☕ VENDEDOR</th>"""
    
    # Agregar encabezados de horarios
    for horario in horarios[:12]:  # Limitar a los primeros 12 horarios
        html_content += f'\n                        <th>⏰ {horario}</th>'
    
    html_content += """
                    </tr>
                </thead>
                <tbody>"""
    
    # Agregar filas de vendedores
    for vendedor in vendedores:
        html_content += f'\n                  <tr>\n                    <td class="vendor-name">☕ {vendedor}</td>'
        
        for horario in horarios[:12]:  # Limitar a los primeros 12 horarios
            compradores = matriz[vendedor][horario]
            if compradores:
                html_content += f'\n                    <td class="buyer-cell">'
                for comprador in compradores:
                    # Abreviar nombres inteligentemente
                    if len(comprador) > 20:
                        # Para nombres muy largos, usar abreviación
                        palabras = comprador.split()
                        if len(palabras) > 3:
                            nombre_display = f"{palabras[0]} {palabras[1]}..."
                        else:
                            nombre_display = comprador[:15] + "..."
                    else:
                        # Mantener nombres completos para casos normales
                        nombre_display = comprador
                    html_content += f'\n                      <span class="buyer-name">{nombre_display}</span>'
                html_content += '\n                    </td>'
            else:
                html_content += '\n                    <td class="buyer-cell empty-cell">-</td>'
        
        html_content += '\n                  </tr>'
    
    html_content += """
                </tbody>
            </table>
        </div>
    </div>
</body>
</html>"""

    # Guardar el archivo
    with open('matriz_vendedores_horarios.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"✅ matriz_vendedores_horarios.html regenerado correctamente")
    print(f"   - {len(vendedores)} vendedores")
    print(f"   - {sum(len(citas) for citas in agenda.values())} citas totales")

def main():
    """Función principal"""
    print("🔄 Regenerando archivos HTML desde agenda_completa.json...")
    print()
    
    regenerar_matriz_compradores()
    regenerar_matriz_vendedores()
    
    print()
    print("✅ Regeneración completada exitosamente!")
    print("📂 Archivos actualizados:")
    print("   - matriz_compradores_horarios.html") 
    print("   - matriz_vendedores_horarios.html")

if __name__ == "__main__":
    main()
