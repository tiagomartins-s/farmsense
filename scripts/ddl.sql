create table UMIDADE
(
    ID      NUMBER generated as identity
        primary key,
    UMIDADE NUMBER(5, 2),
    ALERTA  NUMBER(1)
        check (ALERTA IN (0, 1)),
    DATA    TIMESTAMP(6)
)
/

create table TEMPERATURA
(
    ID          NUMBER generated as identity
        primary key,
    TEMPERATURA NUMBER(5, 2),
    ALERTA      NUMBER(1)
        check (ALERTA IN (0, 1)),
    DATA        TIMESTAMP(6)
)
/
