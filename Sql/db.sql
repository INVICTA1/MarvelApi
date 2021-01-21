-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema marvel
-- -----------------------------------------------------
drop SCHEMA IF EXISTS `marvel` ;

-- -----------------------------------------------------
-- Schema marvel
-- -----------------------------------------------------
create SCHEMA IF NOT EXISTS `marvel` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `marvel` ;

-- -----------------------------------------------------
-- Table `marvel`.`alembic_version`
-- -----------------------------------------------------
drop table IF EXISTS `marvel`.`alembic_version` ;

create TABLE IF NOT EXISTS `marvel`.`alembic_version` (
  `version_num` VARCHAR(32) NOT NULL,
  PRIMARY KEY (`version_num`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `marvel`.`comics`
-- -----------------------------------------------------
drop table IF EXISTS `marvel`.`comics` ;

create TABLE IF NOT EXISTS `marvel`.`comics` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `digitalId` INT(11) NULL DEFAULT NULL,
  `title` VARCHAR(140) NULL DEFAULT NULL,
  `issueNumber` INT(11) NULL DEFAULT NULL,
  `variantDescription` VARCHAR(140) NULL DEFAULT NULL,
  `description` TEXT NULL DEFAULT NULL,
  `modified` DATETIME NULL DEFAULT NULL,
  `isbn` VARCHAR(140) NULL DEFAULT NULL,
  `upc` INT(11) NULL DEFAULT NULL,
  `diamondCode` VARCHAR(140) NULL DEFAULT NULL,
  `ean` VARCHAR(140) NULL DEFAULT NULL,
  `issn` VARCHAR(140) NULL DEFAULT NULL,
  `format` VARCHAR(140) NULL DEFAULT NULL,
  `pageCount` INT(11) NULL DEFAULT NULL,
  `resourceURI` VARCHAR(140) NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 5
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `marvel`.`character`
-- -----------------------------------------------------
drop table IF EXISTS `marvel`.`character` ;

create TABLE IF NOT EXISTS `marvel`.`character` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `available` INT(11) NULL DEFAULT NULL,
  `collectionURI` VARCHAR(140) NULL DEFAULT NULL,
  `returned` INT(11) NULL DEFAULT NULL,
  `comic_id` INT(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `character_ibfk_1`
    FOREIGN KEY (`comic_id`)
    REFERENCES `marvel`.`comics` (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 3
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

create INDEX `comic_id` ON `marvel`.`character` (`comic_id` ASC) VISIBLE;


-- -----------------------------------------------------
-- Table `marvel`.`creator`
-- -----------------------------------------------------
drop table IF EXISTS `marvel`.`creator` ;

create TABLE IF NOT EXISTS `marvel`.`creator` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `firstName` VARCHAR(100) NULL DEFAULT NULL,
  `middleName` VARCHAR(100) NULL DEFAULT NULL,
  `lastName` VARCHAR(100) NULL DEFAULT NULL,
  `suffix` VARCHAR(100) NULL DEFAULT NULL,
  `fullName` VARCHAR(100) NULL DEFAULT NULL,
  `modified` DATETIME NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 5
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `marvel`.`creator_comics`
-- -----------------------------------------------------
drop table IF EXISTS `marvel`.`creator_comics` ;

create TABLE IF NOT EXISTS `marvel`.`creator_comics` (

  `creator_id` INT(11) NOT NULL,
  `comics_id` INT(11) NOT NULL,
  PRIMARY KEY (`creator_id`,`comics_id`),
  CONSTRAINT `creator_comics_ibfk_1`
    FOREIGN KEY (`creator_id`)
    REFERENCES `marvel`.`creator` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `creator_comics_ibfk_2`
    FOREIGN KEY (`comics_id`)
    REFERENCES `marvel`.`comics` (`id`) ON DELETE CASCADE ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

create INDEX `creator_id` ON `marvel`.`creator_comics` (`creator_id` ASC) VISIBLE;

create INDEX `comics_id` ON `marvel`.`creator_comics` (`comics_id` ASC) VISIBLE;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

