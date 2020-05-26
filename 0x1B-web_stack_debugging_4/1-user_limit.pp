# Web stack set User Limit to holberton user and open a
# file without any error message
exec { 'fix_user_limit':
  command => 'sed -i "s/hard nofile 5/hard nofile 1048576/" /etc/security/\
  limits.conf; sed -i "s/soft nofile 4/soft nofile 1048576/" /etc/security/limits.conf',
  path    => ['/usr/bin', '/bin'],
}
