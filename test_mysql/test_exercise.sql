order表 需要 orderId，orderDate,customerId
order_detail表 需要orderId,productId,discount,quantity
customer表 需要customerId,customerName,customerAddr,cutomerCity
product表 需要 productId,productName,unitPrice,

create database jing_dong charset=utf8;
use jing_dong;

create table goods(
    id int unsigned not null primary key auto_increment,
    name varchar (150) not null,
    cate_name varchar (40) not null,
    brand_name varchar (40) not null,
    price decimal (10,3) not null default 0,
    is_show bit not null default 0,
    is_saleoff bit not null default 0
);

insert into goods values(0, "15.6寸笔记本","笔记本","华硕",3329,default,default);
insert into goods values(0, "15.6寸笔记本","超极本","联想",'3329',default,default);
insert into goods values(0, "13寸笔记本","Pad","华为",'3329',default,default);
insert into goods values(0, "15.6寸macPro笔记本","Pad","苹果"，'3329',default,default);
insert into goods values(0, "15.6寸外星人","Pad","戴尔",'8829',default,default);
insert into goods values(0, "15.6寸笔记本","Pad","联想",'3329',default,default);
insert into goods values(0, "15.6寸笔记本","Pad","联想",'3329',default,default);
insert into goods values(0, "15.6寸笔记本","Pad","联想",'3329',default,default);

-- 选择最贵的cate_name 和最大的金钱的 goods
select cate_name,max(price) from goods group by cate_name;

-- 所有的笔记本类型 最高价的 详情信息
select * from (select cate_name,max(price) as max_price from goods group by cate_name) as g_new
left join goods as g on g_new.cate_name=g.cate_name and g_new.max_price =g.price;

create table goods_cate(
    id int unsigned not null primary key auto_increment,
    name varchar (150) not null
);

-- 将goods中的品牌插入到good_cates表里面
insert into goods_cate(name) select cate_name from goods group by cate_name;

-- 将goods中的id修改到good_cates表里面
update goods as g inner join goods_cate as gc on g.cate_name=gc.name set g.cate_name=gc.id;

-- 添加外键 实际开发不使用外键，影响效率
alter table goods add foreign key(cate_id) reference good_cates(id);

-- 事务处理
update money set num=num+100 where id=2;
commit;
rollback;
-- 创建视图语法 视图是一张虚拟的表。原表数据更改会对视图产生影响
create view v_good_info as select g.name,g.brand_name,g.price,g_new.cate_name from (select cate_name,max(price) as max_price from goods group by cate_name) as g_new
left join goods as g on g_new.cate_name=g.cate_name and g_new.max_price =g.price;
update goods set price=9951 where id=5;
select * from v_good_info;
-- 索引
set profiling=1;
select * from goods where name like "%99999";
show profiles; 
create index name_index on goods(name(10));
-- 创建用户并授予所有权限 error on mysql8.0
grant select on jing_dong.* to 'laowang'@'localhost' identified by '123456';
show grants for laowang@localhost
-- 修改密码
update use set authentication_string=password('new_password') where use='user_name';
update use set authentication_string=password('123') where use='laowang';
flush_privileges

-- 开启远程登录 mysql.conf 
-- bind-addr=127.0.0.1 注释掉
-- 删除用户
drop user 'user_name'@'host'
-- 删除mysql表里面的user表数据
delete from user where user='username'
flush_privileges  -- 需要执行刷新权限

-- 备份服务器  所有数据库，锁住所有表防止有人修改
mysqldump -uroot -pmysql --all-databases  --lock=all-tables>~/master.db.sql
 
-- 重启mysql服务
sudo service mysql restart

-- 登录主服务器，创建用于从服务器同步数据使用的账号
grant replication slvae on ** to 'slave'@'%' identified by 'slave';
flush_privileges
-- 开启同步，查看同步状态
start_slave;
-- 查看到下面两个参数为yes，表示已经正常运行了
slave_io_running yes
slave_sql_running yes 
