# Create a file called 'School' in '/tmp' directory and write some text into it.

file { 'School':
  path    => '/tmp/school',
  ensure  => 'file',
  content =>'I Love Puppet',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
}
