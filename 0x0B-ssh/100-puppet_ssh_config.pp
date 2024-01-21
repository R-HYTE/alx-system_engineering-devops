# Ensure the ~/.ssh directory exists
file { '/home/your_username/.ssh':
  ensure => directory,
  mode   => '0700',
  owner  => 'ubuntu',
}

# Configure the SSH client
file_line { 'Ensure PasswordAuthentication is Disabled':
  ensure => 'present',
  path   => '/home/ubuntu/.ssh/config',
  line   => 'PasswordAuthentication no',
}

file_line { 'Declare IdentityFile for SSH Key':
  ensure => 'present',
  path   => '/home/ubuntu/.ssh/config',
  line   => 'IdentityFile ~/.ssh/school',
}
