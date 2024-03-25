-- В данной таблице еще не настроены связи между таблицами
-- В дальнейшем планируется исправить связи,
-- когда время дойдет до запросов удаления

CREATE TABLE contacts (
	id SERIAL PRIMARY KEY,
	mail text NULL,
	telephone text NULL
);

CREATE TABLE users (
	id SERIAL PRIMARY KEY,
	is_customer boolean
);

CREATE TABLE sessions (
	id SERIAL PRIMARY KEY,
	owner integer REFERENCES users ON DELETE RESTRICT,
	key text
);

CREATE TABLE profiles (
	id SERIAL PRIMARY KEY,
	owner integer REFERENCES users ON DELETE RESTRICT,
	contacts integer REFERENCES contacts ON DELETE RESTRICT,
	first_name text,
	second_name text NULL,
	skills text[]
);

CREATE TABLE companies (
	id SERIAL PRIMARY KEY,
	owner integer REFERENCES users ON DELETE RESTRICT,
	contacts integer REFERENCES contacts ON DELETE RESTRICT,
	name text,
	description text
);

CREATE TABLE orders (
	id SERIAL PRIMARY KEY,
	customer integer REFERENCES users ON DELETE RESTRICT,
	performer integer REFERENCES users ON DELETE RESTRICT,
	status text,
	create_date timestamp,
	start_date timestamp NULL,
	close_date timestamp NULL,
	category text,
	description text,
	technology_stack text[]
);

CREATE TABLE chats (
	id SERIAL PRIMARY KEY,
	performer integer REFERENCES users ON DELETE RESTRICT,
	order_link integer REFERENCES orders ON DELETE RESTRICT
);

CREATE TABLE messages (
	id SERIAL PRIMARY KEY,
	chat integer REFERENCES chats ON DELETE RESTRICT,
	owner integer REFERENCES users ON DELETE RESTRICT,
	date timestamp,
	value text
);