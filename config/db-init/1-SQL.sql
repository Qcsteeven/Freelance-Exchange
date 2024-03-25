CREATE TABLE contacts (
	id SERIAL PRIMARY KEY,
	mail text NULL,
	telephone text NULL
);

CREATE TABLE users (
	id SERIAL PRIMARY KEY,
	is_customer boolean
);

CREATE TABLE profiles (
	id SERIAL PRIMARY KEY,
	owner integer REFERENCES users ON DELETE RESTRICT,
	contacts integer REFERENCES contacts ON DELETE RESTRICT,
	first_name text,
	second_name text NULL,
	skills text[]
);