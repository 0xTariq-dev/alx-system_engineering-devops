include stdlib

file_line { 'Turn off password authentication':
  path  => '/etc/ssh/ssh_config',
  line  => 'PasswordAuthentication no',
  match => '^\s*PasswordAuthentication no',
}

file_line { 'Set IdentityFile':
  path  => '/etc/ssh/ssh_config',
  line  => 'IdentityFile ~/.ssh/school',
  match => '^\s*IdentityFile',
}
