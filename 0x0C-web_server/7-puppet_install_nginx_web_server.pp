# Install Nginx web server (w/ Puppet)
package { 'nginx':
  ensure => installed
}

file {'/var/www/html/index.html':
    content => 'Holberton School'
}

file_line { 'redirect':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'server_name _',
  line   => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;'
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx']
}
