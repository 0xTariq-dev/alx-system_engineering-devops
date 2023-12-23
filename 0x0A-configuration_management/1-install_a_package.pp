#!/usr/bin/pup
# Using Puppet, install flask(2.1.0) from pip3.
package { 'python':
  ensure   => '3.8.10',
  provider => 'apt',
}
package { 'Werkzeug ':
  ensure   => '2.1.1',
  provider => 'pip3',
}
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
