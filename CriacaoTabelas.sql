#Criar banco de dados

     DROP DATABASE IF EXISTS "Biblioteca" ;
     CREATE DATABASE "Biblioteca";
     

#Criar tabela Cliente

     DROP TABLE IF EXISTS "Cliente";
     CREATE TABLE "Cliente"(
         "ID" int GENERATED ALWAYS AS IDENTITY,
         "Nome" varchar(255) NOT NULL,
         "CPF" char(11) NOT NULL UNIQUE,
         Primary Key("ID")
    );


#Criar tabela Livro
  DROP TABLE IF EXISTS "Livro";
    CREATE TABLE "Livro"(
         "ID" int GENERATED ALWAYS AS IDENTITY,
        "Nome" varchar(255) NOT NULL,
        "Autor" varchar(255) NOT NULL,
         Primary Key("ID")
     );
     
     DROP TABLE IF EXISTS "Aluguel";
     CREATE TABLE "Aluguel"(
         "ID" int GENERATED ALWAYS AS IDENTITY,
         "ID_Cliente" int NOT NULL,
         "ID_Livro" int NOT NULL,
         "Data_Aluguel" timestamp default current_timestamp,
         Primary Key("ID"),
         Constraint fk_cliente
             Foreign Key ("ID_Cliente")
             References "Cliente"("ID")
             ON DELETE CASCADE
            ON UPDATE NO ACTION
             ,
         Constraint fk_livro
            Foreign Key ("ID_Livro")
             References "Livro"("ID")
             ON DELETE SET NULL
            ON UPDATE NO ACTION
            );

#Consulta simples