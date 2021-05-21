
-- CREATE DATABASE passagens;

CREATE SCHEMA IF NOT EXISTS mydb;

-- -----------------------------------------------------
-- Table mydb.aeroporto
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS mydb.aeroporto (
  id INT NOT NULL,
  nome VARCHAR(100) NOT NULL,
  cidade VARCHAR(100) NOT NULL,
  PRIMARY KEY (id));

-- -----------------------------------------------------
-- Table mydb.voo
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS mydb.voo (
  id INT NOT NULL,
  id_aeroporto INT NULL,
  destino VARCHAR(100) NOT NULL,
  companhia VARCHAR(100) NOT NULL,
  data TIMESTAMP NULL,
  capacidade INT NOT NULL,
  ocupacao INT NOT NULL,
  preco FLOAT NULL,
  PRIMARY KEY (id),
  CONSTRAINT fk_voo_aero
    FOREIGN KEY (id_aeroporto)
    REFERENCES mydb.aeroporto (id));

-- -----------------------------------------------------
-- Table mydb.cadastro
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS mydb.cadastro (
  id INT NOT NULL,
  nome VARCHAR(245) NOT NULL,
  email VARCHAR(45) NOT NULL,
  senha VARCHAR(45) NOT NULL,
  PRIMARY KEY (id));

-- -----------------------------------------------------
-- Table mydb.reserva
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS mydb.reserva (
  id INT NOT NULL,
  id_voo INT NULL,
  id_cadastro INT NULL,
  e_ticket VARCHAR(45) NULL,
  PRIMARY KEY (id),
  CONSTRAINT fk_reserva_voo
    FOREIGN KEY (id_voo)
    REFERENCES mydb.voo (id),
  CONSTRAINT fk_reserva_cadastro
    FOREIGN KEY (id_cadastro)
    REFERENCES mydb.cadastro (id));

