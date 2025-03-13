# 📂 docs/README.md - Documentación del Proyecto
"""
# 📊 Selección, Pivotación y Envío de Datos en Python con Reportes en HTML

## 📌 Descripción del Proyecto

Este proyecto implementa una solución en **Python** para la **selección, transformación y visualización de datos**, generando reportes personalizados para cada país y enviándolos automáticamente por **correo en formato HTML con gráficos embebidos**. Incluye:

- **Extracción y selección de datos desde SQL Server.**
- **Transformación de datos mediante pivotación en Pandas.**
- **Generación de vistas personalizadas para cada país.**
- **Creación de gráficos en HTML con Plotly para visualización en correos.**
- **Automatización del envío de reportes con SMTP.**

## 📂 Estructura del Proyecto
```
📁 Data_Transformation_Email
│── 📂 src/
│   │── data_selection.py  # Selección de datos desde SQL Server
│   │── data_pivot.py  # Pivotación y transformación de datos
│   │── generate_reports.py  # Generación de reportes en HTML con gráficos
│   │── send_email.py  # Envío automatizado de correos con reportes
│── 📂 tests/
│   │── test_data_pivot.py  # Pruebas de validación de transformación de datos
│   │── test_send_email.py  # Pruebas de envío de correos
│── 📂 docs/
│   │── README.md  # Documentación del proyecto
```

## 🚀 Instalación y Configuración

1. **Clona este repositorio:**
   ```sh
   git clone https://github.com/emmacm20-lab/Data_Transformation_Email.git
   ```
2. **Instala los requerimientos del proyecto:**
   ```sh
   pip install -r requirements.txt
   ```
3. **Ejecuta la selección y transformación de datos:**
   ```sh
   python src/data_selection.py
   python src/data_pivot.py
   ```
4. **Genera los reportes en HTML:**
   ```sh
   python src/generate_reports.py
   ```
5. **Envía los reportes por correo:**
   ```sh
   python src/send_email.py
   ```

## 📩 Flujo de Trabajo
1. **Selección de Datos**: Se extraen datos de SQL Server con criterios dinámicos.
2. **Transformación y Pivotación**: Los datos se reorganizan en formato de reportes estructurados.
3. **Generación de Reportes**: Se crean gráficos en HTML con Plotly.
4. **Envío de Correos**: Se automatiza el envío de reportes con gráficos embebidos.

## 🛠 Tecnologías Utilizadas
- **Python & Pandas**: Transformación y manipulación de datos.
- **SQL Server**: Extracción de información estructurada.
- **Plotly**: Creación de gráficos embebidos en HTML.
- **SMTP (Email)**: Automatización del envío de reportes.

## 📈 Resultados Esperados
- 📌 **Automatización del proceso de selección y transformación de datos.**
- 📌 **Visualización interactiva de reportes con gráficos en HTML.**
- 📌 **Envío automático de reportes personalizados por país.**
- 📌 **Reducción del esfuerzo manual en la generación de reportes.**

## 🧪 Pruebas
El proyecto incluye pruebas unitarias para validar la transformación de datos y el envío de correos.
1. **Ejecución de pruebas:**
   ```sh
   python -m unittest discover tests/
   ```

## 📬 Contacto
Para consultas o sugerencias, contáctame en [emmanuel.cmora20@gmail.com].
"""
