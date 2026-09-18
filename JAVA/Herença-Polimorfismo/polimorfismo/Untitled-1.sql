-- -----------------------------------------------------
-- Table `clientes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `clientes` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `contas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `contas` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `saldo` DECIMAL NOT NULL,
  `clientes_id` INT NOT NULL,
  PRIMARY KEY (`id`, `clientes_id`),
  INDEX `fk_contas_clientes_idx` (`clientes_id` ASC),
  CONSTRAINT `fk_contas_clientes`
    FOREIGN KEY (`clientes_id`)
    REFERENCES `clientes` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `logs`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `logs` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `move` DECIMAL(10,2) NOT NULL,
  `id_cli 1` INT NOT NULL,
  `id_cli 2` INT NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;