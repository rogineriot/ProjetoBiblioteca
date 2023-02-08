import psycopg2
from classConexao import Conexao
from classCliente import Cliente
from classLivro import Livro
# def criarBancoDeDados(conexao):
#     conexao.manipularBanco('''
#     DROP DATABASE IF EXISTS "Biblioteca" ;
#     CREATE DATABASE "Biblioteca";
#     ''')

# def criarTabelaCliente(conexao):
#     conexao.manipularBanco('''
#     DROP TABLE IF EXISTS "Cliente";
#     CREATE TABLE "Cliente"(
#         "ID" int GENERATED ALWAYS AS IDENTITY,
#         "Nome" varchar(255) NOT NULL,
#         "CPF" char(11) NOT NULL UNIQUE,
#         Primary Key("ID")
#     );
#     ''')

# def criarTabelaLivro(conexao):

#     conexao.manipularBanco('''
#     DROP TABLE IF EXISTS "Livro";
#     CREATE TABLE "Livro(
#         "ID" int GENERATED ALWAYS AS IDENTITY,
#         "Nome" varchar(255) NOT NULL,
#         "Autor" varchar(255) NOT NULL,
#         Primary Key("ID")
#     );
#     ''')

# def criarTabelaAluguel(conexao):

#     conexao.manipularBanco('''
#     DROP TABLE IF EXISTS "Aluguel";
#     CREATE TABLE "Aluguel"(
#         "ID" int GENERATED ALWAYS AS IDENTITY,
#         "ID_Cliente" int NOT NULL,
#         "ID_Livro" int NOT NULL,
#         "Data_Aluguel" timestamp default current_timestamp,
#         Primary Key("ID"),
#         Constraint fk_cliente
#             Foreign Key ("ID_Cliente")
#             References "Cliente"("ID")
#             ON DELETE CASCADE
#             ON UPDATE NO ACTION
#             ,
#         Constraint fk_livro
#             Foreign Key ("ID_Livro")
#             References "Livro"("ID")
#             ON DELETE SET NULL
#             ON UPDATE NO ACTION
            
#     );
#     ''')

def query(tabela, id):
      
      resultado = (f'''
            SELECT * FROM "{tabela}"
            where "ID" = '{id}'
            ''')
      
      return resultado
      
      
def mostrarClientes(conexao):
  listaClientes = conexao.consultarBanco('''
                                         select * from "Cliente"
                                         
                                         ''')
  for cliente in listaClientes:
    print(f'''
          ID  - {cliente[0]}
          Nome  - {cliente[1]}
          ''')
def mostrarLivros(conexao):
      listaLivros = conexao.consultarBanco('''
                                         select * from "Livro"
                                         
                                         ''')
      for livro in listaLivros:
            print(f'''
                  ID  - {livro[0]}
                  Nome  - {livro[1]}
                  ''')

   
  
try:
      
      login = "postgres"
      password = "postgre"
      con = Conexao("Biblioteca","localhost","5432",login,password)
      print("Conectado")

      opcao = 1
      while opcao != 0 :   
            print(f'''
            Escolha uma das opções:
            1. Ver cliente específico
            2. Inserir novo cliente
            3. Atualizar cliente
            4. Deletar cliente
            5. Ver Livro específico
            6. Inserir novo livro
            7 .Atualizar livro
            8 .Deletar Livro
            0. Voltar para o menu principal
            ''')
            
            opcao = int(input("Digite o que você quer fazer:  "))
            
            match opcao:
                  case 1:
                        condicao = True
                        while condicao: 
                              mostrarClientes(con)
                              id_cliente = int(input("Digite o Id do cliente que quer visualizar: "))
                              resultado =  con.consultarBanco(query("Cliente", id_cliente))
                              if resultado != []:
                                    novoCliente = Cliente(resultado[0][0],resultado[0][1],resultado[0][2])
                                    novoCliente.imprimirCliente()
                                    condicao = False
                              else:
                                    print("Id digitado não existe,digite novamente")      
                                     
                  case 2: 
                        nome = input("Digite o nome do novo cliente: ")
                        cpf = input("Digite o Cpf do novo cliente: ")
                        novoCliente = Cliente(None,nome,cpf)
                        con.manipularBanco(novoCliente.inserirCliente())
                        print("Cliente Adicionado com sucesso!") 
                  case 3:
                        mostrarClientes(con)
                        condicao2 = True
                        while condicao2:
                              idClienteAtual = int(input("Digite o Id do cliente que quer atualizar: "))
                              resultadoAtualizar =  con.consultarBanco(query("Cliente",idClienteAtual))
                              if resultadoAtualizar != []:
                                    novoClienteAtualizar = Cliente(resultadoAtualizar[0][0],resultadoAtualizar[0][1],resultadoAtualizar[0][2])
                                    escolhaCampo = int(input("""Digite o campo que deseja atualizar: 
                                                      1 - Nome
                                                      2 - CPF
                                                      3 - Atulizar Nome E Cpf
                                                      
                                                      """))
                                    match escolhaCampo:
                                          case 1 :
                                                novoClienteAtualizar._nome = input("Digite o novo Nome: ")
                                                con.manipularBanco(novoClienteAtualizar.atualizarCliente()) 
                                                print("Atualizado com sucesso!") 
                                                condicao2 = False
                                          case 2 :
                                                novoClienteAtualizar._cpf = input("Digite o novo Cpf: ")
                                                con.manipularBanco(novoClienteAtualizar.atualizarCliente())
                                                print("Atualizado com sucesso!")
                                                condicao2 = False
                                          case 3 :
                                                novoClienteAtualizar._nome = input("Digite o novo Nome: ")  
                                                novoClienteAtualizar._cpf = input("Digite o novo Cpf: ")  
                                                con.manipularBanco(novoClienteAtualizar.atualizarCliente()) 
                                                print("Atualizado com sucesso!")  
                                                condicao2 = False 
                              else:
                                    print("Id digitado não existe,digite novamente")                      
                  case 4:
                        mostrarClientes(con)
                        condicao3 = True
                        while condicao3: 
                              idClienteDeletado = int(input("Digite o Cliente que deseja deletar: "))
                              resultadoDeletar =  con.consultarBanco(query("Cliente", idClienteDeletado))
                              if resultadoDeletar != []:
                                    novoClienteDeletado = Cliente(resultadoDeletar[0][0],resultadoDeletar[0][1],resultadoDeletar[0][2])
                                    con.manipularBanco(novoClienteDeletado.deletarCliente())
                                    print("Cliente deletado com sucesso!")
                                    condicao3 = False
                              else:
                                    print("Id digitado não existe,digite novamente")      
                  case 5:
                        mostrarLivros(con)
                        condicao4 = True
                        while condicao4: 
                              idLivro = int(input("Digite o id do livro que deseja visualizar: "))
                              livroConsultado =  con.consultarBanco(query("Livro",idLivro))
                              if livroConsultado != []:
                                    novoLivro = Livro(livroConsultado[0][0],livroConsultado[0][1],livroConsultado[0][2])
                                    novoLivro.imprimirLivro() 
                                    condicao4 = False
                              else:
                                    print("Id digitado não existe,digite novamente")    
                  case 6: 
                        novoNome = input("Digite o nome do novo Livro: ")
                        novoAutor = input("Digite o nome do autor do novo livro: ")
                        novoLivro = Livro(None,novoNome,novoAutor)
                        con.manipularBanco(novoLivro.inserirLivro())
                        print("Livro Adicionado com sucesso!")                             
                  case 7 :
                        mostrarLivros(con)
                        condicao5 = True
                        while condicao5: 
                              idLivroAtual = int(input("Digite o Id do livro que quer atualizar: "))
                              resultadoAtualizarLivro =  con.consultarBanco(query("Livro",idLivroAtual))
                              if resultadoAtualizarLivro != []:
                                    novoLivroAtualizado = Livro(resultadoAtualizarLivro[0][0],resultadoAtualizarLivro[0][1],resultadoAtualizarLivro[0][2])
                                    escolhaCampo = int(input("""Digite o campo que deseja atualizar: 
                                                      1 - Nome
                                                      2 - Autor
                                                      3 - Atulizar Nome E Autor
                                                      
                                                      """))
                                    match escolhaCampo:
                                          case 1 :
                                                novoLivroAtualizado._nome = input("Digite o nome do novo livro: ")
                                                con.manipularBanco(novoLivroAtualizado.atualizarLivro()) 
                                                print("Atualizado com sucesso!") 
                                                condicao5 = False
                                          case 2 :
                                                novoLivroAtualizado._autor = input("Digite o novo nome do autor: ")
                                                con.manipularBanco(novoLivroAtualizado.atualizarLivro())
                                                print("Atualizado com sucesso!")
                                                condicao5 = False
                                          case 3 :
                                                novoLivroAtualizado._nome = input("Digite o nome do novo livro: ")  
                                                novoLivroAtualizado._autor = input("Digite o novo nome do autor: ")  
                                                con.manipularBanco(novoLivroAtualizado.atualizarLivro()) 
                                                print("Atualizado com sucesso!") 
                                                condicao5 = False
                              else:
                                    print("Id digitado não existe,digite novamente")    
                                                      
                  case 8:
                        mostrarLivros(con)
                        condicao6 = True
                        while condicao6:
                              idLivroDeletado = int(input("Digite o id do livro que deseja deletar: "))
                              resultadoDeletarLivro =  con.consultarBanco(query("Livro",idLivroDeletado))
                              if resultadoDeletarLivro != []:
                                    novoLivroDeletado = Livro(resultadoDeletarLivro[0][0],resultadoDeletarLivro[0][1],resultadoDeletarLivro[0][2])
                                    con.manipularBanco(novoLivroDeletado.deletarLivro())
                                    print("Livro deletado com sucesso!")
                                    condicao6 = False
                              else:
                                    print("Id digitado não existe,digite novamente")  
                                          
                              
                  
                  
                        
                      
      
      
      
      
      
      
      
      
except(Exception, psycopg2.Error) as error:
        print("Ocorreu um erro -", error)
        

