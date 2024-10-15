Descripción del Código

Este código crea un dashboard interactivo utilizando Streamlit, que permite visualizar y analizar datos de ventas de bebidas refrescantes a partir de un archivo CSV llamado "Sales soft drinks.csv". El dashboard incluye gráficos y tablas que permiten a los usuarios obtener información sobre las ventas por minorista, por período de tiempo, por estado, y por región y ciudad.

Componentes del Código
Importaciones:

streamlit as st: Importa la biblioteca Streamlit para crear la interfaz del dashboard.
pandas as pd: Para manipulación y análisis de datos en forma de DataFrames.
datetime: Para trabajar con fechas y horas.
Image de PIL: Para cargar imágenes en el dashboard.
plotly.express as px y plotly.graph_objects as go: Para crear visualizaciones interactivas.
Carga de Datos:

df=pd.read_csv("Sales soft drinks.csv"): Carga el archivo CSV que contiene los datos de ventas.
Configuración de la Página:

st.set_page_config(layout='wide'): Configura el layout de la página para que sea más amplio.
Estilos Personalizados:

Se utiliza CSS para personalizar la apariencia del título y otros elementos, usando colores y estilos específicos.
Imagen y Títulos:

Se carga una imagen llamada "soft drinks.png" y se muestra junto a un título que describe el dashboard.
Columnas:

Se crean varias columnas para organizar el contenido del dashboard.
Visualización de Ventas Totales por Minorista:

Se crea un gráfico de barras usando plotly.express que muestra las ventas totales por minorista.
Preprocesamiento de Datos:

Se eliminan espacios y caracteres no numéricos de la columna "Total Sales", y se convierten a tipo numérico.
Se agrupan las ventas totales por minorista.
Expansores para Mostrar Datos:

Se utilizan expander para mostrar tablas con los datos agrupados, permitiendo que los usuarios vean detalles adicionales y descarguen los datos en formato CSV.
Visualización de Ventas Totales a lo Largo del Tiempo:

Se crea un gráfico de líneas que muestra cómo las ventas totales cambian con el tiempo.
Análisis por Estado:

Se agrupan las ventas totales y unidades vendidas por estado.
Se crea un gráfico combinado (barras para "Total Sales" y líneas para "Units Sold").
Visualización por Región y Ciudad:

Se crea un gráfico de treemap que representa las ventas totales por región y ciudad.
Descargas de Datos:

Se ofrecen botones de descarga para que los usuarios puedan obtener los datos en formato CSV desde diferentes secciones del dashboard.
Uso del Dashboard
Este dashboard es útil para analistas de ventas, gerentes de marketing o cualquier persona interesada en comprender mejor el desempeño de las ventas de bebidas refrescantes. Proporciona una forma visual e interactiva de explorar datos, permitiendo a los usuarios:

Visualizar rápidamente las ventas totales por minorista.
Analizar cómo varían las ventas a lo largo del tiempo.
Comparar las ventas por estado y ver la cantidad de unidades vendidas.
Examinar los datos de ventas por región y ciudad a través de un treemap.
Descargar datos específicos para análisis adicionales en Excel u otras herramientas.

Code Description

This code creates an interactive dashboard using Streamlit, designed to visualize and analyze sales data for soft drinks from a CSV file titled "Sales soft drinks.csv". The dashboard includes graphs and tables that allow users to gain insights into sales by retailer, time period, state, and by region and city.

Code Components
Imports:

streamlit as st: Imports the Streamlit library to build the dashboard interface.
pandas as pd: Used for data manipulation and analysis in DataFrame format.
datetime: Facilitates working with dates and times.
Image from PIL: To load images in the dashboard.
plotly.express as px and plotly.graph_objects as go: Tools for creating interactive visualizations.
Data Loading:

df=pd.read_csv("Sales soft drinks.csv"): Loads the CSV file containing sales data.
Page Configuration:

st.set_page_config(layout='wide'): Configures the page layout for a wider and more visually appealing design.
Custom Styles:

CSS is utilized to customize the appearance of the title and other elements, applying specific colors and styles that evoke the Coca-Cola brand.
Image and Titles:

An image named "soft drinks.png" is loaded and presented alongside a title that describes the purpose of the dashboard.
Columns:

Several columns are created to organize the dashboard content, optimizing space and readability.
Total Sales by Retailer Visualization:

A bar chart is generated using plotly.express, illustrating total sales for each retailer.
Data Preprocessing:

Spaces and non-numeric characters are removed from the "Total Sales" column, converting it to a numeric type.
Total sales are grouped by retailer, providing a clear summary.
Expanders for Data Display:

Expanders are used to display tables with grouped data, allowing users to see additional details and download data in CSV format.
Total Sales Over Time Visualization:

A line chart is created to show the evolution of total sales over time, facilitating trend analysis.
State-wise Analysis:

Total sales and units sold are grouped by state.
A combined chart is presented showing bars for "Total Sales" and lines for "Units Sold".
Region and City Visualization:

A treemap chart is generated representing total sales by region and city, providing a clear and visually appealing view.
Data Downloads:

Download buttons are provided for users to obtain specific data in CSV format from various sections of the dashboard.
Dashboard Usage
This dashboard is invaluable for sales analysts, marketing managers, or anyone interested in better understanding the performance of soft drink sales. It provides a visual and interactive way to explore data, allowing users to:

Quickly visualize total sales by retailer.
Analyze how sales vary over time.
Compare sales by state and examine the number of units sold.
Investigate sales data by region and city through a treemap.
Download specific data for further analysis in Excel or other tools.
