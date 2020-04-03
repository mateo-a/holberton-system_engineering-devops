# Manifest to add a custom HTTP header in Nginx with Puppet
exec { 'apt-get update':
  command => '/usr/bin/apt-get update -y',
}
package {'nginx':
         ensure => 'present',
         require => Exec['apt-get update'],
}
file_line { 'http_header':
  path  => '/etc/nginx/nginx.conf'
  match => 'http {',
  line  => "http {\n\tadd_header X-Served-By \"${hostname}\";",
}
service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
exec {'restart nginx':
  command => '/usr/sbin/service nginx restart',
}
