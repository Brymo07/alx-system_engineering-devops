# fixes bug in wp-settings.php file
exec { 'sed -i "s/.phpp/.php/g" /var/www/html/wp-settings.php':
  path => '/usr/bin:/usr/sbin:/bin',
}
-> exec {'restart service':
  command => '/usr/sbin/service apache2 restart',
}
