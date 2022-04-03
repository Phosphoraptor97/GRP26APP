CREATE TABLE IF NOT EXISTS userInfo (
email VARCHAR(256) NOT NULL,
username VARCHAR(32) NOT NULL,
firstName VARCHAR(32) NOT NULL,
lastName VARCHAR(32) NOT NULL,
password VARCHAR(32) NOT NULL,
PRIMARY KEY (email, username, firstName, lastName)
);

CREATE TABLE IF NOT EXISTS passengerDetail (
email VARCHAR(256) UNIQUE NOT NULL,
username VARCHAR(32) UNIQUE NOT NULL,
firstName VARCHAR(32) NOT NULL,
lastName VARCHAR(32) NOT NULL,
region VARCHAR(32),
contactNumber VARCHAR(16) NOT NULL,
paymentMethod VARCHAR(16) NOT NULL,
PRIMARY KEY (email, username),
FOREIGN KEY (email, username, firstName, lastName) REFERENCES userInfo(email, username, firstName, lastName) ON DELETE CASCADE DEFERRABLE
);

CREATE TABLE IF NOT EXISTS driverDetail (
email VARCHAR(256) UNIQUE NOT NULL,
username VARCHAR(32) UNIQUE NOT NULL,
firstName VARCHAR(32) NOT NULL,
lastName VARCHAR(32) NOT NULL,
contactNumber VARCHAR(16) NOT NULL,
paymentMethod VARCHAR(16) NOT NULL,
PRIMARY KEY (email, username),
FOREIGN KEY (email, username, firstName, lastName) REFERENCES userInfo(email, username, firstName, lastName) ON DELETE CASCADE DEFERRABLE
);

CREATE TABLE IF NOT EXISTS passengerOrder (
username VARCHAR(32) NOT NULL REFERENCES passengerDetail(username) ON DELETE CASCADE DEFERRABLE,
startPoint VARCHAR(128) NOT NULL,
destination VARCHAR(128) NOT NULL,
orderTime TIME NOT NULL,
numberPassengers SMALLINT NOT NULL,
luggageUsage SMALLINT NOT NULL,
CHECK(startPoint != destination AND orderTime >= '00:00:00' AND orderTime <= '23:59:59' AND numberPassengers >= 1 AND luggageUsage >= 0)
);

CREATE TABLE IF NOT EXISTS driverOrder (
username VARCHAR(32) NOT NULL REFERENCES passengerDetail(username) ON DELETE CASCADE DEFERRABLE,
startPoint VARCHAR(128) NOT NULL,
destination VARCHAR(128) NOT NULL,
startTime TIME NOT NULL,
numberSeats SMALLINT NOT NULL,
luggageSpace SMALLINT NOT NULL,
price DECIMAL(10,2) NOT NULL,
CHECK(startPoint != destination AND startTime >= '00:00:00' AND startTime <= '23:59:59' AND numberSeats >= 1 AND luggageSpace >= 0)
);

CREATE TABLE IF NOT EXISTS transactionHistory (
  transactionID VARCHAR(32) NOT NULL,
  driver VARCHAR(32) NOT NULL, ##refer to driver's username here
  passenger VARCHAR(32) NOT NULL, ##refer to passenger's username here
  startPoint VARCHAR(128) NOT NULL,
  destination VARCHAR(128) NOT NULL,
  totalPassengerNumber SMALLINT NOT NULL,
  price DECIMAL(10,2) NOT NULL,
  CHECK()
  );
  
