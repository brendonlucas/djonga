create table usuario(
    id_usuario integer not null,
    nome varchar(100) not null,
    primary key(id_usuario)
);

create table sala(
    id_sala integer not null,
    nome varchar(100),
    primary key(id_sala)
);

create table frequencia(
    id_frequencia integer,
    descricao varchar(100),
    id_sala integer,
    constraint fk_fre_sala foreign key(id_sala) references sala(id_sala),
    primary key(id_frequencia)
);


create table sala_usuario(
    id_usuario integer,
    id_sala integer,
    constraint fk_su_user foreign key(id_usuario) references usuario(id_usuario),
    constraint fk_su_sala foreign key(id_sala) references sala(id_sala),
    primary key(id_usuario,id_sala)
);

create table frequencia_usuario(
    id_frequencia integer,
    id_usuario integer,
    presenca integer,
    constraint fk_fu_user foreign key(id_usuario) references usuario(id_usuario),
    constraint fk_fu_frec foreign key(id_frequencia) references frequencia(id_frequencia),
    primary key(id_frequencia,id_usuario)
);




