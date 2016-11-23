-- MySQL schema para a API de Processos de Software.
-- Modificada para ter uma descrição mais completa do banco de dados.
SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";
--
-- Database: `processodesoftware`
--
-- --------------------------------------------------------

CREATE SCHEMA IF NOT EXISTS `processodesoftware` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci ;
USE `processodesoftware` ;
--
-- DROP TABLE IF EXISTS `users` ;
--
-- Estrutura da tabela `users`
--
CREATE TABLE IF NOT EXISTS `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `idade` int(11) NOT NULL,
  `senha` varchar(256) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
--
-- DROP TABLE IF EXISTS `users_info` ;
--
-- Estrutura da tabela `users_info`
--
CREATE TABLE IF NOT EXISTS `users_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `facebook` varchar(100) DEFAULT NULL,
  `whatsapp` bigint(11) DEFAULT NULL,
  `id_user` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_users_info_user_idx`
    FOREIGN KEY (`id_user`)
    REFERENCES `processodesoftware`.`users` (`id`)
  ON DELETE CASCADE -- Nao existe mais o usuario que referencia esse objeto
  ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `skills` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `user_interests` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `id_user` int(11) NOT NULL,
  `id_skill` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC),
  CONSTRAINT `fk_ui_user_idx`
    FOREIGN KEY (`id_user`)
    REFERENCES `processodesoftware`.`users` (`id`)
    ON DELETE CASCADE -- Nao existe mais o usuario que referencia esse objeto
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_ui_skill_idx`
    FOREIGN KEY (`id_skill`)
    REFERENCES `processodesoftware`.`skills` (`id`)
    ON DELETE CASCADE -- Nao existe mais o skill que o usuario tinha
    ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `user_skills` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `id_user` int(11) NOT NULL,
  `id_skill` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC),
  CONSTRAINT `fk_us_user_idx`
    FOREIGN KEY (`id_user`)
    REFERENCES `processodesoftware`.`users` (`id`)
    ON DELETE CASCADE -- Nao existe mais o usuario que referencia esse objeto
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_us_skill_idx`
    FOREIGN KEY (`id_skill`)
    REFERENCES `processodesoftware`.`skills` (`id`)
    ON DELETE CASCADE -- Nao existe mais o skill que o usuario tinha
    ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `user_match` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `id_user_not` int(11) NOT NULL,
  `id_user_has` int(11) NOT NULL,
  `id_skill` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC),
  CONSTRAINT `fk_um_user_not_idx`
    FOREIGN KEY (`id_user_not`)
    REFERENCES `processodesoftware`.`users` (`id`)
    ON DELETE CASCADE -- Nao existe mais o usuario que referencia esse objeto
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_um_user_has_idx`
    FOREIGN KEY (`id_user_has`)
    REFERENCES `processodesoftware`.`users` (`id`)
    ON DELETE CASCADE -- Nao existe mais o usuario que referencia esse objeto
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_um_skill_idx`
    FOREIGN KEY (`id_skill`)
    REFERENCES `processodesoftware`.`skills` (`id`)
    ON DELETE CASCADE -- Nao existe mais o skill que o usuario tinha
    ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `pictures` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `filename` varchar(100) NOT NULL,
  `id_user` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_pictures_user_idx`
    FOREIGN KEY (`id_user`)
    REFERENCES `processodesoftware`.`users` (`id`)
  ON DELETE CASCADE -- Nao existe mais o usuario que referencia esse objeto
  ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Alterações das tabelas para não quebrar nada.
ALTER TABLE users
ADD UNIQUE INDEX `email_UNIQUE` (`email` ASC);
ALTER TABLE users
ADD UNIQUE INDEX `id_UNIQUE` (`id` ASC);
ALTER TABLE users_info
ADD UNIQUE INDEX `id_UNIQUE` (`id` ASC);
