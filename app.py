import streamlit as st
from funcoes import import_user, salvar_tar, c_tar, fil_tar_p_user

st.title("Sistema de Tarefas")
st.sidebar.title("Menu")

menu = st.sidebar.radio("selecione:", ["Adicionar tarefa", "Visualizar tarefas"])

user = import_user()

if menu == "Adicionar tarefa":
    st.header("adicionar nova tarefa")

    if user:
        user = st.selectbox("Usuário", user)
        descricao = st.text_input("Descrição da tarefa")
        prioridade = st.selectbox("Prioridade", ["Alta", "Média", "Baixa"])

        if st.button("Salvar"):
            if descricao.strip():
                salvar_tar(user, descricao, prioridade)
                st.success("Tarefa salva com sucesso!")
            else:
                st.warning("Por favor, preencha a descrição da tarefa.")
    else:
        st.error("Nenhum usuário encontrado. Adicione usuários no arquivo 'usuarios.txt'.")

elif menu == "Visualizar tarefas":
    st.header("Visualizar tarefas por usuário")

    if user:
        user = st.selectbox("Escolha o usuário", user)
        tar = c_tar()
        tar_user = fil_tar_p_user(tar, user)

        prioridades = {"Alta": [], "Média": [], "Baixa": []}
        for t in tar_user:
            prioridades[t["prioridade"]].append(t["descricao"])

        for prioridade, lista in prioridades.items():
            st.subheader(f"Tarefas de prioridade {prioridade}")
            if lista:
                for tar in lista:
                    st.write(f"• {tar}")
            else:
                st.write("Nenhuma tarefa.")
    else:
        st.error("Nenhum usuário disponível para visualização.")


def salvar_tar(user, descricao, prioridade, caminho="tar.txt"):
    with open(caminho, "a") as f:
        f.write(f"{user}|{descricao}|{prioridade}\n")
