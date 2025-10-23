Create database Biblioteca;
use Biblioteca;

create table usuario(
id int auto_increment primary key,
cpf char(14) not null,
nome varchar(255) not null,
email varchar(75) unique
);



Create table livros(
id int auto_increment primary key,
titulo varchar(255) not null,
autor varchar(255) not null,
disponivel boolean default true
);



Create table emprestimos(
id int auto_increment primary key,
id_livro int not null,
id_usuario int not null,
data_emprestimo date not null,
data_devolucao date not null,
devolvido boolean default false,
foreign key (id_livro) references livros(id),
foreign key (id_usuario) references usuario(id)
);



select * from emprestimos;
select * from livros;
select * from usuario;

insert into usuario
values(default, "000.167.098-09", "Kauan Felipe Cardoso", "kauan@kauan");


insert into livros
values(default, "Dungeons e Drama", "Kristy Boyce", True);

insert into emprestimos
values(default, 1,1, "2025-08-19", "2025-08-25", False);