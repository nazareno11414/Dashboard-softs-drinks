import streamlit as st
import pandas as pd 
import datetime
from PIL import Image 
import plotly.express as px 
import plotly.graph_objects as go

df=pd.read_csv("Sales soft drinks.csv")
st.set_page_config(layout='wide')

st.markdown(
        """
        <style>
            .coca-cola {
                font-family: 'Arial', sans-serif;
                color: #D50032; /* Color rojo Coca-Cola */
                background-color: #000000; /* Fondo blanco */
                padding: 20px;
                border-radius: 8px;
                border: 2px solid #FFFF00; /* Borde rojo */
                text-align: center;
            }
            .coca-cola h1 {
                font-size: 48px;
                font-weight: bold;
            }
            .coca-cola p {
                font-size: 24px;
            }
        </style>
        """,
        unsafe_allow_html=True
)

image=Image.open("soft drinks.png")

html_texto = """
<center><h1 style="color: red;"><em><strong>Soft Drinks Interactive Sales Dashboard</em></strong></h1>
<p style="font-size: 20px;">
"""

# Crear columnas
col1, col2 = st.columns([0.1, 0.9])

# Colocar contenido en las columnas
with col1:
    st.image(image, width=200)  # Mostrar la imagen
with col2:
    st.markdown(html_texto, unsafe_allow_html=True)


col3,col4,col5=st.columns([0.1, 0.45,0.45])
with col3:
    box_date=str(datetime.datetime.now().strftime("%d %B %Y"))
    st.write(f"Ultima actualizacion:  \n {box_date}")
with col4:
    fig=px.bar(df,x="Retailer",y="Total Sales",labels={"Total Sales":"Total Sales {$} "},
               title="Total Sales by Retailer",hover_data={"Total Sales"},
               template="gridon",height=500)
    st.plotly_chart(fig,use_container_width=True)

    df = pd.read_csv("Sales soft drinks.csv")
    # Eliminar espacios y caracteres no numéricos (excepto el punto decimal)
    df["Total Sales"] = df["Total Sales"].str.replace(' ', '')  # Eliminar espacios
    df["Total Sales"] = df["Total Sales"].str.replace('[^\d.]', '', regex=True)  # Mantener solo números y puntos
    # Transformo los datos en numericos 
    df["Total Sales"] = pd.to_numeric(df["Total Sales"], errors='coerce')

    grouped_data = df.groupby("Retailer", as_index=False)["Total Sales"].sum()
    # Usar columnas para organizar la interfaz
    view1, dwn1 = st.columns([0.13,0.20])

    with view1:
        expander = st.expander("Retailer wise Sales")
        expander.write(grouped_data)

    with dwn1:
        # Convertir el DataFrame agrupado a CSV para la descarga
        csv_data = grouped_data.to_csv(index=False).encode("utf-8")
        st.download_button("Get Data", data=csv_data,
                        file_name="RetailerSales.csv", mime="text/csv")

    df["Invoice Date"] = pd.to_datetime(df["Invoice Date"], errors='coerce')
    df["Months-Year"] = df["Invoice Date"].dt.strftime("%b'%y")

    result=df.groupby(by=df["Months-Year"])["Total Sales"].sum().reset_index()
    
with col5:
    fig1 = px.line(result, x="Months-Year", y="Total Sales", title="Total Sales Over Time",
                    template="gridon")
    st.plotly_chart(fig1, use_container_width=True)
        
    view2, dwn2 = st.columns([0.13,0.20])
        
    grouped_data_year = df.groupby("Months-Year", as_index=False)["Total Sales"].sum()
    with view2:
        expander = st.expander("Year-Month wise Sales")
        expander.write(grouped_data_year)
    with dwn2:
        # Convertir el DataFrame agrupado a CSV para la descarga
        csv_data2 = grouped_data_year.to_csv(index=False).encode("utf-8")
        st.download_button("Get Data", data=csv_data2,
                    file_name="QuarterlySales.csv", mime="text/csv")
st.divider()  



df["Units Sold"] = df["Units Sold"].str.replace(' ', '')  # Eliminar espacios
df["Units Sold"] = df["Units Sold"].str.replace('[^\d.]', '', regex=True)  # Mantener solo números y puntos
# Transformo los datos en numericos 
df["Units Sold"] = pd.to_numeric(df["Units Sold"], errors='coerce')
result1=df.groupby(by="State")[["Total Sales","Units Sold"]].sum().reset_index()

#unidades vendidas como una linea 

fig3 = go.Figure()

# Agregar trazado de barras para "Total Sales"
fig3.add_trace(go.Bar(x=result1["State"], y=result1["Total Sales"], name="Total Sales"))

# Agregar trazado de líneas para "Units Sold"
fig3.add_trace(go.Scatter(x=result1["State"], y=result1["Units Sold"], mode="lines", name="Units Sold", yaxis="y2"))

# Actualizar el diseño del gráfico
fig3.update_layout(
    title="Total Sales and Units Sold by State",
    xaxis=dict(title="State"),
    yaxis=dict(title="Total Sales", showgrid=False),
    yaxis2=dict(title="Units Sold", overlaying="y", side="right"),
    template="gridon",
    legend=dict(x=1, y=1)
)
_, col6=st.columns([0.1,1])
with col6:
    st.plotly_chart(fig3,use_container_width=True)
    _,view3, dwn3 = st.columns([0.1, 1, 1])    
    with view3:
        expander = st.expander("View Data for Sales by Units Sold")
        expander.write(result1)
    with dwn3:
        # Convertir el DataFrame agrupado a CSV para la descarga
        csv_data3 = result1.to_csv(index=False).encode("utf-8")
        st.download_button("Get Data", data=csv_data3,
                    file_name="Sales_by_State.csv", mime="text/csv")

st.divider()

_,col7=st.columns([0.1,1])
treemap = df[["Region", "City", "Total Sales"]].groupby(by=["Region", "City"])["Total Sales"].sum().reset_index()

fig4=px.treemap(treemap,path=["Region","City"], values="Total Sales",
                hover_data=["Total Sales"],
                color="City",height=700,width=600
                )
fig4.update_traces(textinfo="label+value")
with col7:
    st.subheader(":point_right: Total Sales by Region and City in treemap")
    st.plotly_chart(fig4,use_container_width=True)
    _,view4, dwn4 = st.columns([0.1,1,1])    
    with view4:
        result2 = df[["Region", "City", "Total Sales"]].groupby(by=["Region", "City"])["Total Sales"].sum().reset_index()
        expander = st.expander("View Data for Total Sales by Region and City")
        expander.write(result2)
    with dwn4:
        # Convertir el DataFrame agrupado a CSV para la descarga
        csv_data4 = result2.to_csv(index=False).encode("utf-8")
        st.download_button("Get Data", data=csv_data3,
                    file_name="Total_Sales_by_Region_and_City.csv", mime="text/csv")