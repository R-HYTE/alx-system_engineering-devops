# Ensure the ~/.ssh directory exists
file { '/home/ubuntu/.ssh':
  ensure => directory,
  mode   => '0700',
  owner  => 'ubuntu',
}

# Configure the SSH client
file { '/home/ubuntu/.ssh/config':
  ensure  => file,
  mode    => '0600',
  owner   => 'ubuntu',
  content => "\
Host 54.172.171.23
    IdentityFile ~/.ssh/school
    PasswordAuthentication no
",
}
