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



INSERT INTO `marvel`.`comics` (`id`, `digitalId`, `title`, `issueNumber`, `description`, `modified`, `upc`, `format`, `pageCount`, `resourceURI`) VALUES ('2', '0', '\"A-Bomb (HAS)', '0', 'Rick Jones has been Hulk\'s best bud since day one, but now he\'s more than a friend...he\'s a teammate! Transformed by a Gamma energy explosion, A-Bomb\'s thick, armored skin is just as strong and powerful as it is blue. And when he curls into action, he uses it like a giant bowling ball of destruction!', '2013-09-18', '2', 'Digest', '152', 'http://gateway.marvel.com/v1/public/characters/1017100');
INSERT INTO `marvel`.`comics` (`id`, `digitalId`, `title`, `issueNumber`, `variantDescription`, `modified`, `upc`, `diamondCode`, `format`, `pageCount`, `resourceURI`) VALUES ('3', '0', 'Marvel Previews (2017)', '12', 'SPIDER-MAN', '2019-08-21', '3', 'JUL190068', 'printPrice', '178', 'http://gateway.marvel.com/v1/public/stories/66');
INSERT INTO `marvel`.`comics` (`id`, `digitalId`, `title`, `issueNumber`, `variantDescription`, `description`, `modified`, `upc`, `format`, `pageCount`, `resourceURI`) VALUES ('4', '0', 'Official Handbook of the Marvel Universe (2004) #13 (TEAMS)', '13', 'TEAMS', 'Heavy-hitting heroes unite! This Official Handbook contains in-depth bios on more than 30 of the Marvel Universe\'s most awesome assemblages - including the Defenders, Power Pack and the New Thunderbolts! Plus: An all-new cover by superstar artist Tom Grummett, digitally painted by Morry Hollowell.\\r<br>48 PGS./All Ages ...$3.99\\r<br>', '0001-11-30', '4', 'Comic', '195', 'http://gateway.marvel.com/v1/public/stories/65143');
INSERT INTO `marvel`.`comics` (`id`, `digitalId`, `title`, `issueNumber`, `variantDescription`, `description`, `modified`, `upc`, `format`, `pageCount`, `resourceURI`) VALUES ('5', '0', 'Official Handbook of the Marvel Universe (2004) #10 (MARVEL KNIGHTS)', '10', 'MARVEL KNIGHTS', 'On the mean streets of the Marvel Universe, the kid gloves come off. Guardian devils, vengeance-seeking vigilantes and enigmatic assassins stalk the city\'s dark underbelly _ and the urban action unfolds with gritty intensity. The newest entry in Marvel\'s best-selling Handbook series, OHOTMUMK04 includes in-depth bios on a host of the House\'s edgiest icons - from Black Panther to Shang-Chi!', '0001-11-30', '5', 'Comic', '214', 'http://gateway.marvel.com/v1/public/comics/323');


INSERT INTO `marvel`.`character` (`id`, `available`, `collectionURI`, `returned`, `comic_id`) VALUES ('1', '8', 'http://gateway.marvel.com/v1/public/characters/1011176/stories', '1', '3');
INSERT INTO `marvel`.`character` (`id`, `available`, `collectionURI`, `returned`, `comic_id`) VALUES ('2', '1', 'http://gateway.marvel.com/v1/public/characters/1011176/events', '8', '5');
INSERT INTO `marvel`.`character` (`id`, `available`, `collectionURI`, `returned`, `comic_id`) VALUES ('3', '0', 'http://gateway.marvel.com/v1/public/characters/1010870/comics', '3', '4');
INSERT INTO `marvel`.`character` (`id`, `available`, `collectionURI`, `returned`, `comic_id`) VALUES ('4', '21', 'http://gateway.marvel.com/v1/public/characters/1010870/series', '4', '2');

INSERT INTO `marvel`.`creator` (`id`, `firstName`, `middleName`, `lastName`, `suffix`, `fullName`, `modified`) VALUES ('1', '#X', ' ', ' ', ' ', '#X', '2019-12-11');
INSERT INTO `marvel`.`creator` (`id`, `firstName`, `middleName`, `lastName`, `suffix`, `fullName`, `modified`) VALUES ('2', 'A.R.K.', ' ', ' ', ' ', 'A.R.K.', '2007-01-02');
INSERT INTO `marvel`.`creator` (`id`, `firstName`, `middleName`, `lastName`, `suffix`, `fullName`, `modified`) VALUES ('3', 'All Thumbs Creative', ' ', ' ', ' ', 'All Thumbs Creative', '2018-07-24');
INSERT INTO `marvel`.`creator` (`id`, `firstName`, `middleName`, `lastName`, `suffix`, `fullName`, `modified`) VALUES ('4', 'ALSJOERDSMA', ' ', ' ', ' ', 'ALSJOERDSMA', '2007-01-02');



INSERT INTO `marvel`.`creator_comics` (`creator_id`, `comics_id`) VALUES ('1', '2');
INSERT INTO `marvel`.`creator_comics` (`creator_id`, `comics_id`) VALUES ('2', '3');
INSERT INTO `marvel`.`creator_comics` (`creator_id`, `comics_id`) VALUES ('1', '4');
INSERT INTO `marvel`.`creator_comics` (`creator_id`, `comics_id`) VALUES ('3', '4');
INSERT INTO `marvel`.`creator_comics` (`creator_id`, `comics_id`) VALUES ('4', '5');
INSERT INTO `marvel`.`creator_comics` (`creator_id`, `comics_id`) VALUES ('2', '2');
