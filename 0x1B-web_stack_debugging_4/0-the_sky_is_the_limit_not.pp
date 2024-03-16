# Increase the capacity for handling traffic by adjusting Nginx settings.

# Increase the ULIMIT of the default file
exec { '/etc/default/nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx', # Change ULIMIT value to 4096
  path    => '/usr/local/bin/:/bin/', # Specify path for sed command
  notify  => Exec['nginx-restart'], # Ensure Nginx restarts after ULIMIT change
}

# Restart Nginx
exec { 'nginx-restart':
  command     => 'nginx restart', # Restart Nginx service
  path        => '/etc/init.d/', # Specify path for service command
  refreshonly => true, # Restart Nginx only when notified by ULIMIT change
}
