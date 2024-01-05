#!/usr/bin/pup
# Script to install nginx and configure a server.

# Install nginx
exec { 'update and install nginx':
  provider => 'shell',
  command  => 'apt-get update && apt-get install -y nginx',
}

# Create the index.html file
file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
  require => Exec['update and install nginx'],
}

# Create a server block.
exec { 'Edit default server block':
  provider => 'shell',
  command  => 'sed -i "s/server_name _;/server_name _;\n\trewrite ^\/redirect_me http:\/\/www.waza.org\/404 permanent;/g" \
  /etc/nginx/sites-available/default',
  require  => File['/var/www/html/index.html'],
}

# Start or restart nginx service
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => [
    Exec['Edit default server block'],
    Exec['update and install nginx'],
  ],
}
