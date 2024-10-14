# Cocreation Planet

This site shows the cocreation planet for use in courses

# Jekyll website source
Theme bootstrap5-creative-jekyll.

Ported the current version of [Creative Theme](https://startbootstrap.com/theme/creative) by [Start Bootstrap](https://github.com/StartBootstrap) into Jekyll.

`index.html` uses the `home` layout defined in `/_layouts/home.html` and its contents are defined in `/_includes`


## QuickStart

### Local website testing
- For local testing use the lines
```
bundle exec jekyll serve --config _config.yml,_config_dev.yml
```
- You can then test the site locally in the browser via: `http://localhost:4000`

### Production site rollout

- For production, the google analytics must be included. Use build lines:
```
JEKYLL_ENV=production bundle exec jekyll build --config _config.yml
```
- The site is hosted on github pages: [cocreationplanet](https://bmcage.github.io/cocreationplanet/), and will be served also via the [ExtenDT2 site](https://extendt2.eu/).