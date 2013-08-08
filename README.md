This is a Start of a project who wants to record acts of douchery.
If you are interested in working on the project you are more than welcome.

Visit us at www.doucherism.com

*We are working with Django-CMS*

Following this tutorials

- http://blog.equip9.org/blog/2013/05/06/deploy-django-cms-to-heroku-and-amazon-s3
- https://devcenter.heroku.com/articles/django#start-a-django-app-inside-a-virtualenv

Requirements:
- VirtualBox
- Vagrant (< 1.1)
- chef-solo (< 11 on Host and Guest)
- librarian-chef

Installation Procedure
1. git clone this repo
2. run "librarian-chef install"
3. run "vagrant up"
4. run "vagrant ssh"
5. run "cd /vagrant"
6. run "export DATABASE_URL='postgres://postgres:password@localhost:5432/postgres'"
7. run "python manage.py syncdb --all && python manage.py migrate --fake"
8. run "foreman start"
9. open Browser to localhost:9091
