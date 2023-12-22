#!/usr/bin/pup
# Using Puppet, install flask(2.1.0) from pip3.
package { 'python3-flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
