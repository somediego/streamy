create schema if not exists src_stream;
set search_path to src_stream;

drop view if exists src_stream.total;
drop view if exists src_stream.points;

drop table if exists src_stream.bets;
drop table if exists src_stream.results;

create table if not exists src_stream.bets(
	race varchar(32),
	bettor varchar(32),
	alo smallint,
	sai smallint,
	win varchar(32),
	cal varchar(32),
	id serial primary key
);
insert into src_stream.bets(race,bettor,alo,sai,win,cal) values('some','my',5,7,'ver','nor'),('some','you',12,6,'gul','mor');

create table if not exists src_stream.results(
	id serial primary key,
	race varchar(32) not null unique,
	alo smallint null,
	sai smallint null,
	win varchar(32) null,
	cal varchar(32) null
);
insert into src_stream.results(race) values
	('Bahrain'),
	('Saudi Arabia'),
	('Australia'),
	('Japan'),
	('China'),
	('Miami'),
	('Emilia Romagna'),
	('Monaco'),
	('Canada'),
	('Spain'),
	('Austria'),
	('United Kingdom'),
	('Hungary'),
	('Belgium'),
	('Netherlands'),
	('Italy'),
	('Azerbaijan'),
	('Singapore'),
	('USA'),
	('Mexico'),
	('Brazil'),
	('Las Vegas'),
	('Qatar'),
	('Abu Dhabi')
;
create view src_stream.points as
select
	results.id as id,
	results.race as race,
	bets.bettor as bettor,
	case when bets.alo= results.alo then 1 else 0 end as alo,
	case when bets.sai= results.sai then 1 else 0 end as sai,
	case when bets.win= results.win then 1 else 0 end as win,
	case when bets.cal= results.cal then 1 else 0 end as cal
from results
left join bets on results.race= bets.race
order by results.id;

create view src_stream.total as
select
	bettor,
	sum(alo) as alo,
	sum(sai) as sai,
	sum(win) as win,
	sum(cal) as cal,
	sum(alo+sai+win+cal) as tt
from src_stream.points
group by bettor;
