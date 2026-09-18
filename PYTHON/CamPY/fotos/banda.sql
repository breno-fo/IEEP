

-- -----------------------------------------------------
-- Table `genero`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `genero` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `bandas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bandas` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(45) NOT NULL,
  `genero_id` INT NOT NULL,
  PRIMARY KEY (`id`, `genero_id`),
  INDEX `fk_bandas_genero_idx` (`genero_id` ASC),
  CONSTRAINT `fk_bandas_genero`
    FOREIGN KEY (`genero_id`)
    REFERENCES `genero` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `discos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `discos` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(45) NOT NULL,
  `bandas_id` INT NOT NULL,
  `bandas_genero_id` INT NOT NULL,
  PRIMARY KEY (`id`, `bandas_id`, `bandas_genero_id`),
  INDEX `fk_discos_bandas1_idx` (`bandas_id` ASC, `bandas_genero_id` ASC),
  CONSTRAINT `fk_discos_bandas1`
    FOREIGN KEY (`bandas_id` , `bandas_genero_id`)
    REFERENCES `bandas` (`id` , `genero_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `musicas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `musicas` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(45) NOT NULL,
  `discos_id` INT NOT NULL,
  PRIMARY KEY (`id`, `discos_id`),
  INDEX `fk_musicas_discos1_idx` (`discos_id` ASC),
  CONSTRAINT `fk_musicas_discos1`
    FOREIGN KEY (`discos_id`)
    REFERENCES `discos` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;