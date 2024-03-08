#!/usr/bin/puppet
# This is a sample Puppet manifest for fixing a typo in a file a php file.

exec { 'fix wordpress typo':
  command  => "sudo sed -i 's/.phpp/.php/g' /var/www/html/wp-settings.php",
  provider => shell,
}

exec { 'restart apache':
  command  => 'sudo service apache2 restart',
  provider => shell,
  require  => Exec['fix wordpress typo'],
}
