import streamlit as st

import base64

# Função para converter imagem para base64
def get_base64_of_image(path):
    with open(path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Converte imagem de asfalto para base64
asfalto_base64 = get_base64_of_image("textura_asfalto.jpg")

# Layout da página
st.set_page_config(page_title="Trânsito na Via 9", layout="wide")

# CSS com fundo de asfalto + texto branco com sombra
st.markdown(f"""
    <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{asfalto_base64}");
            background-size: cover;
            background-attachment: fixed;
            background-position: center;
        }}
        h1, h2, h3, h4, h5, h6, p, div, span {{
            color: white !important;
            text-shadow: 1px 1px 3px black;
        }}
        audio {{
            margin-bottom: 2rem;
        }}
    </style>
""", unsafe_allow_html=True)

     
# Áudio ambiente
st.audio("150efeitosonorodetrnsitonacidadecombuzinasepessoas.mp3", loop=True)

# Conteúdo principal
st.title("🚦 Obra mal planejada trava o trânsito na Via 9, no Recreio")
st.subheader("Rotatória e radar de 40km/h colocados no fim da Avenida Balthazar da Silveira estão causando engarrafamentos diários nos horários de pico.")
st.markdown("---")

st.header("🧭 Contexto")
st.write("""
A rotina de quem passa pela Avenida Balthazar da Silveira, mais conhecida como Via 9, ficou bem mais complicada. 
Uma obra feita pela Prefeitura no fim da via, com a instalação de uma rotatória e um radar de 40km/h para dar acesso ao Terminal de BRT do Recreio, 
tem causado longos congestionamentos nos horários de maior movimento.
""")

st.header("🎥 O trânsito na prática")
st.video("https://www.youtube.com/watch?v=nRz0HaSwQ_M")
st.video("https://www.youtube.com/watch?v=hedAndSmwdk")

st.header("📍 Onde fica esse trecho?")
st.image("mapa_recreio_geral.png", caption="🗺️ Mapa geral do Recreio dos Bandeirantes", use_container_width=True)
st.image("mapa_balthazar1.png", caption="📌 Trecho da Av. Balthazar da Silveira próximo à Salvador Allende", use_container_width=True)
st.image("mapa_balthazar2.png", caption="📍 Rotatória no fim da Via 9 próxima ao Terminal Recreio", use_container_width=True)

st.header("🚗 O impacto no dia a dia")
st.write("""
A Via 9 é uma das principais entradas e saídas do Recreio dos Bandeirantes. Quem mora ou trabalha na região costuma passar por ali todos os dias. 
O problema é que, desde 2015, quando a Prefeitura iniciou a obra do Terminal de BRT do Recreio, o trânsito na região piorou visivelmente.

Para acessar o terminal, foi construída uma rotatória no fim da avenida, junto com a instalação de um radar de 40 km/h. 
O motorista precisa frear para o radar e, em seguida, esperar sua vez para entrar na rotatória, onde a preferência nem sempre parece lógica. 
Do outro lado, quem vem da Avenida Salvador Allende encontra uma placa de “PARE” — mas essa via raramente tem congestionamento.

Conversei com **Inácio Soares**, um amigo que trabalha como motorista de aplicativo e conhece bem o local. Ele compartilhou suas impressões:
""")
st.markdown("> “Muita gente fica parada por vários minutos sem necessidade. A gente já reduz a velocidade por causa do radar, aí tem que esperar ainda mais. Enquanto isso, quase não vem carro da outra pista.” – Inácio Soares")

st.header("🎙️ Entrevista com Inácio Soares")
st.write("""
**Você costuma passar por aqui todos os dias?**  
Sim. Trabalho com transporte de passageiros há mais de cinco anos e essa é uma das rotas mais comuns pra mim. Antes da obra, até havia um fluxo, mas nada comparado ao que é hoje.

**O que mudou, na sua opinião, depois da instalação do radar e da rotatória?**  
A principal mudança foi a lentidão. O radar já faz a gente frear bastante. Mas o problema é o fluxo grande de carros e a rotatória mal planejada. Você tem que parar mesmo quando o carro vai entrar na entrada antes, só porque o pessoal não dá a seta vindo e ferra tudo.

**Já houve alguma situação crítica por aqui?**  
Sim, já vi carro quase bater porque o motorista perde a paciência e tenta entrar de qualquer jeito. É um estresse desnecessário.
""")

st.header("📊 Dados e preocupações dos moradores")
st.write("""
Segundo a Prefeitura do Rio, a cidade possui hoje 979 radares de velocidade — mais até que São Paulo. 
Um deles está posicionado justamente na saída da Via 9, obrigando os motoristas a desacelerarem logo antes da rotatória.

A instalação da rotatória e do radar foi feita como parte do projeto do Terminal Recreio, 
que integra o corredor BRT TransOlímpica. Desde o início da obra, moradores manifestaram preocupação com o impacto no trânsito da região. 
Reportagem do jornal O Globo, ainda em 2015, mostrou que muitos já antecipavam que a obra traria mais confusão do que solução.

Um relatório técnico do ITDP Brasil também apontou falhas na integração e acessibilidade do Terminal, além de impacto negativo na fluidez das vias próximas.
""")

st.header("💡 O que poderia ser feito?")
st.write("""
Sugestões dos moradores incluem revisar a lógica da rotatória — talvez invertendo a prioridade — 
e substituir o radar por outro tipo de controle de velocidade mais compatível com o fluxo. 
O objetivo é garantir mais fluidez sem comprometer a segurança viária.

As entrevistas, vídeos e registros feitos durante este trabalho mostram claramente como a obra gerou efeitos inesperados no dia a dia da população.
""")

st.markdown("---")
st.markdown("📝 Matéria multimídia produzida por **Bruno Alexandre Rodrigues** — estudante de Comunicação Digital, na disciplina Jornalismo Digital 2025.1")
