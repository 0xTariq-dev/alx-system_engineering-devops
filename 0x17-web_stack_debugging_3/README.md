# Web Stack Debugging #3 Project.

## Requirements
in this project we are given a web server that is not working properly. We are to debug the server and fix it.
The web server is running on LAMP stack.
The PHP script wp-settings file is supposed to execute another script in the wb-includs directory but it is not doing so due to a typo in the name of the script.

## Tasks
0. `strace` is a useful tool to debug a program. For this task, we are to use `strace` to track the system calls that a program makes.
1. We are to fix the typo in the name of the script that the wp-settings file is supposed to execute.
2. We are to fix the server configuration file to allow the server to run the script that the wp-settings file is supposed to execute.

## File Descriptions
0. 0-strace_is_your_friend.pp - A Puppet manifest file that fixes the error discoverd with strance in the wb-settings file.

