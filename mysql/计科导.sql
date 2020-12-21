/*
SQLyog Ultimate v12.09 (64 bit)
MySQL - 8.0.22 : Database - website
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`website` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `website`;

/*Table structure for table `building` */

DROP TABLE IF EXISTS `building`;

CREATE TABLE `building` (
  `name` varchar(9) DEFAULT NULL,
  `intro` text,
  `like_num_building` int DEFAULT NULL,
  `rank_building` int DEFAULT NULL,
  `picture` varchar(200) DEFAULT NULL,
  `id` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `building` */

insert  into `building`(`name`,`intro`,`like_num_building`,`rank_building`,`picture`,`id`) values ('仰望星空','2007年5月14日，同济大学百年校庆期间，国务院总理温家宝亲临同济视察并\r\n即席演讲。9月4日，温总理诗作《仰望星空》在《人民日报》发表。以此赋名校区中心景观，寄寓同济人的精神追求。\r\n',25,2,'image/building/1.jpg',1),('智信馆','智信馆是同济大学电子与信息工程学院楼，其建筑风格十分前卫，与电院学子勇于创新、开拓进取的精神非常契合。(这也是电信人自己的楼哦！)\r\n',8,5,'image/building/2.jpg',2),('开物馆','开物馆是同济大学机械工程学院楼，其建筑风格朴实大气。开物馆的名字取自《天工开物》，寓意机械学子也能像宋应星那样，为祖国的生产发展做出自己的贡献。\r\n',12,4,'image/building/3.jpg',3),('宁远馆','宁远馆是同济大学汽车学院楼，外墙选用了亮丽的颜色体现了汽院学子积极向上的学习态度，辅以玻璃外墙增强了视觉感受，绿化的设计与整体建筑相得益彰，让人赏心悦目。\r\n',14,3,'image/building/4.jpg',4),('嘉定校区体育中心','嘉定同济体育中心游泳馆整体构筑呈三角形，房顶呈20°倾斜，房顶一侧接地，接地处利用曲线连接，使游泳馆整体给人一种流线型之美。\r\n窗户则采用网格状结构，使得照射进入游泳馆的光线不至于太集中，让人们能够在游泳的同时享受夕阳点缀在泳池中央的黄昏之美。\r\n左侧的游泳馆与右侧的体育馆相连接，连接部分也是体育馆二楼的入口，入口处采用多级式楼梯与地相连，给人一种大气感。\r\n',31,1,'image/building/5.jpg',5),('通达馆','通达馆是同济大学交通运输工程学院楼。而与之相应，楼如其名，通达馆并没有选择复杂的建筑风格，俯视时只简简单单的呈现出矩形的形状，但在细微处的设计上却独树一帜，用相间的色块配上玻璃窗，提升了建筑的层次感，豁达的外观也是交运学子一往无前的内心写照。\r\n',7,8,'image/building/6.jpg',6),('德才馆','德才馆是同济大学材料科学与工程学院楼，在建筑风格厚重无华的同时也添加了别样的色彩。象征了材料学子恪守规则却又想推陈出新的理想追求。\r\n',8,6,'image/building/7.jpg',7),('图书馆','同济大学嘉定校区图书馆位于同济大学嘉定校区核心区域，处于三条校园主轴线的交汇点。\r\n图书馆建筑造型气势恢宏，读者从室外进入矿场的一层借阅大厅后，可以通过一层钢木结构的楼梯直上二层的阅览室和三层的学术报告厅，意喻“书籍是人类进步的阶梯”，读者拾级而上，到达知识的殿堂。主楼西北两侧的外墙面设计成以“图”和“书”的艺术体造型花岗岩，意喻读者在知识的海洋里遨游。\r\n\r\n',8,7,'image/building/8.jpg',8);

/*Table structure for table `comments` */

DROP TABLE IF EXISTS `comments`;

CREATE TABLE `comments` (
  `user_id` int DEFAULT NULL,
  `object_name` varchar(8) DEFAULT NULL,
  `content` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `comments` */

insert  into `comments`(`user_id`,`object_name`,`content`) values (0,'嘉定食堂','什么jb玩意'),(0,'麦当劳','没有安全问题');

/*Table structure for table `food` */

DROP TABLE IF EXISTS `food`;

CREATE TABLE `food` (
  `name` varchar(8) DEFAULT NULL,
  `intro` text,
  `like_num_food` int DEFAULT NULL,
  `rank_food` int DEFAULT NULL,
  `picture` varchar(200) DEFAULT NULL,
  `id` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `food` */

insert  into `food`(`name`,`intro`,`like_num_food`,`rank_food`,`picture`,`id`) values ('嘉定食堂','物美价廉，安全卫生，菜品多种多样。',13,6,'image/food/1.jpg',1),('希食东','主打日料，味道很不错，肉量和饭量在日料店里都算比较实惠的。',14,5,'image/food/2.jpg',2),('麦当劳','麦当劳永远滴神！！！！！。',44,1,'image/food/3.jpg',3),('黄小渝','小面比较正宗，豆浆和泡菜都和重庆当地很像，串串味道也不错',23,2,'image/food/4.jpg',4),('淮南牛肉汤','牛肉汤头十分鲜美，烧饼又薄又脆，牛骨啃着很香',22,3,'image/food/5.jpg',5),('面霸','比较干净卫生，面的味道不错，但口味有点重',22,4,'image/food/6.jpg',6);

/*Table structure for table `id` */

DROP TABLE IF EXISTS `id`;

CREATE TABLE `id` (
  `id_yjh` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `id` */

insert  into `id`(`id_yjh`) values (2);

/*Table structure for table `likes` */

DROP TABLE IF EXISTS `likes`;

CREATE TABLE `likes` (
  `user_id` int DEFAULT NULL,
  `object_name` varchar(8) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `likes` */

insert  into `likes`(`user_id`,`object_name`) values (1,'仰望星空');

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `username` varchar(20) DEFAULT NULL,
  `id` int NOT NULL,
  `sex` char(2) DEFAULT NULL,
  `password` varchar(20) DEFAULT NULL,
  `sign` varchar(100) DEFAULT NULL,
  `email` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `user` */

insert  into `user`(`username`,`id`,`sex`,`password`,`sign`,`email`) values ('lly',0,'帅','001210','没有签名','1977625799@qq.com'),('cxk',1,'男','123456','好家伙','1977625799@qq.com'),('alex',2,'男','1qaz','好家伙',' '),('llyy',3,'男','1234546','好家伙','1977625799@qq.com'),('alex',4,'男','123','好家伙',' ');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
