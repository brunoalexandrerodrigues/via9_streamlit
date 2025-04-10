import streamlit as st

st.set_page_config(page_title="Trânsito na Via 9", layout="wide")

st.markdown("<h1 style='text-align: center;'>Caos na Via 9: como uma obra transformou o trânsito no Recreio</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Radar, rotatória e sinalização confusa geram congestionamentos todos os dias</h4>", unsafe_allow_html=True)

#st.audio('sons_transito_final.mp3', format='audio/mp3', start_time=0)

st.markdown("### O que está acontecendo?")
st.write("""
A Avenida Balthazar da Silveira, a famosa Via 9, é uma das principais rotas de entrada e saída do Recreio dos Bandeirantes. 
Uma obra recente da prefeitura colocou uma rotatória e um radar de 40km/h no final da via, e desde então o trânsito virou um problema sério.
""")

st.markdown("### Veja como está o trânsito de verdade")
st.write("Gravamos dois vídeos para mostrar como o trânsito trava na Via 9:")
st.video("https://www.youtube.com/watch?v=nRz0HaSwQ_M")
st.video("https://www.youtube.com/watch?v=hedAndSmwdk")

st.markdown("### Onde fica esse trecho?")
st.image('mapa_recreio_geral.png', caption='Mapa geral do Recreio dos Bandeirantes', use_container_width=True)
st.image('mapa_balthazar1.png', caption='Avenida Alfredo Balthazar da Silveira e acesso à Salvador Allende', use_container_width=True)
st.image('mapa_balthazar2.png', caption='Rotatória no fim da Via 9 próxima ao Terminal Recreio', use_container_width=True)


st.markdown("### Fiscalização intensa e fluxo parado")
st.write("""
Segundo dados da Prefeitura do Rio, a cidade tem 979 radares de velocidade — mais até que São Paulo. 
Um deles está instalado bem no fim da Avenida Balthazar da Silveira, com limite de 40 km/h. 
Quem passa ali precisa frear, o que já começa a travar o trânsito. E logo em seguida, ainda precisa esperar a vez na rotatória.

Do outro lado da rotatória, tem uma placa de 'PARE' para não travar o fluxo da Avenida Salvador Allende. 
Mas a Allende quase não tem engarrafamento, então essa preferência acaba prejudicando todo mundo que vem da Via 9.
""")

st.markdown("> “A gente para por causa do radar e depois fica esperando à toa. O outro lado mal tem carro.” — André Luiz, motorista de aplicativo")

st.markdown("### E agora?")
st.write("""
Moradores pedem uma reavaliação da sinalização e da lógica de prioridade na rotatória. 
Uma simples troca no lado que tem a placa de 'PARE' já poderia melhorar bastante a fluidez no local.

A equipe deste projeto está acompanhando a situação e busca ampliar o debate sobre a mobilidade urbana no bairro. 
""")

st.markdown("---")
st.markdown("**Matéria multimídia feita por estudante da disciplina de Jornalismo Multimídia - Bruno Alexandre Rodrigues**")
