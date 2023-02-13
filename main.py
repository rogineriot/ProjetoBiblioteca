import psycopg2
from Controle.classConexao import Conexao
from Modelo.classCliente import Cliente
from Modelo.classLivro import Livro

def query(tabela, id):
      
      resultado = (f'''
            SELECT * FROM "{tabela}"
            where "ID" = '{id}'
            ''')
      
      return resultado
     
#Função para mostrar Clientes     
def mostrarClientes(conexao):
  listaClientes = conexao.consultarBanco('''
                                         select * from "Cliente"
                                         ORDER BY "ID" ASC
                                         
                                         ''')
  for cliente in listaClientes:
    print(f'''
          ID  - {cliente[0]}
          Nome  - {cliente[1]}
          ''')
#Função para mostrar Livros
def mostrarLivros(conexao):
      listaLivros = con.consultarBanco('''
                Select * FROM "Livro"
                ORDER BY "ID" ASC
                ''')
      print("ID | Nome")
      for livro in listaLivros:
                    print(f"{livro[0]} | {livro[1]}")
                    
#Função para mostrar alugueis
def mostrarAlugueis(conexao):
    resultado = conexao.consultarBanco('''
    Select * FROM "Aluguel"
    ORDER BY "ID" ASC
    ''')
    print("ID | Cliente | Livro | Data ")
    for aluguel in resultado:

        cliente = Cliente(aluguel[1], None, None)
        clienteDoAluguel = conexao.consultarBanco(cliente.consultarClientePorID())[0]
        cliente._nome = clienteDoAluguel[1]
        cliente._cpf = clienteDoAluguel[2]

        livro = Livro(aluguel[2], None, None)
        livroDoAluguel = conexao.consultarBanco(livro.consultarLivroPorID())[0]
        livro._nome = livroDoAluguel[1]
        livro._autor = livroDoAluguel[2]
        
        print(f"{aluguel[0]} | {cliente._nome} | {livro._nome} | {aluguel[3]}")                    

   
  
try:
 #Login ddo banco de dados     
 login = "postgres"
 password = "postgre"
 con = Conexao("Biblioteca","localhost","5432",login,password)


 opcao = 1
 while opcao != 0 :   
  #Menu principal         
  print(f'''
      1 - Cliente
      2 - Livro
      3 - Alugueis
      0 - Sair do programa
      ''')
  opcao = int(input("Digite o que você quer fazer:  "))
           
  match opcao :
      case 1:
            opcaoCliente = 1
            while opcaoCliente != 0:
                  print('''
                        Escolha uma das opções:
                        1. Ver cliente específico
                        2. Inserir novo cliente
                        3. Atualizar cliente
                        4. Deletar cliente
                        0. Voltar para o menu principal
                        ''')
                  opcaoCliente = int(input("Digite o que deseja fazer: "))
                  match opcaoCliente:
                        #visualizar cliente específico
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
                              #inserir novo cliente 
                              nome = input("Digite o nome do novo cliente: ")
                              cpf = input("Digite o Cpf do novo cliente: ")
                              novoCliente = Cliente(None,nome,cpf)
                              con.manipularBanco(novoCliente.inserirCliente())
                              print("Cliente Adicionado com sucesso!") 
                        case 3:
                              #atualizar cliente
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
                                          #atualizar somente o nome
                                          case 1 :
                                                novoClienteAtualizar._nome = input("Digite o novo Nome: ")
                                                con.manipularBanco(novoClienteAtualizar.atualizarCliente()) 
                                                print("Atualizado com sucesso!") 
                                                condicao2 = False
                                                
                                          #atualizar somente o cpf
                                          case 2 :
                                                novoClienteAtualizar._cpf = input("Digite o novo Cpf: ")
                                                con.manipularBanco(novoClienteAtualizar.atualizarCliente())
                                                print("Atualizado com sucesso!")
                                                condicao2 = False
                                         
                                          #atualizar nome e cpf     
                                          case 3 :
                                                novoClienteAtualizar._nome = input("Digite o novo Nome: ")  
                                                novoClienteAtualizar._cpf = input("Digite o novo Cpf: ")  
                                                con.manipularBanco(novoClienteAtualizar.atualizarCliente()) 
                                                print("Atualizado com sucesso!")  
                                                condicao2 = False 
                              else:
                                    print("Id digitado não existe,digite novamente")                      
                        case 4:
                              #deletar cliente
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
                                               
  match opcao :
      case 2:
           opcaoLivro = 1
           while opcaoLivro !=0 :
                 #menu livro
                  print('''
                        1. Ver Livro específico
                        2. Inserir novo livro
                        3 .Atualizar livro
                        4 .Deletar Livro
                        0 .Voltar para o menu principal
                        ''')  
                  opcaoLivro = int(input("Digite o que deseja fazer: "))                               
                  match opcaoLivro:
                  #Ver livro específico      
                   case 1:
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
                   case 2: 
                        #inserir Livro
                        novoNome = input("Digite o nome do novo Livro: ")
                        novoAutor = input("Digite o nome do autor do novo livro: ")
                        novoLivro = Livro(None,novoNome,novoAutor)
                        con.manipularBanco(novoLivro.inserirLivro())
                        print("Livro Adicionado com sucesso!")                             
                   case 3 :
                        #Atualizar Livro
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
                                          #Atualizar somente o nome do livro
                                          case 1 :
                                                novoLivroAtualizado._nome = input("Digite o nome do novo livro: ")
                                                con.manipularBanco(novoLivroAtualizado.atualizarLivro()) 
                                                print("Atualizado com sucesso!") 
                                                condicao5 = False
                                          case 2 :
                                                #Atualizar somente o nome do autor do livro
                                                novoLivroAtualizado._autor = input("Digite o novo nome do autor: ")
                                                con.manipularBanco(novoLivroAtualizado.atualizarLivro())
                                                print("Atualizado com sucesso!")
                                                condicao5 = False
                                          case 3 :
                                                #Atualizar o nome e o autor do livro
                                                novoLivroAtualizado._nome = input("Digite o nome do novo livro: ")  
                                                novoLivroAtualizado._autor = input("Digite o novo nome do autor: ")  
                                                con.manipularBanco(novoLivroAtualizado.atualizarLivro()) 
                                                print("Atualizado com sucesso!") 
                                                condicao5 = False
                              else:
                                    print("Id digitado não existe,digite novamente")    
                                                                       
                   case 4:
                              #deletar Livro
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
                                   
  match opcao :
     case 3:
           #Menu aluguel
           opcaoAluguel = 1
           while opcaoAluguel !=0 :   
            print('''
                        1. Adicionar aluguel
                        2. Ver Alugueis
                        3. Deletar aluguel
                        0 .Voltar para o menu principal
                        ''')  
            opcaoAluguel = int(input("Digite o que deseja fazer: "))      
            match opcaoAluguel:
                  #Inserir novo aluguel
                   case 1:
                        mostrarClientes(con)
                        print("Escolha um Cliente:")
                        clienteID = input("Digite o id do cliente escolhido: ")

                        print("Escolha um Livro:")
                        mostrarLivros(con)

                        livroID = input("Digite o id do livro escolhido: ")

                        con.manipularBanco(f'''
                                    INSERT INTO "Aluguel"
                                    Values(default, {clienteID}, {livroID}, default)
                                    ''')
                        print("Aluguel cadastrado.")    
                   case 2:
                         #Mostrar alugueis de um cliente 
                         mostrarAlugueis(con)
                         idConsulta = int(input("Digite o id do aluguel para consultar: "))
                         tuplas =  con.consultarBanco(f'''
                                             SELECT "Cliente"."Nome", "Livro"."Nome" FROM "Aluguel"
                                                INNER JOIN "Cliente" 
                                                      ON "Aluguel"."ID_Cliente" = "Cliente"."ID"
                                                INNER JOIN "Livro"
                                                      ON "Aluguel"."ID_Livro" = "Livro"."ID"
                                                WHERE  "Aluguel"."ID" = '{idConsulta}' 
                                             ''')
                         for resultado in tuplas:
                                print(f'''
                                    Nome do Cliente  - {resultado[0]}
                                    Livro Alugado  - {resultado[1]}
                                          ''')
                   case 3:
                              #Deletar aluguel 
                              mostrarAlugueis(con)
                              idAluguelDeletado = int(input("Digite o id do aluguel que deseja deletar: "))
                              con.manipularBanco(f'''
                                                DELETE FROM "Aluguel"
                                                WHERE "ID" = '{idAluguelDeletado}'    
                                                '''    )
                              print("Aluguel deletado com sucesso!")             
                                                
except(Exception, psycopg2.Error) as error:
        print("Ocorreu um erro -", error)
        