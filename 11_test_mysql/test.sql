-- tinyint 1-128 127
-- smallint 2 -32768-32767
-- mediumint 3 -8388608-8388607
-- int 4 -213747483648-2147483747
-- bigint 8 -9223372036854775808-9223372036854775807

-- 整数 int
-- 小数 decimal
-- 字符串 varchar,char （0-255）
-- 日期时间 date(4)|2020-01-01,time(3)|12:49:12,datetime(8)|2012-01-12 12:12:12,year(1)|2018,timstamp(4)
-- 枚举类型 enum
-- 大文本数据类型 text 当字符大于4000的时候推荐使用这个（0-65535）


create table classes(id int not null primary key,
name varchar(30));

insert into classes value (0,"python大神");
-- shift+option+down 复制下一行
insert into classes value (0,"python第一人");

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
select round((sum(age)/count(*)),2) as avg from students;
-- 计算男性平均身高
select round((sum(age)/count(*)),2) as avg from students where gender=1;
-- 查找所有性别的数量统计
select gender,count(*) from students group by gender;
-- 组的名字拼接
select gender,group_concat(name) from students group by gender;

select gender,group_concat(name,age) from students group by gender;
select gender,group_concat(name," ",age,"-") from students group by gender;

-- 查询平均年龄超过30的姓名和性别 已经 平均年龄超过 30 的性别-----having age>30
select gender,group_concat(name,"-",gender,"-",age) from students group by gender having avg(age)>30;

-- 分页 从 index=0，开始往后取五条  （第N页减-1）*每页数量
select * from students limit 0,5;
select * from students limit 1,5;
-- 第二页 每页10条
select * from students limit 10,10;

-- 连接查询
select * from students as s inner join classes as c ;
-- 起一个别名
select * from students as s inner join classes as c on s.class_id=c.id;
-- left join会显示左边所有信息
select * from students as s left join classes as c on s.class_id=c.id;
-- right join会显示右边表所有信息
select s.*,c.name from students as s right join classes as c on s.class_id=c.id;
-- 增加where条件，查询没有报班级的信息
select s.*,c.name from students as s right join classes as c on s.class_id=c.id where s.class_id is null;

-- 子查询 查询身高最高的男生信息
select * from students where height=(select max(height) from students where gender="男");

-- 什么是三大范式：
-- 第一范式：当关系模式R的所有属性都不能在分解为更基本的数据单位时，称R是满足第一范式的，简记为1NF。满足第一范式是关系模式规范化的最低要
--         求，否则，将有很多基本操作在这样的关系模式中实现不了。 用户名和电话号码地址不应该存储于一个字段。
-- 第二范式：如果关系模式R满足第一范式，并且R得所有非主属性都完全依赖于R的每一个候选关键属性，称R满足第二范式，简记为2NF。
--         每一行的数据只能与其中一列相关，即一行数据只做一件事。只要数据列中出现数据重复，就要把表拆分开来。
-- 第三范式：设R是一个满足第一范式条件的关系模式，X是R的任意属性集，如果X非传递依赖于R的任意一个候选关键字，称R满足第三范式，简记为3NF.
--         比如订单表里面的用户表，用户名称，用户电话，都依赖于customer_id ，所以不符合3NF,需要通过拆分.

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