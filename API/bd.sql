-- MySQL schema para a API de Processos de Software.
-- Modificada para ter uma descrição mais completa do banco de dados.
SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";
--
-- Database: `processodesoftware`
--
-- --------------------------------------------------------

CREATE SCHEMA IF NOT EXISTS `dbpat` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci ;
USE `dbpat` ;
--
-- DROP TABLE IF EXISTS `users` ;
--
-- Estrutura da tabela `users`
--
CREATE TABLE IF NOT EXISTS `usuario` (
  `idUsuario` INT(11) AUTO_INCREMENT PRIMARY KEY,
  `nome` VARCHAR(50),
  `login` VARCHAR(50) ,
  `senha` VARCHAR(50),
  `nvacesso` INT(1)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


 CREATE TABLE IF NOT EXISTS `protocolo`(
   `idProtocolo` INT(15) AUTO_INCREMENT PRIMARY KEY,
   `origem` VARCHAR(50),
   `destino` VARCHAR(50),
   `idObjeto` INT(15),
    CONSTRAINT `fk_protoc_object`
    FOREIGN KEY (`idObjeto`)
    REFERENCES `dbpat`.`objeto` (`id`),
   `data` VARCHAR(10),
   `idUsuario` INT(11),
    CONSTRAINT `fk_proto_usuario`
    FOREIGN KEY (`idUsuario`)
    REFERENCES `dbpat`.`usuario` (`idUsuario`)
 )ENGINE=InnoDB DEFAULT CHARSET=utf8;

 CREATE TABLE IF NOT EXISTS `cautela` (
   `idCautela` INT(15) AUTO_INCREMENT PRIMARY KEY,
   `data_inicio` VARCHAR(10),
   `data_final` VARCHAR(10),
   `idUsuario` int(11) NOT NULL,
    CONSTRAINT `fk_cautela_usuario`
    FOREIGN KEY (`idUsuario`)
    REFERENCES `dbpat`.`usuario` (`idUsuario`),
   `cautelado` int(11) NOT NULL,
    CONSTRAINT `fk_cautela`
    FOREIGN KEY (`cautelado`)
    REFERENCES `dbpat`.`usuario` (`idUsuario`),
    `idObjeto` int(15) NOT NULL,
    CONSTRAINT `fk_objeto1`
    FOREIGN KEY (`idObjeto`)
    REFERENCES `dbpat`.`objeto` (`id`)
  )ENGINE=InnoDB DEFAULT CHARSET=utf8;

 CREATE TABLE IF NOT EXISTS `objeto` (
     `id` INT(15) AUTO_INCREMENT PRIMARY KEY,
     `tombo` INT(10) NOT NULL,
     `serialn` VARCHAR(30) NOT NULL,
     `local` VARCHAR(50),
     `descricao` VARCHAR(50),
     `situacao` INT(2)
     )ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `pictures` (
  `id` int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `filename` varchar(100) NOT NULL,
  `idObjeto` int(15) NOT NULL,
  CONSTRAINT `fk_picture_object`
  FOREIGN KEY (`idObjeto`)
  REFERENCES `dbpat`.`objeto` (`id`)
  ON DELETE CASCADE -- Nao existe mais o usuario que referencia esse objeto
  ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

