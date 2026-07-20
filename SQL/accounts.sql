CREATE DATABASE IF NOT EXISTS bank_db0;
use bank_db0;

CREATE TABLE accounts (
	Account_number BIGINT PRIMARY KEY AUTO_INCREMENT,
    First_name VARCHAR(100) NOT NULL,
    Last_name VARCHAR(100) NOT NULL,
    Address VARCHAR(255),
    Mobile_number VARCHAR(13) NOT NULL,
    Date_of_birth DATE NOT NULL,
    Aadhaar_number CHAR(12) NOT NULL UNIQUE,
    Email VARCHAR(100) ,
    Password VARCHAR(100) NOT NULL,
    Balance DECIMAL(12,2) DEFAULT 0.00 ,
    
    CHECK (Mobile_number REGEXP '^[0-9]{10}$'),
    CHECK (Aadhaar_number REGEXP '^[0-9]{12}$'),
    CHECK (Balance >= 0)
    
    );