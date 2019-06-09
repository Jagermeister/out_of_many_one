# SQLite Basics

You can download a [command line shell](https://www.sqlite.org/cli.html) for SQLite to help you interrogate the schema and data. Typing `.help` will display the available commands and a brief description. Just `.open PATH\\TO\\DATABASE\\data.db` to have access to your database. I've used `.tables` to check which tables are available and `.lint fkey-indexes` to see a list of supporting indexes that could be created based on your foriegn keys.

For examples on the Python syntax/api, [the offical documentation](https://docs.python.org/3/library/sqlite3.html) seems straightforward.

## Primary Keys
SQLite has a built in integer, auto-incrementing primary key column named `rowid`. You can (should) create the first column of your table as `table_name_key INTEGER PRIMARY KEY` which will result in being an alias for `rowid` (always a 64-bit signed integer). Perfect! The `rowid` is the true primary key for the table and is used in the underlying B-tree storage enging. You don't want to use SQLite's `AUTOINCREMENT` keyword.
>The AUTOINCREMENT keyword imposes extra CPU, memory, disk space, and disk I/O overhead and should be avoided if not strictly needed. It is usually not needed.

https://www.sqlite.org/autoinc.html

## Table Column Information
`pragma table_info(TABLE_NAME);`
```sql
sqlite> pragma table_info(filer_type);
0|filer_type_key|INTEGER|0||1
1|filer_name|TEXT|1||0
2|is_senator|INTEGER|1||0
3|is_candidate|INTEGER|1||0
4|is_former_senator|INTEGER|1||0
```

## Date and Time Datatype
/!\\ Review still needed for trade-offs involved in the various date storage methods:
- TEXT as ISO8601 strings ("YYYY-MM-DD HH:MM:SS.SSS").
- REAL as Julian day numbers, the number of days since noon in Greenwich on November 24, 4714 B.C. according to the proleptic Gregorian calendar.
- INTEGER as Unix Time, the number of seconds since 1970-01-01 00:00:00 UTC.
