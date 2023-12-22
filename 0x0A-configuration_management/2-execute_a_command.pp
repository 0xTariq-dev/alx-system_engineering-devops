#!/usr/bin/pup
# A puppet manifest to kill a process named "killmenow".
exec { 'killmenow':
  command  => 'pkill killmenow',
  provider => 'shell',
}
