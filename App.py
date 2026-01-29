import streamlit as st
import google.generativeai as genai

# ==========================================
#  ZONA DE CONFIGURACIÓN
# ==========================================
MI_API_KEY = "AIzaSyD2ULijrtPY58U5NSBAj43oUHvybvc2flU".strip()
# ==========================================

# 1. Configuración de página
st.set_page_config(page_title="CodeMorph Auto", page_icon="", layout="wide")


try:
    genai.configure(api_key=MI_API_KEY)
    
    # --- AUTO-DETECCIÓN DE MODELO ---
    # Buscamos qué modelos permite usar tu cuenta
    modelos_disponibles = []
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            modelos_disponibles.append(m.name)
    
    # Seleccionamos el mejor modelo disponible automáticamente
    if not modelos_disponibles:
        st.error(" Tu API Key es válida, pero no tiene acceso a ningún modelo generativo.")
        st.stop()
    
    # Preferimos el 1.5 Flash si existe, si no, el primero de la lista
    if 'models/gemini-1.5-flash' in modelos_disponibles:
        MODELO_USAR = 'models/gemini-1.5-flash'
    elif 'models/gemini-pro' in modelos_disponibles:
        MODELO_USAR = 'models/gemini-pro'
    else:
        MODELO_USAR = modelos_disponibles[0] # El que sea que haya
        
except Exception as e:
    st.error(f" Error crítico de conexión: {e}")
    st.stop()

# 3. Interfaz
st.title(f" Asistente de Código")
st.caption(f"Conectado exitosamente usando: **{MODELO_USAR}**")
st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Código Original")
    source_lang = st.selectbox("Lenguaje Origen:", ["Auto-detectar", "Python", "JS", "Java", "C++", "C#"], index=0)
    code_input = st.text_area("Tu código:", height=400)

with col2:
    st.subheader("Configuración")
    target_lang = st.selectbox("Traducir a:", ["Python", "JavaScript", "Java", "C++", "C#"], index=0)
    st.markdown("---")
    output_container = st.empty()

# 4. Botones
st.markdown("---")
col_b1, col_b2 = st.columns(2)
with col_b1:
    btn_traducir = st.button(" Traducir", use_container_width=True, type="primary")
with col_b2:
    btn_explicar = st.button(" Explicar", use_container_width=True)

# 5. Ejecución
if (btn_traducir or btn_explicar) and code_input:
    try:
        with st.spinner("Procesando..."):
            model = genai.GenerativeModel(MODELO_USAR)
            
            if btn_traducir:
                prompt = f"Traduce este código de {source_lang} a {target_lang}. Solo código. \n\n{code_input}"
            else:
                prompt = f"Explica este código paso a paso en español. \n\n{code_input}"
            
            response = model.generate_content(prompt)
            
            with output_container:
                if btn_traducir:
                    # Limpiamos formateo extra
                    texto_limpio = response.text.replace("```python","").replace("```","")
                    st.code(texto_limpio)
                else:
                    st.markdown(response.text)
                    
    except Exception as e:
        st.error(f"Error al generar: {e}")
