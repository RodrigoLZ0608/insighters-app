import streamlit as st

# ===== CONFIGURACIÓN DE LA PÁGINA =====
st.set_page_config(page_title="Insighters", layout="wide")

# ===== FUNCIÓN PARA CARGAR CSS =====

# ===== HEADER =====
with st.container():
    col_logo, col_menu = st.columns([1, 5])

    # Logo a la izquierda
    with col_logo:
        st.markdown("### 🟣 Insighters")

    # Botones a la derecha
    with col_menu:
        spacer, btn1, btn2, btn3, btn4, btn5, btn6 = st.columns(
            [7, 2, 2, 2, 2, 2, 4]
        )

        with btn1:
            st.button("Nosotros")
        with btn2:
            st.button("Servicios")
        with btn3:
            st.button("Proyectos")
        with btn4:
            st.button("Recursos")
        with btn5:
            st.button("Contacto")
        with btn6:
            st.button("Agendar asesoría")



st.divider()

# ===== HERO =====
with st.container():
    col1, col2 = st.columns([2, 1])

    # TEXTO HERO
    with col1:
        st.markdown("AGENCIA DIGITAL")
        st.subheader("Vemos lo que otros pasan por alto para hacer crecer tu marca con criterio")
        st.markdown("""
        Te ayudamos a escalar ventas y mejorar tu rentabilidad con  
        estrategias, contenido y análisis centrados en tus consumidores.  
        Menos improvisación, más decisiones con data
        """)

        # BOTONES HERO
        b1, b2 = st.columns(2)
        with b1:
            st.button("Quiero una asesoría")  
        with b2:
            st.button("Ver proyectos destacados")

        # LOGROS HERO
        col_achievements = st.columns(2)
        col_achievements[0].markdown("+20 marcas acompañadas")
        col_achievements[1].markdown("360° estrategia, contenido y paid media")

    # VIDEO SIMULADO
    with col2:
        st.info("Video presentación (simulado)")
        st.video("https://www.youtube.com/watch?v=iWCenGIIBVE")

st.divider()
with st.container():
    left, center, right = st.columns([1, 2, 1])

    with center:
        st.subheader(
            "Comercializas servicios o productos pero no estás llegando a tus metas de ventas. ¿Por qué?"
        )

    
    with st.container():
        c1, c2, c3, c4, c5 = st.columns(5)

    items = [
        ("🎯", "No cuentas con una estrategia integral enfocada en la obtención y conversión de leads."),
        ("🧠", "Una vez que llegan los leads, no sabes qué hacer con ellos ni cómo nutrirlos."),
        ("❓", "No sabes cuánto vale tu cliente, por lo que tampoco sabes cuánto invertir para conseguirlo."),
        ("📈", "Tus ventas fluctúan mes a mes y sientes que no tienes control de las variables clave."),
        ("⚙️", "No tienes la tecnología ni procesos para automatizar, fidelizar y generar recompra.")
    ]

    for col, (emoji, text) in zip([c1, c2, c3, c4, c5], items):
        with col:
            # Simulación de centrado
                left, center, right = st.columns([1, 2, 1])
                with center:
                    with st.container(border=True):
                        st.title(emoji)

                st.write(text)


    st.divider()


    with st.container():
        col_texto, col_checklist = st.columns([2, 1])

        # COLUMNA TEXTO
        with col_texto:
            st.subheader(
                "Antes de contarte cómo lo hacemos, "
                "queremos saber si estás listo para..."
            )
            st.markdown("""
        Si respondiste que sí a estas preguntas (esperamos que sí),  
        te va a interesar lo que viene a continuación.
        """)

        # COLUMNA CHECKLIST
        with col_checklist:
            with st.container(border=True):
                st.markdown("Checklist ¿Tú marca está lista para escalar?")
                st.checkbox("Obtener todos los clientes que puedas gestionar, de forma predecible.")
                st.checkbox("Tener identificados en tiempo real los KPIs que miden el cumplimiento de tus objetivos.")
                st.checkbox("Escalar tu negocio y llegar a mas consumidores con una propuesta de valor clara.")

    st.divider()

    with st.container():
        col_text, col_btn = st.columns([4, 1])

        with col_text:
            with col_text:
                st.subheader("Servicios")
                st.markdown("""
            Creamos marcas, contenidos y ecosistemas digitales que conectan con las personas  
            correctas y sostienen el crecimiento en el tiempo
            """)

        with col_btn:
            st.button("Ver todos los servicios ->")
            
            
with st.container():
    c1, c2, c3, c4 = st.columns(4)

    items = [
        ("0️⃣1️⃣", "BRANDING", "Estrategia e identidad de marca",
         "Definimos la esencia, el posicionamiento y el sistema visual que harán que tu marca se recuerde."),
        ("0️⃣2️⃣", "WEB & ECOMMERCE", "Desarrollo de páginas web",
         "Sitios rápidos, claros y pensados para convertir visitas en leads y ventas."),
        ("0️⃣3️⃣", "MARKETING", "Contenido & publicidad digital",
         "Guiones, creatividades y campañas en Meta/Google alineadas a objetivos de negocio."),
        ("0️⃣4️⃣", "AUTOMATIZACIÓN", "Inbound & CRM",
         "Implementamos flujos, automatizaciones y seguimiento para no perder oportunidades."),
    ]

    for col, (emoji, title, subtitle, description) in zip([c1, c2, c3, c4], items):
        with col:
            # Contenedor dentro de la columna para poder apuntar con CSS
            with st.container(border=True):
                st.markdown(emoji)
                st.markdown(f"**{title}**")
                st.subheader(subtitle)
                st.markdown(description)

    st.divider()
    with st.container():  # contenedor principal
        col_left, col_right = st.columns([2, 1])  # 2 columnas

    # ===== COLUMNA IZQUIERDA =====
    with col_left:
        st.subheader("Nuestro método para hacer crecer tu ecosistema digital")
        st.markdown("""
            No hacemos campañas sueltas. Diseñamos un flujo que acompaña al usuario
            desde que descubre tu marca hasta que se convierta en cliente concurrente.
        """)

        # Lista de subtítulos y descripciones
        lista_items = [
            ("Diagnóstico y oportunidades", "Revisamos tu marca, ventas, contenido y datos actuales. Detectamos qué está frenando tu crecimiento."),
            ("Estrategia y propuesta", "Planteamos objetivos claros, KPIs y un plan accionable de contenido, pauta y tecnología."),
            ("Producción y lanzamientos", "Creamos las piezas, guiones y landings necesarias para activar tu ecosistema digital."),
            ("Medición y optimización", "Monitoreamos resultados, optimizamos campañas y ajustamos el plan constantemente."),
        ]

        numeros = ["1️⃣", "2️⃣", "3️⃣", "4️⃣"]  # números en círculos

        for num, (subtitle, text) in zip(numeros, lista_items):
            # Mostrar número al inicio del subtítulo
            st.markdown(f"{num} **{subtitle}**")
            st.markdown(text)  # texto debajo              # texto debajo

        with col_right:
            with st.container(border=True):
                st.markdown("**Embudo tipo See-Think-Do-Care**")
                # Columnas por fila, separadores entre filas
                filas_col1 = [
                    "**Damos a conocer tu marca**",
                    "**Generamos tráfico y resolvemos dudas**",
                    "**Cerramos ventas**",
                    "**Fidelizamos y generamos recomendación**"
                ]
                filas_col2 = [
                    "Social Media Ads, PR, Youtube, brand days, contenido masivo.",
                    "Reels, blogs, influencers, email campañas de interacción y remarketing.",
                    "Landing pages, anuncios de conversión, WhatsApp, llamadas y embudos fijados.",
                    "Programas de lealtad, CRM, automatizaciones, contenido post-venta."
                ]
                for texto1, texto2 in zip(filas_col1, filas_col2):
                    c1, c2 = st.columns(2)
                    c1.markdown(texto1)
                    c2.markdown(texto2)
                    st.divider()  # separador después de cada fila
    st.divider()
    with st.container():
        col_text, col_btn = st.columns([4, 1])

        with col_text:
            with col_text:
                st.subheader("Proyectos destacados")
                st.markdown("""
            Contamos historias que conectan con personas reales y convierten en resultados de
            negocio.
            """)

        with col_btn:
            st.button("Ver todos los casos ->")
    

    c1, c2, c3 = st.columns(3)

    items = [
        (
            "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?q=80&w=1170&auto=format&fit=crop&ixlib=rb-4.1.0",
            "BRANDING PERSONAL",
            "Dr.Darwin - Marca médica",
            "Posicionamiento de un especialista en salud con narrativa cercana y contenido educativo.",
            "+300% interacciones | +X consultas mensuales"
        ),
        (
            "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?q=80&w=1170&auto=format&fit=crop&ixlib=rb-4.1.0",
            "B2B INDUSTRIAL",
            "Climber World Perú",
            "Estrategia digital para una marca industrial que necesitaba visibilidad y leads calificados.",
            "Ecosistema web + contenido + paid media"
        ),
        (
            "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?q=80&w=1170&auto=format&fit=crop&ixlib=rb-4.1.0",
            "SERVICIOS B2C",
            "Clínica & estética",
            "Campañas estacionales y contenidos que conectan con deseo, confianza y resultados.",
            "Mejoras en tasa de agendamiento y recompra"
        ),
    ]

    for col, (img_path, title, subtitle, description, extra_info) in zip([c1, c2, c3], items):
        with col:
            with st.container(border=True):
                st.image(img_path, width=350)  # ancho de la imagen
                st.markdown(f"**{title}**")
                st.subheader(subtitle)
                st.markdown(description)
                st.markdown(extra_info)

    with st.container():
        
# Título
        st.subheader("Nuestros clientes")

# Texto
st.markdown("""
Marcas de salud, industria,retail y servicios que ya confían en nosotros.
""")

# Ajustamos los anchos para que los textos queden en una sola línea
b1, b2, b3, b4, b5, _ = st.columns([3, 3, 2, 4, 2, 10])  # últimos número es relleno

with b1:
    st.button("Valle del Sol")
with b2:
    st.button("Puggy Shoes")
with b3:
    st.button("CWP")
with b4:
    st.button("Cirugía Plástica")
with b5:
    st.button("+ otros")


st.divider()
    
# Título
st.subheader("Los que ya nos conocen")

# Texto
st.markdown("""
Testimonios en video y texto de marcas con las que trabjamos de la mano
""")

col1, col2, col3 = st.columns([3, 3, 3])  # videos más anchos que la columna de texto

# Primer cuadro: video más grande
with col1:
    with st.container(border=True):
        st.video("https://www.youtube.com/watch?v=iWCenGIIBVE", format="video/mp4")

# Segundo cuadro: subtítulo + texto centrado
with col2:
    with st.container(border=True):
        st.markdown("### Melissa Núñez")  # subtítulo
        st.text("Gerente de marketing")
        st.text(
            '"Ingsighters es un equipo con criterio y\n'
            'creatividad, muy enfocado en objetivos. Nos\n'
            'ayudaron a ordenar nuestra estrategia y a\n'
            'convertir mejor cada campaña."'
        )

# Tercer cuadro: video más grande
with col3:
    with st.container(border=True):
        st.video("https://www.youtube.com/watch?v=iWCenGIIBVE", format="video/mp4")

st.divider()

import streamlit as st

# Creamos fila de 3 columnas
col_left, col_center, col_right = st.columns([1, 2, 1])  # columna central más ancha

with col_center:
    # Título
    st.markdown("### Necesitas un ecosistema digital integral que responda a tus necesidades comerciales.")  

    # Texto debajo del título
    st.markdown("""
    Nosotros nos encargamos de armarlo y ejecutarlo correctamente,con un 
    plan estratégico en tu consumidor.
    """)

    # Botón debajo del texto
    st.button("Ver Servicios")

col_left, col_right = st.columns(2)

# ----- COLUMNA IZQUIERDA -----
with col_left:
    with st.container(border=True):
        
        # Título
        st.markdown("### Escríbenos")  

        # Texto normal
        st.markdown("""
        Cuéntanos brevemente sobre tu marca y lo que necesitas. Te responderemos con 
        una propuesta o una llamada exploratoria.
        """)

        # Texto en negrita
        st.markdown("**Nombre**")
        # Cuadro de texto rellenable
        nombre = st.text_input("Nombre", placeholder="Tu nombre", label_visibility="hidden")

        # Texto en negrita
        st.markdown("**Teléfono**")
        # Cuadro de texto rellenable
        telefono = st.text_input("Teléfono", placeholder="+51 ...", label_visibility="hidden")

        st.markdown("**Email**")
        # Cuadro de texto rellenable
        email = st.text_input("Email", placeholder="tucorreo@ejemplo.com", label_visibility="hidden")

        st.markdown("**Servicio de interés**")
        # Texto en negrita
        tipo_consulta = st.selectbox(
        "Seleccionar servicio",
        ["Opción 1", "Opción 2"],
        index=0,
        label_visibility="hidden")

        st.markdown("**Mensaje**")
        # Cuadro de texto rellenable
        email = st.text_area("Mensaje", placeholder="Cuéntanos un poco sobre tu negocio y objetivos", label_visibility="hidden")


# ----- COLUMNA DERECHA -----
with col_right:
    with st.container(border=True):
        # Título
        st.markdown("### Datos de contacto")

        # Texto normal
        st.markdown("Si prefieres, puedes escribirnos directamente o agendar una reunión.")

        # Texto en negrita seguido de texto normal
        st.markdown("**Correo:** hello@insighters.agency")
        st.markdown("**Télefono:** +51 999 999 999")
        st.markdown("**Ubicación:** Lima-Perú")

        # Texto normal
        st.markdown("Partners")

        # 4 botones en fila (DENTRO de col_right)
        btn1, btn2, btn3, btn4 = st.columns(4)

        with btn1:
            st.button("Salud")
        with btn2:
            st.button("Industrial")
        with btn3:
            st.button("Retail")
        with btn4:
            st.button("Educación")


st.divider()  # separador antes del footer (opcional)

# Footer con 4 columnas
col1, col2, col3, col4 = st.columns(4)

# ----- COLUMNA 1 -----
with col1:
    st.markdown("#### 🟣 Insighters")  # subtítulo
    st.markdown("""
    Agencia enfocada en estrategia, creatividad y 
    datos para marcas que quieren crecer en 
    serio.
    """)

# ----- COLUMNA 2 -----
with col2:
    st.markdown("#### Soluciones")  # subtítulo
    st.markdown("Branding")
    st.markdown("Desarrollo")
    st.markdown("Marketing Digital")
    st.markdown("Inboud / CRM ")

# ----- COLUMNA 3 -----
with col3:
    st.markdown("#### Sitio")  # subtítulo
    st.markdown("Nosotros")
    st.markdown("Proyectos")
    st.markdown("Recursos")
    st.markdown("Contacto")

# ----- COLUMNA 4 -----
with col4:
    st.markdown("#### Contacto")  # subtítulo
    st.markdown("Lima-Perú")
    st.markdown("hello@insighters.agency")
    st.markdown("+51 999 999 999")


