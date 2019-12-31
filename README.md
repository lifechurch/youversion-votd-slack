# YouVersion Verse Of The Day Slack Bot &middot; [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com) [![GitHub license](https://img.shields.io/badge/license-Apache%202-blue.svg?style=flat-square)](https://github.com/lifechurch/youversion-votd-slack/blob/master/LICENSE)

> An [Open Digerati Project](https://opendigerati.com/)

The YouVersion Verse Of The Day Slack Bot can be used to bring the daily word of God into your slack workspace.

## Installing / Getting started

> Coming Soon!

Follow Slack's installing apps guideline found [here](https://slack.com/help/articles/202035138-add-an-app-to-your-workspace#install-apps)

Be sure to search for `YouVersion` in the [Slack App Directory](https://my.slack.com/apps)

## Developing

### Built With

---

#### Slack bot

* Python3.6
* [Python slackclient](https://github.com/slackapi/python-slackclient)
* [YouVersion API Client](https://github.com/jyksnw/yv-api-python)

#### Front-end

* TBD

### Prerequisites

---

You will need a YouVersion Developer API Token. This can be obtained from the [YouVersion API Developer Portal](https://developers.youversion.com/). Sign in with your existing YouVersion account. Please head over to <https://my.bible.com/sign-in> if you do not currently have a YouVersion account or if you log into YouVersion using Google or Facebook.

*Note: Currently the YouVersion API Developer Portal does not support Google or Facebook sign in.*

| *TODO*: Add instructions for obtaining Slack Bot token (either via OAth or directly through slack [ref](https://slack.dev/python-slackclient/auth.html))

You will also want to be sure to install the latest version of Python 3.6. If you on Linux (including Windows Subsytem for Linux) or macOS the suggested way to install is to use a tool called [pyenv](https://github.com/pyenv/pyenv). If on Windows, head over to [Python.org](https://www.python.org/downloads/) and download the latest version of Python 3.6 for Windows (at the time of writing this is version 3.6.9)

To get setup with [pyenv](https://github.com/pyenv/pyenv) run the following (lines starting with `$>` are commands to be run. Do not include the `$>` when running the command):

```bash
# Install pyenv if not already installed
$> curl https://pyenv.run | bash

# Verify pyenv was installed (note the version may be different for you)
$> pyenv --version
pyenv 1.2.14

# Verify all dependencies for pyenv have been met. Install any unmet dependcies with the system package manager (apt, yum, brew, etc...)
$> pyenv doctor

# Initialize pyenv and follow any intialization steps such as adding pyenv to your PATH
$> pyenv init

# Install Python (at the time of writting the project is targetting version 3.6.9 for development)
$> pyenv install 3.6.9
```

You will need an integrated developer environment (IDE) to do development work in. We suggest using [Visual Studio Code](https://code.visualstudio.com/) with the [Python plugin](https://code.visualstudio.com/docs/languages/python) installed. There is a convience script in the `scripts` directory of this project that be used to install all the suggested Visual Studio Code plugins for the project.

### Setting up Dev

---

Here's a brief intro about what a developer must do in order to start developing
the project further:

```shell
git clone git@github.com:lifechurch/youversion-votd-slack.git
cd youversion-votd-slack/
pyenv virtualenv
pyenv activate
pip install tox
```

And state what happens step-by-step. If there is any virtual environment, local server or database feeder needed, explain here.

### Building

If your project needs some additional steps for the developer to build the
project after some code changes, state them here. for example:

```shell
./configure
make
make install
```

Here again you should state what actually happens when the code above gets
executed.

### Deploying / Publishing

give instructions on how to build and release a new version
In case there's some step you have to take that publishes this project to a
server, this is the right time to state it.

```shell
packagemanager deploy your-project -s server.com -u username -p password
```

And again you'd need to tell what the previous code actually does.

## Versioning

We can maybe use [SemVer](http://semver.org/) for versioning. For the versions available, see the [link to tags on this repository](/tags).

## Configuration

Here you should write what are all of the configurations a user can enter when
using the project.

## Tests

Describe and show how to run the tests with code examples.
Explain what these tests test and why.

```shell
Give an example
```

## Style guide

Explain your code style and show how to check it.

## Api Reference

If the api is external, link to api documentation. If not describe your api including authentication methods as well as explaining all the endpoints with their required parameters.

## Database

Explaining what database (and version) has been used. Provide download links.
Documents your database design and schemas, relations etc...

## Licensing

State what the license is and how to find the text version of the license.
