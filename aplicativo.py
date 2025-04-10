# Gerar o aplicativo.py final com:
# - Fundo de asfalto
# - Texto claro
# - Estilo translúcido para legibilidade
# - Entrevista e matéria completa
# - Áudio ambiente em autoplay

# Inserir o base64 do áudio no HTML do autoplay
audio_html_final = f"""
<audio autoplay loop>
    <source src="data:audio/mp3;base64,{audio_base64_final}" type="audio/mp3">
</audio>
"""

# Criar o conteúdo completo do aplicativo.py
app_final = f"""
import streamlit as st

st.set_page_config(page_title="Trânsito na Via 9", layout="wide")

# Estilo visual: fundo de asfalto e texto claro
st.markdown(\"\"\"
    <style>
        body {{
            background-image: url('https://i.imgur.com/IiK6p0z.jpg');
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
            background-position: center;
        }}
        h1, h2, h3, h4, h5, h6, p, div, span {{
            color: #f1f1f1 !important;
        }}
        .reportview-container .main {{
            background-color: rgba(0, 0, 0, 0.7);
            padding: 1.5rem;
            border-radius: 10px;
        }}
    </style>
\"\"\", unsafe_allow_html=True)

# Áudio ambiente com autoplay e loop
st.markdown(\"\"\"{audio_html_final}\"\"\", unsafe_allow_html=True)

st.markdown("## 🚦 Obra mal planejada trava o trânsito na Via 9, no Recreio")
st.markdown("#### Rotatória e radar de 40km/h colocados no fim da Avenida Balthazar da Silveira estão causando engarrafamentos diários nos horários de pico.")
st.markdown("---")

st.markdown("### 🧭 Contexto")
st.write(\"""
A rotina de quem passa pela Avenida Balthazar da Silveira, mais conhecida como Via 9, ficou bem mais complicada. 
Uma obra feita pela Prefeitura no fim da via, com a instalação de uma rotatória e um radar de 40km/h para dar acesso ao Terminal de BRT do Recreio, 
tem causado longos congestionamentos nos horários de maior movimento.
\""")

st.markdown("### 🎥 O trânsito na prática")
st.video("https://www.youtube.com/watch?v=nRz0HaSwQ_M")
st.video("https://www.youtube.com/watch?v=hedAndSmwdk")

st.markdown("### 📍 Onde fica esse trecho?")
st.image('mapa_recreio_geral.png', caption='🗺️ Mapa geral do Recreio dos Bandeirantes', use_container_width=True)
st.image('mapa_balthazar1.png', caption='📌 Trecho da Av. Balthazar da Silveira próximo à Salvador Allende', use_container_width=True)
st.image('mapa_balthazar2.png', caption='📍 Rotatória no fim da Via 9 próxima ao Terminal Recreio', use_container_width=True)

st.markdown("### 🚗 O impacto no dia a dia")

st.write(\"""
A Via 9 é uma das principais entradas e saídas do Recreio dos Bandeirantes. Quem mora ou trabalha na região costuma passar por ali todos os dias. 
O problema é que, desde 2015, quando a Prefeitura iniciou a obra do Terminal de BRT do Recreio, o trânsito na região piorou visivelmente.

Para acessar o terminal, foi construída uma rotatória no fim da avenida, junto com a instalação de um radar de 40 km/h. 
O motorista precisa frear para o radar e, em seguida, esperar sua vez para entrar na rotatória, onde a preferência nem sempre parece lógica. 
Do outro lado, quem vem da Avenida Salvador Allende encontra uma placa de “PARE” — mas essa via raramente tem congestionamento.

Conversei com **Inácio Soares**, um amigo que trabalha como motorista de aplicativo e conhece bem o local. Ele compartilhou suas impressões:
\""")

st.markdown("> “Muita gente fica parada por vários minutos sem necessidade. A gente já reduz a velocidade por causa do radar, aí tem que esperar ainda mais. Enquanto isso, quase não vem carro da outra pista.” – Inácio Soares, motorista de aplicativo")

st.markdown("### 🎙️ Entrevista com Inácio Soares")

st.write(\"""
**Você costuma passar por aqui todos os dias?**  
Sim. Trabalho com transporte de passageiros há mais de cinco anos e essa é uma das rotas mais comuns pra mim. Antes da obra, até havia um fluxo, mas nada comparado ao que é hoje.

**O que mudou, na sua opinião, depois da instalação do radar e da rotatória?**  
A principal mudança foi a lentidão. O radar já faz a gente frear bastante. Mas o problema é o fluxo grande de carros e o rotatória mal planejada. Você tem que parar mesmo quando o carro vai entrar na entrada antes, só porque o pessoal não dá a seta vindo e ferra tudo.

**Já houve alguma situação crítica por aqui?**  
Sim, já vi carro quase bater porque o motorista perde a paciência e tenta entrar de qualquer jeito. É um estresse desnecessário.
\""")

st.markdown("### 📊 Dados e preocupações dos moradores")

st.write(\"""
Segundo a Prefeitura do Rio, a cidade possui hoje 979 radares de velocidade — mais até que São Paulo. 
Um deles está posicionado justamente na saída da Via 9, obrigando os motoristas a desacelerarem logo antes da rotatória.

A instalação da rotatória e do radar foi feita como parte do projeto do Terminal Recreio, 
que integra o corredor BRT TransOlímpica. Desde o início da obra, moradores manifestaram preocupação com o impacto no trânsito da região. 
Reportagem do jornal O Globo, ainda em 2015, mostrou que muitos já antecipavam que a obra traria mais confusão do que solução.

Um relatório técnico do ITDP Brasil também apontou falhas na integração e acessibilidade do Terminal, além de impacto negativo na fluidez das vias próximas.
\""")

st.markdown("### 💡 O que poderia ser feito?")

st.write(\"""
Sugestões dos moradores incluem revisar a lógica da rotatória — talvez invertendo a prioridade — 
e substituir o radar por outro tipo de controle de velocidade mais compatível com o fluxo. 
O objetivo é garantir mais fluidez sem comprometer a segurança viária.

As entrevistas, vídeos e registros feitos durante este trabalho mostram claramente como a obra gerou efeitos inesperados no dia a dia da população.
\""")

st.markdown("---")
st.markdown("📝 Matéria multimídia produzida por **Bruno Alexandre Rodrigues** — estudante de Comunicação Digital, na disciplina Jornalismo Digital 2025.1")
"""

# Salvar o aplicativo final no arquivo
with open("/mnt/data/aplicativo.py", "w", encoding="utf-8") as f:
    f.write(app_final)

"/mnt/data/aplicativo.py"
