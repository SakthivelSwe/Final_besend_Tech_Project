create database atm;

use atm;

create table atmusers(
	bank_id int primary key auto_increment,acc_user varchar(40),acc_no int,
    	atm_pin int not null,balance_amt int
);

desc atmusers;


insert into atmusers(acc_user,acc_no,atm_pin,balance_amt) 
	values("sakthivel",123456,1234,40000),
	("Riyaz",234567,9876,100000),
	("sunil",345678,5688,60000);


select * from atmusers;