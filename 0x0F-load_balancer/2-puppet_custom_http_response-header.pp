# Manifest to add a custom HTTP header in Nginx with Puppet
exec { 'update':
  command => 'sudo sudo apt-get update -y',
  path    => ['/usr/bin', '/bin'],
  returns => [0,1]
}

exec { 'install':
  require => Exec['update'],
  command => 'sudo apt-get install nginx -y',
  path    => ['/usr/bin', '/bin'],
  returns => [0,1]
}

exec { 'header':
  require => Exec['install'],
  command => 'sudo sed -i "s/server_name _;/server_name _;\n\tadd_header X-Served-By \$hostname;/" /etc/nginx/sites-enabled/default',
  path    => ['/usr/bin', '/bin'],
  returns => [0,1]
}

exec { 'restart':
  require => Exec['header'],
  command => 'sudo service nginx restart',
  path    => ['/usr/bin', '/bin', '/usr/sbin'],
  returns => [0,1]
}
