# WilmingtonWebDev.github.io

## Development setup

The static site is developed using the [Pelican](http://docs.getpelican.com) static site generator.

### Running the development server

Install dependendencies in a virutalenv

```
pip install virtualenv
virtualenv ~/virtualenvs/wilwebdev
source ~/virtualenvs/wilwebdev/bin/activate
pip install -r requirements.txt -c requirements.lock
```

Start development server on port 8000
```
make devserver
```

Then browse to http://localhost:8000/ to view local version of site.

### Adding editing content

- All content can be found in the `./content` directory.
- Content is added by creating new Markdown files which contain metadata and content.
- Any content in saved in the `./pages/` directory will be compiled to seperate site pages.

For example the content directory might look like
```
./content/
│── 2016-10-29_first_article.md
│── 2016-10-30_second_article.md
└── pages
    └── about_page.md
```

**2016-10-29_first_article.md**
```
Title: An article Title
Date: 201-10-26 13:30:59
Authors: Tom Marks

Article content goes here!
```

**about_page.md**
```
Title: About
Date: 2016-10-29
Modified: 2016-10-29

About content goes here!
```

## Updating the live site

The following command will upload the build site to https://wilmingtonwebdev.github.io/

```
make github
```
