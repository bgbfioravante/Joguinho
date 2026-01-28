import streamlit as st
import random
import time

st.set_page_config(page_title="Joguinhos do Bruno", page_icon="🎮")

if "screen" not in st.session_state:
    st.session_state.screen = "home"
if "name" not in st.session_state:
    st.session_state.name = ""
if "score" not in st.session_state:
    st.session_state.score = 0

def nova_pergunta():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    return f"{a} + {b}", a + b

def iniciar_jogo():
    st.session_state.score = 0
    st.session_state.pergunta, st.session_state.resposta = nova_pergunta()
    st.session_state.screen = "game"

def finalizar():
    st.session_state.screen = "fim"

st.title("🎮 Joguinhos do Bruno")

if st.session_state.screen == "home":
    st.subheader("Tela inicial")
    nome = st.text_input("Digite seu nome")

    if st.button("Começar"):
        if nome.strip() == "":
            st.error("Digite um nome")
        else:
            st.session_state.name = nome
            iniciar_jogo()

elif st.session_state.screen == "game":
    st.write(f"Jogador: **{st.session_state.name}**")
    st.write(f"Pontos: **{st.session_state.score}**")
    st.markdown(f"### ❓ {st.session_state.pergunta}")

    resposta = st.text_input("Resposta")

    if st.button("Confirmar"):
        if resposta.isdigit() and int(resposta) == st.session_state.resposta:
            st.success("Acertou!")
            st.session_state.score += 10
            st.session_state.pergunta, st.session_state.resposta = nova_pergunta()
        else:
            st.error("Errou 😢")
            finalizar()

elif st.session_state.screen == "fim":
    st.subheader("Fim de jogo")
    st.write(f"Jogador: **{st.session_state.name}**")
    st.write(f"Pontuação final: **{st.session_state.score}**")

    if st.button("Jogar novamente"):
        st.session_state.screen = "home"
