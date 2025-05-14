from data.cliente_model import Cliente
from data.cliente_sql import *
from data.util import get_connection

def criar_tabela():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(CRIAR_TABELA)
    conn.commit()
    conn.close()

def inserir(cliente: Cliente):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(INSERIR, (
        cliente.nome, 
        cliente.cpf, 
        cliente.email, 
        cliente.telefone, 
        cliente.senha))
    conn.commit()
    conn.close()

def obter_todos() -> list[Cliente]:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(OBTER_TODOS)
    tuplas = cursor.fetchall()
    clientes = [
        Cliente(
            id=tupla[0], 
            nome=tupla[1], 
            cpf=tupla[2],
            email=tupla[3],
            telefone=tupla[4],
            senha=tupla[5]) 
            for tupla in tuplas]
    conn.close()
    return clientes