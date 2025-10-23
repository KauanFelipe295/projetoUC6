create database biblioteca;

use biblioteca;

create table livros (
    id_livro integer auto_increment primary key,
    titulo text not null,
    autor text not null,
    disponivel integer default 1
);

create table usuario (
    cpf varchar(11) not null primary key,
    nome text not null
);

create table emprestimos (
    id_emprestimo integer auto_increment primary key,
    cpf varchar(11) not null,
    id_livro integer not null,
    data_emprestimo date not null,
    foreign key (cpf) references usuario(cpf),
    foreign key (id_livro) references livros(id_livro)
);