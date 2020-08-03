# Kills a process
exec { 'killing killmenow':
  command  => 'pkill killmenow',
  provider => 'shell',
}
