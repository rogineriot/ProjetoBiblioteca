CREATE TABLE Aluno(
	NroMatricula int GENERATED ALWAYS AS IDENTITY,
	Nome varchar(255) NOT NULL,
	CPF char(11) NOT NULL,
	Telefone char(255),
	Endereço varchar(255) NOT NULL
	Ano de nascimento int,
	Primary key(NroMatricula)
	);
	
INSERT INTO Aluno
	VALUES(default,'Antonio Almeida','12458794587','32136349','Avenida Anotnio Sales','1998');


CREATE TABLE Disciplina(
	CodDisciplina int GENERATED ALWAYS AS IDENTITY,
	Nome varchar(255) NOT NULL,
	Codigo do curso char(11) NOT NULL,
  Primary key(CodDisciplina)
	); 

  INSERT INTO Aluno
	  VALUES(default,'Banco de Dados','CK_14235');

  CREATE TABLE Matricula(
    NroMatricula int GENERATED ALWAYS AS IDENTITY,
    	CodDisciplina char(50) NOT NULL,
      Semestre int NOT NULL,
      Ano int NOT NULL,
      Nota float NOT NULL,
      NroFaltal int NOT NULL

    Primary key(NroMatricula)
	); 

    INSERT INTO Matricula
	    VALUES(default,'CK_485','2','2023','7.8','5')