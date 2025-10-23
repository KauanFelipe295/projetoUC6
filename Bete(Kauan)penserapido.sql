create database pense_rapido;
use pense_rapido;

Create table perguntas(
id  int auto_increment primary key,
pergunta varchar(512) not null,
categoria varchar(255) not null,
resposta text not null
);

use pense_rapido;

select * from perguntas;

insert into perguntas (pergunta, categoria, resposta)
values("Qual comando atualiza dados em uma tabela?", "Banco de dados", "UPDATE")