from todo_app import create_connection, create_table, create_todo

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
        title = input("Digite o título do TODO: ")
        description = input("Digite a descrição do TODO (pressione Enter se não houver descrição): ")
        due_date = input("Digite a data de vencimento do TODO (formato: AAAA-MM-DD): ")

        # Adiciona um novo TODO ao banco de dados com base no input do usuário
        new_todo = (title, description, due_date, None, 0)
        todo_id = create_todo(conn, new_todo)
        print(f"TODO criado com sucesso com o ID {todo_id}")

    else:
        print("Error! Não foi possível conectar ao banco de dados.")

if __name__ == '__main__':
    main()