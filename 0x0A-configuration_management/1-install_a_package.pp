#!/usr/bin/pup
# Using Puppet, install flask(2.1.0) from pip3.
package { 'python3':
  ensure   => '3.8.10',
  provider => 'pip3',
}
package { 'Werkzeug ':
  ensure   => '2.1.1',
  provider => 'pip3',
}
exec { 'install_flask':
  command => '/usr/bin/pip3 install flask==2.1.0',
  require => [Package['python3'], Package['Werkzeug']],
}
