$base_packages = [ 'python3', 'python3-pip' ]

package { $base_packages:
  ensure => 'installed'
}

package { 'pip3':
  require  => Package[$base_packages],
  ensure   => latest,
  provider => 'pip3',
}

package { 'flask':
  ensure => '2.1.0',
  require  => Package[$base_packages],
  name     => 'flask',
  provider => 'pip3',
}
