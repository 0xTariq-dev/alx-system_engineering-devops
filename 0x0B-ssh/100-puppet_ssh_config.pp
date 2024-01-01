#!/usr/bin/pup
# Script to Configure ssh client to
# reject passwd auth

include stdlib

file_line { 'Turn off passwd auth':
  ensure  => present,
  path    => '/etc/ssh/ssh_config',
  line    => '^\s*PasswordAuthentication no',
  replace => true,
}

file_line { 'Declare identity file':
  ensure  => present,
  path    => '/etc/ssh/ssh_config',
  line    => '^\s*IdentityFile ~/.ssh/school',
  replace => true,
}
