CRIAR_TABELA = """
CREATE TABLE IF NOT EXISTS categoria (
id INTEGER PRIMARY KEY AUTOINCREMENT,
nome TEXT NOT NULL)
"""

INSERIR = """
INSERT INTO categoria (nome) 
VALUES (?)
"""

OBTER_TODOS = """
SELECT 
id, nome
FROM categoria
ORDER BY nome
""" 