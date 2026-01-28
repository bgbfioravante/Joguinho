import streamlit as st
import random
import time

st.set_page_config(page_title="Joguinhos", page_icon="🎮", layout="centered")

# ---------------- ESTADOS ----------------
if "screen" not in st.session_state:
    st.session_state.screen = "home"

if "name" not in st.session_state:
    st.session_state.name = ""

if "score" not in st.session_state:
    st.session_state.score = 0

if "streak" not in st.session_state:
    st.session_state.streak = 0

if "mode" not in st.session_state:
    st.session_state.mode = "Matemática"

if "question" not in st.session_state:
    st.session_state.question = ""

if "answer" not in st.session_state:
    st.session_state.answer = 0

if "deadline" not in st.session_state:
    st.session_state.deadline = None


# ---------------- FUNÇÕES ----------------
def nova_pergunta(modo):
    if modo == "Matemática":
        a, b = random.randint(1, 20), random.randint(1, 20)
        op = random.choice(["+", "-", "x"])
        if op == "+":
            return f"{a} + {b}", a + b, None
        if op == "-":
            return f"{a} - {b}", a - b, None
        return f"{a} x {b}", a * b, None

    if modo == "Sequência":
        ini = random.randint(1, 10)
        passo = random.randint(1, 5)
        seq = [ini + i * passo for i in range(4)]
        return f"{seq[0]}, {seq[1]}, {seq[2]}, {seq[3]}, ?", seq[3] + passo, None

    if modo == "Tempo":
        a, b = random.randint(1, 15), random.randint(1, 15)
        return f"⏱ {a} + {b} (5s)", a + b, time.time() + 5


def iniciar_jogo(modo):
    st.session_state.mode = modo
    st.session_state.score = 0
    st.session_state.streak = 0
    q, a, d = nova_pergunta(modo)
    st.session_state.question = q
    st.session_state.answer = a
    st.session_state.deadline = d
    st.session_state.screen = "game"


# ---------------- TELA INICIAL ----------------
if st.session_state.screen == "home":
    st.title("🎮 Joguinhos")
    st.caption("Escolha um modo e tente fazer o máximo de pontos 😄")

    st.session_state.name = st.text_input("Nome do jogador")

    modo = st.selectbox(
        "Modo de jogo",
        ["Matemática", "Sequência", "Tempo"]
    )

    if st.button("▶️ Começar"):
        if st.session_state.name.strip() == "":
            st.error("Digite um nome para jogar")
        else:
            iniciar_jogo(modo)

# ---------------- JOGO ----------------
elif st.session_state.screen == "game":
    st.subheader(f"👤 {st.session_state.name}")
    st.write(f"🎯 Modo: {st.session_state.mode}")
    st.write(f"⭐ Pontos: {st.session_state.score} | 🔥 Combo: {st.session_state.streak}")

    if st.session_state.deadline:
        tempo = int(st.session_state.deadline - time.time())
        st.warning(f"⏳ Tempo restante: {tempo}s")
        if tempo <= 0:
            st.error("⏰ Tempo acabou!")
            st.sess
