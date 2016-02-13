stage { 'first':
    before => Stage['main'];
}

class prepare {
    class { 'apt':
      update => {
        frequency => 'always',
      },
    }
    class { 'python' :
      version    => 'system',
      pip        => true,
      dev        => true,
      virtualenv => true,
      gunicorn   => true,
    }
}
class { 'prepare':
    stage => first;
}

include prepare


$sysPackages = ['git', 'curl']
package { $sysPackages:
  ensure => "installed",
  require  => Class['prepare']
}


class { 'postgresql::server':
    ip_mask_allow_all_users    => '0.0.0.0/0',
    listen_addresses           => '*',
    postgres_password          => 'postgres',
}

postgresql::server::db { 'codethon_db':
  user     => 'codethon_user',
  password => postgresql_password('codethon_user', 'codethon_pass');
}
package { 'python-psycopg2':
    ensure => installed,
  }

package {
    "django":
        ensure => "1.9",
        provider => pip;
    "django-bootstrap3":
        ensure => "installed",
        provider => pip;
    "djangorestframework":
        ensure => "installed",
        provider => pip;
    "python-daemon":
        ensure => "installed",
        provider => pip;
    "pika":
        ensure => "0.9.8",
        provider => pip;
    "Sphinx":
        ensure => "installed",
        provider => pip;
    "Pillow":
        ensure => "2.9.0",
        provider => pip;
    "dj_static":
        ensure => "installed",
        provider => pip;
    "django-toolbelt":
        ensure => "installed",
        provider => pip;
    "six":
        ensure => "1.9.0",
        provider => pip;
    "dj_database_url":
        ensure => "installed",
        provider => pip;
    "django-tables2":
        ensure => "installed",
        provider => pip;
}
