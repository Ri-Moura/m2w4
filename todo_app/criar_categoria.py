from todo_app import create_connection, create_table, create_category

def main():
    database = "todo_app.db"
    
    # Consulta SQL para criar a tabela de categorias
    sql_create_categories_table = """CREATE TABLE IF NOT EXISTS categories (
                                    id INTEGER PRIMARY KEY,
                                    name TEXT NOT NULL UNIQUE
                                );"""

    # Consulta SQL para criar a tabela de todos
    sql_create_todos_table = """CREATE TABLE IF NOT EXISTS todos (
                                id INTEGER PRIMARY KEY,
                                title TEXT NOT NULL,
                                description TEXT,
                                due_date TEXT NOT NULL,
                                category_id INTEGER,
                                is_done INTEGER NOT NULL DEFAULT 0,
                                FOREIGN KEY (category_id) REFERENCES categories (id)
                            );"""
    
    # Cria conexão com o DB
    conn = create_connection(database)

    # Testa a conexão, caso ela já tenha sido feita, executa as queries. Caso não, printa erro!
    if conn is not None:
        create_table(conn, sql_create_categories_table)
        create_table(conn, sql_create_todos_table)
        
        # Recebe o input do usuário
        nome_categoria = input("Digite o nome da Categoria da Tarefa: ")

        # Adiciona uma nova categoria ao banco de dados com base no input do usuário
        novo_nome_categoria = (nome_categoria)
        categoria_id = create_category(conn, novo_nome_categoria)
        print(f"Nome de Categoria criado com sucesso com o ID {categoria_id}")

    else:
        print("Error! Não foi possível conectar ao banco de dados.")

if __name__ == '__main__':
    main()