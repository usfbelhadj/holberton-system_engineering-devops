# Puppet script

exec { 'change ulimit':
  command => "sed -i 's/15/2000/g' /etc/default/nginx",
  path    => '/bin',
}

-> exec { 'nginx restart':
  command => 'nginx restart',
  path    => '/etc/init.d/',
}
