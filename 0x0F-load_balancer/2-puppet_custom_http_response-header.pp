# Manifest to add a custom HTTP header in Nginx with Puppet
exec { 'apt-get update':
  command => '/usr/bin/apt-get update -y'
}

package { 'nginx':
         ensure => 'present',
         require => Exec['apt-get update']
}

exec { 'header':
     require => Exec['apt-get update'],
     path    => '/usr/bin:/bin',
     command => 'sed -i '/server_name _;/a add_header X-Served-By $hostname;' /etc/nginx/sites-available/default'
}

exec { 'start nginx':
     require => Exec['header'],
     path    => '/usr/bin:/bin',
     command => 'service nginx restart'
}
