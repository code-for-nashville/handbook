# How do I build…
*Resources for building and deploying common types of websites and applications.*

## a static site

[Github Pages](https://pages.github.com/) lets you host a static site right from your Github repository.  You can automate a build step, such as those required by a [Jekyll](https://jekyllrb.com/docs/quickstart/), [vue-cli](https://github.com/vuejs/vue-cli/), or [create-react-app](https://github.com/facebook/create-react-app) project, using [Travis CI’s Github Pages integration](https://docs.travis-ci.com/user/deployment/pages/).   You can use a PaaS like [Firebase](https://firebase.google.com/) for a fully featured backend.

## a Node.js app

[Glitch](https://glitch.com/) lets you develop and deploy live Node.js apps directly from the site for free, and keep your work in sync with a Github repository.  Glitch projects [come with a persistent filesystem](https://glitch.com/faq#db) so you can make real apps using databases like [LowDB](https://glitch.com/edit/#!/low-db) or [SQLite3](https://glitch.com/edit/#!/sqlite3-db?path=README.md:1:0).

## a web app

[Heroku](http://heroku.com/) lets you deploy web applications written in many languages with without managing infrastructure.  Code for America [sponsors qualified projects by covering their Heroku bills](http://brigade.codeforamerica.org/resources/software/heroku) - contact one of the CfN organizers and we can help with applying for sponsorship.

## a very complex web app

Cloud providers like [AWS](http://aws.amazon.com/), [Google Cloud](https://cloud.google.com/), or [DigitalOcean](https://www.digitalocean.com/) let you provision low-cost infrastructure for complex or special purpose applications.  [Use a tool like Terraform](http://terraform.io/) to 🐇declare ✨🎩your infrastructure - it’s worth the day or two [to learn by reading through the documentation](https://www.terraform.io/docs/index.html).  See the [inclucivics/terraform folder](https://github.com/code-for-nashville/inclucivics/tree/master/terraform) for an example that uses [AWS to run a scheduled Lambda function](https://www.terraform.io/docs/providers/aws/index.html), but [also consider using the DigitalOcean provider for a simpler setup.](https://www.terraform.io/docs/providers/do/r/droplet.html)

## a mobile app

**You found a** 🐛! [React Native](https://github.com/facebook/react-native) seems promising, but none of us know what we’re doing with mobile development, and we’d love your help filling this section in.  Comment if you’re interested!

[ ] 

