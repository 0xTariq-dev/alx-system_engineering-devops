## 0x14-mysql
> This is a repository containing assignments for the 0x14-mysql project.
- The following tasks are present in this project:

Task 0: Install MySQL
Installing MySQL 5.7.x on both your web-01 and web-02 servers.
- The process of installing MySQL on the servers is done manually for the purpose of the project.
- Make sure that MySQL is running on both web-01 and web-02.
- Also, make sure that no error is returned when you log into MySQL from the command line.

Task 1: Let us in!
Create a MySQL user named holberton_user on both web-01 and web-02.
- The user should have all privileges on the database.
- The user should be created with the host name set to localhost.

Task 2: If only you could see what I've seen with your eyes
- Create a database named tyrell_corp on both web-01 and web-02.
- Make sure that holberton_user has all privileges on the tyrell_corp database.

Task 3: Quite an experience to live in fear, isn't it?
- Create a table named nexus6 in the tyrell_corp database on both web-01 and web-02.
- The table should have two columns: `id` (INT, auto-increment) and `name` (VARCHAR(256), not null).

Task 4: Setup a Primary-Replica infrastructure using MySQL
- Set up a Primary-Replica infrastructure using MySQL.
- The primary server is web-01 and the replica server is web-02.
- Set up the replica server so that it is synced with the primary server.

Task 5: MySQL backup
- Write a Bash script that generates a MySQL dump and creates a compressed archive out of it.
- The script should have the following requirements:
  - The MySQL dump must contain all the databases on the server.
  - The MySQL dump must be named `backup.sql`.
  - The MySQL dump file should be compressed to a `tar.gz` archive.
  - The script should have the following usage: `./5-mysql_backup.sh [mysql_root_password]`.
  - The script should return an error code if the `mysql_root_password` is not provided or incorrect.
