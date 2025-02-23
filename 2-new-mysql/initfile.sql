CREATE USER IF NOT EXISTS s4t_keystone@localhost IDENTIFIED BY 'Um3d3m0n';
SET PASSWORD FOR s4t_keystone@localhost = PASSWORD('Um3d3m0n');

CREATE USER IF NOT EXISTS s4t_iotronic@localhost IDENTIFIED BY 'Um3d3m0n';
SET PASSWORD FOR s4t_iotronic@localhost = PASSWORD('Um3d3m0n');

CREATE USER IF NOT EXISTS s4t_designate@localhost IDENTIFIED BY 'Um3d3m0n';
SET PASSWORD FOR s4t_designate@localhost = PASSWORD('Um3d3m0n');

CREATE DATABASE s4t_keystone;
GRANT ALL PRIVILEGES ON s4t_keystone.* TO 's4t_keystone'@'localhost' IDENTIFIED BY 'Um3d3m0n';
GRANT ALL PRIVILEGES ON s4t_keystone.* TO 's4t_keystone'@'%' IDENTIFIED BY 'Um3d3m0n';

CREATE DATABASE s4t_iotronic;
GRANT ALL PRIVILEGES ON s4t_iotronic.* TO 's4t_iotronic'@'localhost' IDENTIFIED BY 'Um3d3m0n';
GRANT ALL PRIVILEGES ON s4t_iotronic.* TO 's4t_iotronic'@'%' IDENTIFIED BY 'Um3d3m0n';

--CREATE DATABASE s4t_designate;
--GRANT ALL PRIVILEGES ON s4t_designate.* TO 's4t_designate'@'localhost' IDENTIFIED BY 'sm3d3m0n';
--GRANT ALL PRIVILEGES ON s4t_designate.* TO 's4t_designate'@'%' IDENTIFIED BY 'sm3d3m0n';
