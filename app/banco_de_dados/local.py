from contextlib import contextmanager
import sqlite3


class BancoDeDadosLocal:

    def __init__(self, nome_arquivo="techlog.db"):
        self.nome_arquivo = nome_arquivo

    @contextmanager
    def conectar(self):
        conexao = sqlite3.connect(self.nome_arquivo)
        try:
            yield conexao
            conexao.commit()
        except Exception as e:
            conexao.rollback()
            raise e
        finally:
            conexao.close()

    def inicializar_banco(self):
        with self.conectar() as conexao:
            cursor = conexao.cursor()

            # Tabela de clientes
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS clientes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    email TEXT NOT NULL,
                    telefone TEXT NOT NULL
                )
            """)

            # Tabela de usuarios
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS usuarios (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    senha TEXT NOT NULL
                )
            """)

            print("Banco de dados inicializado com sucesso!")