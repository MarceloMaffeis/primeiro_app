# app.py
import streamlit as st

# Configuração da página (título da aba, layout centralizado e ícone)
st.set_page_config(
    page_title="Calculadora Interativa",
    page_icon="🧮",
    layout="centered"
)

# 1. Título principal com ícone amigável
st.title("🧮 Minha Calculadora Streamlit")
st.caption("Exemplo didático de aplicação interativa rápida com Python.")

st.divider()

# 2. Entradas numéricas organizadas em colunas para uma interface mais limpa
col1, col2 = st.columns(2)

with col1:
    num1 = st.number_input(
        label="Primeiro número:",
        value=0.0,
        format="%.2f"
    )

with col2:
    num2 = st.number_input(
        label="Segundo número:",
        value=0.0,
        format="%.2f"
    )

# 3. Componente de seleção da operação aritmética
operacao = st.radio(
    label="Selecione a operação desejada:",
    options=["Soma (+)", "Subtração (-)", "Multiplicação (*)", "Divisão (/)"],
    horizontal=True
)

st.write("")  # Espaçamento sutil antes do botão

# 4. Botão de ação para disparar o cálculo
if st.button("Calcular", type="primary", use_container_width=True):
    resultado = None
    erro = None

    # Lógica de cálculo e validação
    if operacao == "Soma (+)":
        resultado = num1 + num2
    elif operacao == "Subtração (-)":
        resultado = num1 - num2
    elif operacao == "Multiplicação (*)":
        resultado = num1 * num2
    elif operacao == "Divisão (/)":
        # 5. Tratamento de divisão por zero
        if num2 == 0.0:
            erro = "Divisão por zero não é permitida! Altere o segundo número."
        else:
            resultado = num1 / num2

    st.divider()

    # Exibição dos resultados ou mensagens de erro
    if erro:
        st.error(f"⚠️ {erro}")
    else:
        st.success("Cálculo realizado com sucesso!")
        st.metric(
            label=f"Resultado da {operacao.split(' ')[0]}",
            value=f"{resultado:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        )