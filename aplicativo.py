import streamlit as st

st.set_page_config(page_title="Trânsito na Via 9", layout="wide")

st.markdown("""
    <style>
        .centered {
            text-align: center;
        }
        .highlight {
            background-color: #f9f9f9;
            padding: 20px;
            border-left: 5px solid #f63366;
            border-radius: 5px;
            margin-bottom: 20px;
        }
        .quote {
            font-style: italic;
            color: #555;
            border-left: 4px solid #ccc;
            padding-left: 10px;
            margin: 20px 0;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='centered'>🚦 Trânsito travado na Via 9</h1>", unsafe_allow_html=True)
st.markdown("<h4 class='centered'>Radar, rotatória e sinalização confusa travam o bairro do Recreio nos horários de pico</h4>", unsafe_allow_html=True)

st.markdown("---")

# st.audio() está desativado para evitar erro
# st.audio('sons_transito_final.mp3', format='audio/mp3', start_time=0)

st.markdown("### 📍 O que está acontecendo?")
st.markdown("""
<div class='highlight'>
A Avenida Balthazar da Silveira, conhecida como Via 9, é uma das principais saídas e entradas do bairro do Recreio dos Bandeirantes. 
Mas uma obra recente — com a instalação de uma rotatória e um radar de 40km/h — vem transformando a rotina dos motoristas.
</div>
""", unsafe_allow_html=True)

st.markdown("### 🎥 O trânsito na prática")
st.markdown("Veja abaixo dois vídeos gravados durante horários de pico na Via 9:")

st.video("https://www.youtube.com/watch?v=nRz0HaSwQ_M")
st.video("https://www.youtube.com/watch?v=hedAndSmwdk")

st.markdown("### 🗺️ Onde fica esse trecho?")
st.markdown("Abaixo estão os mapas para visualizar melhor a região impactada pela obra:")

st.image('mapa_recreio_geral.png', caption='🗺️ Mapa geral do Recreio dos Bandeirantes', use_container_width=True)
st.image('mapa_balthazar1.png', caption='📌 Trecho da Av. Balthazar da Silveira próximo à Salvador Allende', use_container_width=True)
st.image('mapa_balthazar2.png', caption='📍 Rotatória no fim da Via 9, em frente ao Terminal Recreio BRT', use_container_width=True)

st.markdown("### 🚔 Fiscalização demais, fluidez de menos")
st.markdown("""
<div class='highlight'>
O Rio de Janeiro tem hoje mais radares do que São Paulo: são 979 equipamentos. Um deles está bem no fim da Via 9, forçando os motoristas a reduzirem bruscamente. 
Logo depois, ainda precisam esperar para entrar na rotatória — onde a preferência nem sempre faz sentido.
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='quote'>
“A gente para por causa do radar e depois fica esperando à toa. O outro lado mal tem carro.”
<br>— André Luiz, motorista de aplicativo
</div>
""", unsafe_allow_html=True)

st.markdown("### 💡 O que poderia ser feito?")
st.write("""
A preferência atual da rotatória considera o fluxo da Avenida Salvador Allende, que raramente congestiona. 
Moradores sugerem inverter a prioridade ou tirar a placa de “PARE” do lado errado da rotatória, para melhorar a fluidez de quem vem pela Via 9.

Além disso, a presença de um radar tão próximo à rotatória poderia ser repensada — talvez substituído por outro tipo de controle de velocidade mais inteligente.
""")

st.markdown("---")
st.markdown("📚 **Matéria multimídia feita por estudantes de Jornalismo Multimídia — Bruno Alexandre Rodrigues**")

