create table classes(id int not null primary key,
name varchar(30));

insert into classes value (0,"python大神");

select * from classes;

create table students(
      id int not null primary key auto_increment ,
      name varchar (30),
      age tinyint unsigned default 0,
      gender enum("男","女"),
      class_id int unsigned
      );

drop table students;

#  修改表名
ALTER TABLE students RENAME teacher;

# 删除表的外键约束
ALTER TABLE 表名 DROP FOREIGN KEY 外键别名;

SHOW CREATE TABLE students;

insert into students values (0,"张三",12,"男",1);

select * from students;

-- 增加字段
alter table students add column birthday date;
alter table students add column height decimal (5,2);

-- 修改属性名称的 数据格式
alter table students change column birth births  date default "1990-01-01";
alter table students change  birthday birth date  default "1990-01-01";

-- 删除字段
alter table students drop column height;
# – –按日
SELECT COUNT(*),DATE(CreateTime) FROM t_voipchannelrecord WHERE YEAR(CreateTime)='2016' GROUP BY DAY(CreateTime);
# – –按周
SELECT COUNT(*),WEEK(CreateTime) FROM t_voipchannelrecord WHERE MONTH(CreateTime) = '8' GROUP BY WEEK(CreateTime);
# –周一到周五每天的统计结果
SELECT COUNT(*),DAYNAME(CreateTime) FROM t_voipchannelrecord WHERE YEAR(CreateTime) = '2016' GROUP BY DAYNAME(CreateTime);
# 统计本周数据
SELECT COUNT(*) FROM t_voipchannelrecord WHERE MONTH(CreateTime) = MONTH(CURDATE()) AND WEEK(CreateTime) = WEEK(CURDATE());
# –按月统计
SELECT COUNT(*),MONTH(CreateTime) FROM t_voipchannelrecord WHERE YEAR(CreateTime) = '2016' GROUP BY MONTH(CreateTime);
# –统计本月数据
SELECT COUNT(*) FROM t_voipchannelrecord WHERE MONTH(CreateTime) = MONTH(CURDATE()) AND YEAR(CreateTime) = YEAR(CURDATE());
# –按季统计
SELECT COUNT(*),QUARTER(CreateTime) FROM t_voipchannelrecord WHERE YEAR(CreateTime) = '2016' GROUP BY QUARTER(CreateTime);
# –按年统计
SELECT COUNT(*),YEAR(CreateTime) FROM t_voipchannelrecord GROUP BY YEAR(CreateTime)
