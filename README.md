# Rueda de Negocios - Sistema de Gestión de Citas

Un sistema completo para la gestión y visualización de citas de una rueda de negocios, desarrollado en Python con múltiples vistas web estáticas.

## 🚀 Demo en Vivo

[Ver Demo](https://agenda-rueda-negocios.netlify.app) _(Actualizar después del despliegue)_

## ✨ Características

- **📊 Matriz Compradores-Horarios**: Vista principal con compradores como filas y horarios como columnas
- **🏪 Matriz Vendedores-Horarios**: Vista complementaria con vendedores como filas
- **📅 Agenda Web Completa**: Vista detallada de todas las citas organizadas por horarios
- **📋 Agenda Estática**: Formato optimizado para impresión
- **🔍 Visualizador Interactivo**: Herramienta para explorar y analizar la agenda
- **📱 Diseño Responsive**: Optimizado para móviles, tablets y desktop

## 📈 Estadísticas del Proyecto

- **61 citas programadas**
- **141 encuentros individuales**
- **31 vendedores participantes**
- **11 compradores**
- **98.6% de preferencias cumplidas**

## 🎯 Funcionalidades Avanzadas

### Restricciones Implementadas

- Máximo 3 vendedores por cita
- Regional SAS disponible solo de 8:30 AM - 10:30 AM
- ENCADENAMIENTOS PRODUCTIVOS como comprador (10:15 AM - 11:15 AM)
- Café Origen de la Montaña con doble rol (comprador y vendedor)

### Sistema de Navegación

- Panel de control central (`index.html`)
- Enlaces de navegación en todas las vistas
- Botones "🏠 Inicio" en cada cabecera

## 🛠️ Tecnologías Utilizadas

- **Backend**: Python 3.11+
- **Librerías**: openpyxl, python-docx
- **Frontend**: HTML5, CSS3, JavaScript
- **Estilos**: CSS Grid, Flexbox, Gradientes
- **Exportación**: Excel, CSV, JSON, Word

## 📁 Estructura del Proyecto

```
├── index.html                          # Panel de control principal
├── matriz_compradores_horarios.html    # Vista matriz por compradores
├── matriz_vendedores_horarios.html     # Vista matriz por vendedores
├── agenda_web_completa.html            # Agenda detallada
├── agenda_web_estatica.html            # Vista para impresión
├── visualizar_agenda.html              # Visualizador interactivo
├── agenda_rueda_negocios.py            # Motor de generación de citas
├── preferencias_multiples.csv          # Configuración de preferencias
├── agenda_rueda_negocios.xlsx          # Exportación Excel completa
├── documentos_vendedores/              # Documentos Word individuales
└── archivos de datos (CSV, JSON)
```

## 🚀 Instalación y Uso

### Para Desarrollo Local

1. **Clona el repositorio**

```bash
git clone https://github.com/ovicristian/agenda_rueda_negocios.git
cd agenda_rueda_negocios
```

2. **Instala las dependencias**

```bash
pip install openpyxl python-docx
```

3. **Ejecuta el generador**

```bash
python agenda_rueda_negocios.py
```

4. **Abre el navegador**

```
file://ruta/al/proyecto/index.html
```

### Para Visualización Web

Simplemente abre `index.html` en cualquier navegador web. No requiere servidor web ya que es completamente estático.

## 📊 Archivos Generados

- **`agenda_rueda_negocios.xlsx`**: Excel con 6 hojas completas
- **`agenda_rueda_negocios.csv`**: Datos en formato CSV
- **`resumen_vendedores.csv`**: Estadísticas por vendedor
- **`agenda_completa.json`**: Configuración completa en JSON
- **`documentos_vendedores/`**: 31 documentos Word individuales

## 🎨 Características de Diseño

- **Paleta de colores**: Azul para compradores, rojo para vendedores
- **Navegación horizontal**: Scroll optimizado para matrices extensas
- **Efectos visuales**: Gradientes, sombras, transiciones CSS
- **Iconografía**: Emojis para identificación rápida
- **Tipografía**: Segoe UI, sistema de fuentes moderno

## 📱 Compatibilidad

- ✅ Chrome/Chromium (Recomendado)
- ✅ Firefox
- ✅ Safari
- ✅ Edge
- ✅ Móviles iOS/Android

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para detalles.

## 👥 Contribución

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📧 Contacto

Proyecto desarrollado para gestión empresarial de ruedas de negocios.

**Link del Proyecto**: [https://github.com/ovicristian/agenda_rueda_negocios](https://github.com/ovicristian/agenda_rueda_negocios)

---

⭐ **¡Dale una estrella al proyecto si te ha sido útil!**
