myip
====

This is an experiment in a DIY replacement for icanhazip.com and the
like. It's intended to run in a Dokku instance. To set it up, run

```
dokku apps:create myip
dokku domains:set myip myip.<your domain>
dokku letsencrypt:enable myip
dokku ps:scale web=1
dokku nginx:set myip x-forwarded-for-value "\$http_x_forwarded_for"
```

then deploy by adding your Dokku remote and pushing to it, something
like

```
git add dokku dokku@dokku.<your domain>:myip
git push dokku develop
```
