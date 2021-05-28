CREATE TABLE employees (
    Id       INTEGER      PRIMARY KEY AUTOINCREMENT,
    fullname VARCHAR (30) NOT NULL,
    job      VARCHAR (10),
    salary   INTEGER (10)
);

insert into employees(fullname,job,salary)
   values('Andy Roberts','SP',1500000)