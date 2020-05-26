# Web stack debugging Nginx is not working properly under pressure (a big number of requests)
exec { 'fix_ulimit_Nginx':
  command => 'sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4096\"/" /etc/default/nginx; sudo service nginx restart',
  path    => ['/usr/bin', '/bin'],
}
