begin transaction;

create table Todo (
    id serial primary key,
    task varchar not null,
    done boolean not null default false
);
commit;