# Exploratory-Data-Analysis-EDA-de-Incendios-Forestales-en-Brasil
Este proyecto tiene como objetivo analizar los incendios forestales registrados en Brasil durante un período determinado. Se desarrolló una clase llamada EDA en Python que permite realizar un análisis exploratorio detallado del conjunto de datos, generando visualizaciones y estadísticas relevantes.
---
Los datos fueron obtenidos del sitio web oficial del gobierno brasileño.

Kaggle dataset: amazon.csv
---

## Tabla de Contenidos
1. [Descripción del Proyecto](#descripción-del-proyecto)
2. [Descripción del Conjunto de Datos](#descripción-del-conjunto-de-datos)
3. [Funciones Principales](#funciones-principales)
4. [Visualizaciones Generadas](#visualizaciones-generadas)
5. [Cómo Ejecutar el Código](#cómo-ejecutar-el-código)
6. [Requisitos del Sistema](#requisitos-del-sistema)
7. [Autor](#autor)

---

## Descripción del Proyecto

El análisis responde preguntas clave sobre los incendios forestales en Brasil, tales como:
- Total de incendios registrados en el período analizado.
- Año y estado con mayor cantidad de incendios.
- Tendencias temporales y mensuales de los incendios.
- Comparación entre estados con más y menos incendios.

Se desarrollaron métodos en la clase `EDA` para automatizar el análisis y generar visualizaciones que facilitan la interpretación de los datos.

---

## Descripción del Conjunto de Datos

El conjunto de datos contiene información sobre incendios forestales registrados en Brasil. A continuación, algunos detalles importantes:
- **Observaciones**: Cada fila representa un registro de incendios en un estado brasileño durante un mes y año específicos.
- **Variables principales**:
  - `state`: Estado brasileño donde ocurrió el incendio.
  - `month`: Mes en el que se registraron los incendios.
  - `year`: Año del registro.
  - `number`: Número de incendios registrados.
- **Rangos de valores**:
  - `state`: Nombres de los estados de Brasil.
  - `month`: Meses del año (enero a diciembre).
  - `year`: Años en el rango del conjunto de datos.
  - `number`: Número de incendios (valor numérico positivo).

---

## Funciones Principales

La clase `EDA` contiene los siguientes métodos para el análisis exploratorio:

1. **show_columns_types**  
   Muestra información sobre las columnas, sus tipos de datos y valores nulos.

2. **missing_values**  
   Identifica valores nulos en el conjunto de datos y los visualiza con un heatmap.

3. **detect_duplicates**  
   Detecta y elimina filas duplicadas en el conjunto de datos.

4. **forest_fires_year**  
   Calcula el total de incendios registrados y los años cubiertos por los datos.

5. **wildfire_season**  
   Identifica el año con más incendios y genera un gráfico de línea con la distribución mensual.

6. **wildfire_months**  
   Muestra un histograma con la cantidad total de incendios para cada mes, acumulando todos los años.

7. **fire_state**  
   Identifica el estado con más incendios y visualiza los totales acumulados por estado.

8. **year_register**  
   Genera un box-plot para analizar la distribución de incendios por año.

9. **most_fire_state**  
   Muestra la evolución mensual de incendios para el estado con mayor cantidad de registros.

10. **diference_fire_state**  
    Compara los estados con más y menos incendios, graficando sus tendencias temporales y la diferencia absoluta entre ellos.

---

## Visualizaciones Generadas

El análisis genera los siguientes gráficos:

1. **Heatmap de valores nulos**  
   Representación visual de las columnas con datos faltantes.

2. **Gráfico de línea**  
   Distribución mensual de incendios para el año con más registros.

3. **Histograma acumulado**  
   Número total de incendios por mes para todos los años.

4. **Barplot por estado**  
   Estados ordenados por el total de incendios registrados.

5. **Box-plot anual**  
   Análisis de la distribución de incendios para cada año.

6. **Comparación de estados**  
   Gráfico con la evolución temporal de incendios en el estado con más y menos registros, incluyendo la diferencia absoluta entre ellos.

---

## Cómo Ejecutar el Código

1. Asegúrate de tener Python 3.8 o superior instalado en tu sistema.
2. Instala las dependencias necesarias utilizando `pip`:
   ```bash
   pip install pandas matplotlib seaborn
   ```
3. Descarga el archivo del conjunto de datos (`amazon.csv`) y colócalo en el mismo directorio que el código.
4. Ejecuta el script principal:
   ```bash
   python main.py
   ```

---

## Requisitos del Sistema

- **Python**: 3.8 o superior.
- **Librerías**:
  - `pandas`
  - `matplotlib`
  - `seaborn`
  - `sqlite3` (para consultas SQL opcionales)

---

## Autor

**Britez, Carnichi Santiago Luis**  
Analista de datos y Científico de datos   
LinkedIn: www.linkedin.com/in/santiago-luis-britez-101a8a217 

--- 
