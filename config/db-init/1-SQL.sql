-- В данной таблице еще не настроены связи между таблицами
-- В дальнейшем планируется исправить связи,
-- когда время дойдет до запросов удаления

CREATE TABLE contacts (
	id SERIAL PRIMARY KEY,
	email text NULL,
	telephone text NULL
);

CREATE TABLE users (
	id SERIAL PRIMARY KEY,
	is_customer boolean
);

CREATE TABLE sessions (
	id SERIAL PRIMARY KEY,
	owner integer REFERENCES users ON DELETE CASCADE,
	create_date timestamp,
	key text
);

CREATE TABLE profiles (
	id SERIAL PRIMARY KEY,
	contacts integer REFERENCES contacts ON DELETE RESTRICT,
	owner integer REFERENCES users ON DELETE RESTRICT,
	-- CASCADE don't work
	first_name text,
	second_name text NULL,
	skills text[]
);

CREATE TABLE companies (
	id SERIAL PRIMARY KEY,
	owner integer REFERENCES users ON DELETE CASCADE,
	contacts integer REFERENCES contacts ON DELETE RESTRICT,
	name text,
	description text
);

CREATE TABLE orders (
	id SERIAL PRIMARY KEY,
	customer integer REFERENCES users ON DELETE SET NULL,
	performer integer REFERENCES users ON DELETE SET NULL,
	status text,
	create_date text,
	start_date text NULL,
	close_date text NULL,
	category text,
	description text,
	technology_stack text[]
);

CREATE TABLE requests (
	id SERIAL PRIMARY KEY,
	performer integer REFERENCES users ON DELETE CASCADE,
	order_link integer REFERENCES orders ON DELETE CASCADE
);

CREATE TABLE chats (
	id SERIAL PRIMARY KEY,
	performer integer REFERENCES users ON DELETE RESTRICT,
	order_link integer REFERENCES orders ON DELETE CASCADE
);

CREATE TABLE messages (
	id SERIAL PRIMARY KEY,
	chat integer REFERENCES chats ON DELETE CASCADE,
	owner integer REFERENCES users ON DELETE RESTRICT,
	date timestamp,
	value text
);