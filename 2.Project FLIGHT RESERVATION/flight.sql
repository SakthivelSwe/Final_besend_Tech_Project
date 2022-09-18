create database flight;

use flight;

CREATE TABLE `clstype` (
  `sno` int DEFAULT NULL,
  `classtype` varchar(30) DEFAULT NULL,
  `rate` int DEFAULT NULL
) 


CREATE TABLE `food` (
  `sno` int DEFAULT NULL,
  `itemname` varchar(30) DEFAULT NULL,
  `rate` int DEFAULT NULL
)

CREATE TABLE `luggages` (
  `sno` int DEFAULT NULL,
  `weight` varchar(20) DEFAULT NULL,
  `rate` int DEFAULT NULL
)

CREATE TABLE `passengers` (
  `p_name` varchar(30) DEFAULT NULL,
  `p_address` varchar(30) DEFAULT NULL,
  `p_mobile` int DEFAULT NULL,
  `res_date` date DEFAULT NULL,
  `source` varchar(30) DEFAULT NULL,
  `destination` varchar(30) DEFAULT NULL
);