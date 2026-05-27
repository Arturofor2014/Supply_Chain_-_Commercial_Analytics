import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="OC Shoes — Business Simulator", layout="wide", page_icon="👟")

st.markdown("""
<style>
  .stApp { background-color: #ffffff; }
  .brand-header {
    background: linear-gradient(135deg, #1a1a2e 0%, #E63946 100%);
    border-radius: 14px; padding: 28px 40px; margin-bottom: 8px;
  }
  .brand-title { color: #fff; font-size: 32px; font-weight: 900; letter-spacing: 2px; }
  .brand-title span { color: #FFD700; }
  .brand-sub { color: rgba(255,255,255,0.75); font-size: 14px; margin-top: 4px; }
  .sec-title { font-size: 20px; font-weight: 800; color: #1a1a2e; margin-bottom: 4px; }
  .sec-sub { font-size: 13px; color: #888; margin-bottom: 18px; }
</style>
""", unsafe_allow_html=True)

# ── HEADER ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="brand-header">
  <div class="brand-title">👟 OC <span>Shoes</span></div>
  <div class="brand-sub">Business Simulator · Cadena Comercial y Financiera Completa</div>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.sidebar.markdown("### 👤 Arturo Aguilar")
st.sidebar.caption("Senior Commercial & Financial Analytics Engineer · 7+ años")
st.sidebar.divider()
st.sidebar.markdown("**Navegación:**")

seccion = st.sidebar.radio("Sección", [
    
    "🏠  Presentación",
    "1 · Planificación de Producción",
    "2 · Logística y Distribución",
    "3 · Costos del Producto",
    "4 · Estrategia de Precio",
    "5 · Forecast de Ventas",
    "6 · Presupuesto Comercial",
    "7 · Real vs Forecast",
    "8 · Dashboard Ejecutivo",
])

st.sidebar.divider()
st.sidebar.caption("OC Shoes · Simulador empresarial")

st.divider()

# ── 0 · PRESENTACIÓN ─────────────────────────────────────────────────────────
if seccion == "🏠  Presentación":
    st.markdown("""
    <style>
      .pres-box {
        background: #ffffff;
        border: 1px solid #e0e7f0;
        border-radius: 16px;
        padding: 44px 52px;
        box-shadow: 0 2px 16px rgba(0,0,0,.06);
      }
      .pres-eyebrow {
        font-size: 12px; color: #E63946; letter-spacing: 2px;
        text-transform: uppercase; margin-bottom: 10px; font-weight: 700;
      }
      .pres-name {
        font-size: 34px; font-weight: 900; color: #1a1a2e; margin-bottom: 6px;
      }
      .pres-name span { color: #E63946; }
      .pres-role {
        font-size: 15px; color: #E63946; font-weight: 700;
        letter-spacing: 1px; margin-bottom: 24px;
      }
      .pres-obj-title {
        font-size: 13px; font-weight: 800; color: #1a1a2e;
        text-transform: uppercase; letter-spacing: 1px; margin-bottom: 10px;
      }
      .pres-obj {
        font-size: 15px; color: #444; line-height: 1.75; max-width: 820px; margin-bottom: 28px;
      }
      .pres-tags { display: flex; flex-wrap: wrap; gap: 10px; }
      .pres-tag {
        background: #fff0f1; border: 1px solid #E63946;
        color: #E63946; font-size: 12px; font-weight: 700;
        padding: 5px 14px; border-radius: 20px;
      }
    </style>

    <div class="pres-box">
      <div class="pres-eyebrow">Simulador Empresarial · OC Shoes</div>
      <div class="pres-name">Portafolio de <span>Ing. Arturo Aguilar</span></div>
      <div class="pres-role">Senior Commercial & Financial Analytics Engineer</div>

      <div class="pres-obj-title">Objetivo del Proyecto</div>
      <div class="pres-obj">
        Este simulador replica la cadena comercial y financiera completa de una marca ficticia de
        zapatillas — <strong>OC Shoes</strong> — desde la orden de fabricación hasta el análisis
        de rentabilidad ejecutiva. El objetivo es demostrar la capacidad de modelar, integrar y
        visualizar datos a lo largo de toda la operación: producción, logística, costos, precios,
        forecast de ventas, presupuesto y control de gestión.<br><br>
        Cada sección es interactiva y está diseñada para ser expandida con datos reales,
        conectada a fuentes externas o adaptada a cualquier categoría de producto o industria.
      </div>

      <div class="pres-tags">
        <span class="pres-tag">🏭 Planificación</span>
        <span class="pres-tag">🚢 Logística</span>
        <span class="pres-tag">💵 Costos & Pricing</span>
        <span class="pres-tag">📈 Forecast</span>
        <span class="pres-tag">📋 Presupuesto</span>
        <span class="pres-tag">🖥️ Dashboard Ejecutivo</span>
      </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.info("👈 Selecciona una sección en el menú lateral para comenzar.")

# ── 1 · PLANIFICACIÓN DE PRODUCCIÓN ──────────────────────────────────────────
elif seccion == "1 · Planificación de Producción":
    st.markdown('<div class="sec-title">🏭 Planificación de Producción</div>', unsafe_allow_html=True)
    st.markdown('<div class="sec-sub">Orden de fabricación y tiempos estimados</div>', unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    unidades   = c1.number_input("Unidades a pedir", value=5000, step=500)
    moq        = c2.number_input("MOQ (mínimo de orden)", value=1000, step=100)
    dias_prod  = c1.number_input("Días de producción estimados", value=45, step=5)
    fecha_ini  = c2.date_input("Fecha inicio producción")

    import datetime
    fecha_salida = fecha_ini + datetime.timedelta(days=int(dias_prod))

    st.markdown("<br>", unsafe_allow_html=True)
    m1, m2, m3 = st.columns(3)
    m1.metric("Unidades ordenadas", f"{unidades:,}")
    m2.metric("Días de producción", f"{dias_prod} días")
    m3.metric("Fecha salida de fábrica", str(fecha_salida))

    if unidades < moq:
        st.error(f"⚠️ La orden ({unidades:,} u.) está por debajo del MOQ ({moq:,} u.)")
    else:
        st.success(f"✅ Orden válida — {unidades:,} unidades supera el MOQ de {moq:,}")

# ── 2 · LOGÍSTICA Y DISTRIBUCIÓN ─────────────────────────────────────────────
elif seccion == "2 · Logística y Distribución":
    st.markdown('<div class="sec-title">🚢 Logística y Distribución</div>', unsafe_allow_html=True)
    st.markdown('<div class="sec-sub">Transporte, aduana y tiempos de tránsito</div>', unsafe_allow_html=True)

    via = st.radio("Vía de transporte", ["Marítimo", "Aéreo"], horizontal=True)
    dias_transito = 35 if via == "Marítimo" else 5

    df = pd.DataFrame({
        "Concepto":  ["Flete", "Seguro de carga", "Impuesto de aduana", "Nacionalización", "Almacenaje"],
        "Costo ($)": [8500, 420, 3200, 1800, 600] if via == "Marítimo" else [22000, 800, 3200, 1800, 400],
    })
    df["% del Total"] = (df["Costo ($)"] / df["Costo ($)"].sum() * 100).round(1)

    st.dataframe(df, use_container_width=True, hide_index=True)

    c1, c2, c3 = st.columns(3)
    c1.metric("Vía seleccionada", via)
    c2.metric("Días en tránsito", f"{dias_transito} días")
    c3.metric("Costo logístico total", f"${df['Costo ($)'].sum():,.0f}")

# ── 3 · COSTOS DEL PRODUCTO ───────────────────────────────────────────────────
elif seccion == "3 · Costos del Producto":
    st.markdown('<div class="sec-title">💵 Costos del Producto</div>', unsafe_allow_html=True)
    st.markdown('<div class="sec-sub">Desglose de costos por unidad y landed cost total</div>', unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    fab      = c1.number_input("Costo de fabricación / u.",  value=18.00, step=0.50)
    royalty  = c2.number_input("Royalties / u.",              value=1.80,  step=0.10)
    empaque  = c1.number_input("Empaque / u.",                value=0.90,  step=0.10)
    seguro   = c2.number_input("Seguro / u.",                 value=0.30,  step=0.05)
    impuesto = c1.number_input("Impuestos / u.",              value=2.50,  step=0.10)
    logis    = c2.number_input("Costos logísticos / u.",      value=3.20,  step=0.10)

    landed = fab + royalty + empaque + seguro + impuesto + logis

    df = pd.DataFrame({
        "Componente": ["Fabricación", "Royalties", "Empaque", "Seguro", "Impuestos", "Logística"],
        "Costo ($)":  [fab, royalty, empaque, seguro, impuesto, logis],
    })
    df["% del Landed"] = (df["Costo ($)"] / landed * 100).round(1)

    st.dataframe(df, use_container_width=True, hide_index=True)
    st.metric("💰 Landed Cost por unidad", f"${landed:.2f}")

# ── 4 · ESTRATEGIA DE PRECIO ──────────────────────────────────────────────────
elif seccion == "4 · Estrategia de Precio":
    st.markdown('<div class="sec-title">🏷️ Estrategia de Precio</div>', unsafe_allow_html=True)
    st.markdown('<div class="sec-sub">Márgenes, precio mayorista y retail sugerido</div>', unsafe_allow_html=True)

    landed   = st.number_input("Landed cost / u. ($)", value=26.70, step=0.50)
    margen   = st.slider("Margen mayorista deseado (%)", 20, 80, 45)
    multiplo = st.slider("Múltiplo retail (sobre mayorista)", 1.5, 3.5, 2.2)

    precio_may   = landed / (1 - margen / 100)
    precio_retail = precio_may * multiplo
    ganancia_u   = precio_may - landed

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Landed Cost",       f"${landed:.2f}")
    c2.metric("Precio Mayorista",  f"${precio_may:.2f}")
    c3.metric("Precio Retail",     f"${precio_retail:.2f}")
    c4.metric("Ganancia / unidad", f"${ganancia_u:.2f}", f"{margen}%")

# ── 5 · FORECAST DE VENTAS ────────────────────────────────────────────────────
elif seccion == "5 · Forecast de Ventas":
    st.markdown('<div class="sec-title">📈 Forecast de Ventas</div>', unsafe_allow_html=True)
    st.markdown('<div class="sec-sub">Pronóstico mensual 12 meses · Temporadas y canales</div>', unsafe_allow_html=True)

    meses   = ["Ene","Feb","Mar","Abr","May","Jun","Jul","Ago","Sep","Oct","Nov","Dic"]
    tienda  = [320,290,340,380,420,310,290,350,410,480,520,600]
    ecomm   = [180,160,200,220,260,190,170,210,250,300,340,410]
    distrib = [500,460,540,580,620,480,450,530,590,660,720,850]

    df = pd.DataFrame({"Mes": meses, "Tienda Física": tienda, "E-commerce": ecomm, "Distribuidores": distrib})
    df["Total"] = df["Tienda Física"] + df["E-commerce"] + df["Distribuidores"]

    st.dataframe(df, use_container_width=True, hide_index=True)
    st.line_chart(df.set_index("Mes")[["Tienda Física", "E-commerce", "Distribuidores"]])

    c1, c2, c3 = st.columns(3)
    c1.metric("Total anual proyectado", f"{df['Total'].sum():,} u.")
    c2.metric("Mes pico", meses[df['Total'].idxmax()])
    c3.metric("Mes más bajo", meses[df['Total'].idxmin()])

# ── 6 · PRESUPUESTO COMERCIAL ────────────────────────────────────────────────
elif seccion == "6 · Presupuesto Comercial":
    st.markdown('<div class="sec-title">📋 Presupuesto Comercial</div>', unsafe_allow_html=True)
    st.markdown('<div class="sec-sub">Ventas, ingresos, costos y margen bruto proyectado</div>', unsafe_allow_html=True)

    meses   = ["Ene","Feb","Mar","Abr","May","Jun","Jul","Ago","Sep","Oct","Nov","Dic"]
    ventas  = [1000, 910, 1080, 1180, 1300, 980, 910, 1090, 1250, 1440, 1580, 1860]
    precio  = 58.50
    costo   = 26.70

    df = pd.DataFrame({
        "Mes":        meses,
        "Unidades":   ventas,
        "Ingresos ($)": [v * precio for v in ventas],
        "Costos ($)":   [v * costo  for v in ventas],
    })
    df["Margen Bruto ($)"] = df["Ingresos ($)"] - df["Costos ($)"]
    df["Margen %"]         = (df["Margen Bruto ($)"] / df["Ingresos ($)"] * 100).round(1)

    st.dataframe(df, use_container_width=True, hide_index=True)
    st.bar_chart(df.set_index("Mes")[["Ingresos ($)", "Costos ($)"]])

    c1, c2, c3 = st.columns(3)
    c1.metric("Ingresos anuales",    f"${df['Ingresos ($)'].sum():,.0f}")
    c2.metric("Margen bruto anual",  f"${df['Margen Bruto ($)'].sum():,.0f}")
    c3.metric("Margen % promedio",   f"{df['Margen %'].mean():.1f}%")

# ── 7 · REAL VS FORECAST ─────────────────────────────────────────────────────
elif seccion == "7 · Real vs Forecast":
    st.markdown('<div class="sec-title">📊 Ejecución Real vs Forecast</div>', unsafe_allow_html=True)
    st.markdown('<div class="sec-sub">Desviaciones, variación % y KPIs de cumplimiento</div>', unsafe_allow_html=True)

    meses    = ["Ene","Feb","Mar","Abr","May","Jun"]
    forecast = [1000, 910, 1080, 1180, 1300, 980]
    real     = [980,  870, 1120, 1050, 1380, 940]

    df = pd.DataFrame({"Mes": meses, "Forecast": forecast, "Real": real})
    df["Variación"]  = df["Real"] - df["Forecast"]
    df["Variación %"] = (df["Variación"] / df["Forecast"] * 100).round(1)
    df["Estado"]     = df["Variación %"].apply(lambda x: "✅ OK" if abs(x) <= 5 else ("🟡 Alerta" if abs(x) <= 10 else "🔴 Desvío"))

    st.dataframe(df, use_container_width=True, hide_index=True)
    st.line_chart(df.set_index("Mes")[["Forecast", "Real"]])

    cumpl = (df["Real"].sum() / df["Forecast"].sum() * 100)
    c1, c2, c3 = st.columns(3)
    c1.metric("Cumplimiento acumulado", f"{cumpl:.1f}%")
    c2.metric("Mejor mes",  meses[df["Variación %"].idxmax()])
    c3.metric("Peor mes",   meses[df["Variación %"].idxmin()])

# ── 8 · DASHBOARD EJECUTIVO ───────────────────────────────────────────────────
elif seccion == "8 · Dashboard Ejecutivo":
    st.markdown('<div class="sec-title">🖥️ Dashboard Ejecutivo</div>', unsafe_allow_html=True)
    st.markdown('<div class="sec-sub">Vista consolidada de inventario, rotación y rentabilidad</div>', unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Inventario disponible", "3,240 u.", "-180 u.")
    c2.metric("Sell Through",          "67%",      "+4%")
    c3.metric("Rotación inventario",   "4.2x",     "+0.3x")
    c4.metric("Rentabilidad bruta",    "54.3%",    "+1.2%")

    st.markdown("#### Top Modelos Vendidos")
    top = pd.DataFrame({
        "Modelo":       ["OC Runner Pro", "OC Street", "OC Casual", "OC Lite", "OC Sport X"],
        "Unidades":     [1820, 1540, 1210, 980, 760],
        "Ingresos ($)": [106470, 90090, 70785, 57330, 44460],
        "Margen %":     [56, 52, 50, 48, 54],
    })
    st.dataframe(top, use_container_width=True, hide_index=True)
    st.bar_chart(top.set_index("Modelo")["Unidades"])
