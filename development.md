# Development

The master branch of the handbook repo is published on the [Code For Nashville](https://github.com/code-for-nashville/code-for-nashville.github.io) website. The markdown is rendered into html using [Showdown.js](https://github.com/showdownjs/showdown).

To test how changes to the handbook will look rendered on the site you can serve the files using `static-server.py`. Then in `js/markdown.js` you can point the url to fetch the markdown file to the python server at `0.0.0.0:8000` instead of the github cdn.

The site paths for the documents should match the directory structure of this repo as the files are fetched dynamically based on the path.