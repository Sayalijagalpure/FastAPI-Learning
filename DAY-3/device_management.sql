create database device_monitoring;
use device_monitoring;
create table devices(
device_id int primary key,
device_name varchar(50),
company varchar(50));
insert into devices values
(1, 'Galaxy S24', 'Samsung'),
(2, 'iPhone 16', 'Apple'),
(3, 'Pixel 9', 'Google'),
(4, 'OnePlus 13', 'OnePlus');

create table readings (
    reading_id int primary key,
    device_name varchar(50),
    battery_percentage int
);
insert into readings values
(101, 'Galaxy S24', 90),
(102, 'iPhone 16', 85),
(103, 'Pixel 9', 78),
(104, 'OnePlus 13', 95);

select * from devices;

select * from devices
where company = 'Samsung';

select * from readings;

update readings
set battery_percentage = 80
where reading_id = 103;

delete from devices
where device_id = 4;