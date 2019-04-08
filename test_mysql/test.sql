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

-- 修改表名
ALTER TABLE students RENAME teacher;

-- 删除表的外键约束
ALTER TABLE 表名 DROP FOREIGN KEY 外键别名;
-- 删除字段
alter table students drop column height;

show CREATE TABLE students;

insert into students values (0,"张三",12,"男",1);
insert into students values (0,"李四",18,"女",1);
insert into students values (0,"王五",28,"男",1);
insert into students values (0,"李小三",22,"男",1);
insert into students values (0,"周杰伦",22,"男",1);
insert into students values (0,"周公",22,"男",1);
insert into students values (0,"小梅",2,"女",1,168);

select * from students;

 select gender from student;
--  用于返回唯一不同的值
select distinct gender from students;

select students.name,students.age from students;
select s.name,s.age from students as s;
-- 查询所有年龄为18的学生
select s.name,s.age from students as s where age=18;
-- 查询所有年龄大于18小于28的学生
select s.name,s.age from students as s where age>18 and age<29;


-- 增加字段
alter table students add column birthday date;
alter table students add column height decimal (5,2);

-- 修改属性名称的 数据格式
alter table students change column birth births  date default "1990-01-01";
alter table students change  birthday birth date  default "1990-01-01";
-- 添加身高column
 alter table students add column height int;
-- 修改数据
update students set height=170 where id<8;

--模糊查询
-- like %替换一个或者多个  _替换一个
select * from students as s where s.name like "%三";
-- 查询有两个名字的姓名
select * from students as s where s.name like "__";
-- 查询字符必须大于等于两个 三
select * from students as s where s.name like "%_三";
-- 查询以周开始的姓名
select * from students as s where s.name like "周%";
select * from students as s where s.name rlike "^周.*";
select * from students as s where s.name like "周%伦";
-- 周开头，伦结尾
select * from students as s where s.name rlike "^周.*伦$";

-- 范围查询
-- 年龄在12,18,28之间的学生
select * from students where age =12 or age= 18 or age=28;
select * from students where age in(12,18,28);
-- 年龄不在12，18之前的学生
select * from students where age not in(12,18);

--between and 代表连续空间
-- 年龄在12 到19之间的学生
select * from students where age between 12 and 19;
-- 年龄不在12 到19之间的学生
select * from students where age not between 12 and 19;

-- 查询身高为空的人
select * from students where height is null;
-- 查询身高不为空的人
select * from students where height is not null;

-- 排序 年龄从大到小排
select * from students order by age desc;
-- 查询所有男生的年龄从小到大排
select * from students where gender=1 order by age ;
-- 查询所有男生的年龄18 到 22 从小到大排 如果年龄相同，id从大到小
select * from students where (age between 18 and 22 )and gender=1 order by age ,id desc;
--  查询所有女生年龄从大到小排列
select * from students where gender=2 order by age desc;
--  查询所有女生年龄从大到小排列 如果年龄相同，id从大到小
select * from students where gender=2 order by age desc,id desc;
--  查询所有女生年龄从小到大排列 如果年龄相同，height从大到小
 select * from students where (age between 18 and 22 )and gender=1 order by age ,height desc;

-- 聚合函数
select sum(age) from students;

-- 求最大的年龄
select max(age) from students;
-- 求平均年龄
select avg(age) from students;
select (sum(age)/count(*)) as avg from students;
-- 保留两位小数  存储单位不用小数
select round((sum(age)/count(*)),2) as acg from students;
-- 计算男性平均身高
select round((sum(age)/count(*)),2) as acg from students where gender=1;

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