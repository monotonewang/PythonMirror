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