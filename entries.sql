/*
* @Author: yata
* @Date:   2018-06-04 16:04:32
* @Last Modified by:   yata
* @Last Modified time: 2018-06-04 16:07:08
*/
drop table if exists entries;
create table entries(
	id integer primary key autoincrement,
	title string not null,
	text string not null
);
