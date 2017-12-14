# alfred-github-repositories
[Alfred 3][1] workflow for opening your GitHub Repositories in your default browser.

# Installation
1) Install [alfred-github-repositories][2] workflow.
2) All further updates are handled automatically.

## Usage
In Alfred, type `repos`. This initiate a repository retrieval process, which shows all your public and private GitHub Repositories.
Then, you could preview a selected repository content by pressing <kbd>⌘</kbd>+<kbd>y</kbd>, or open a selected repository in default browser by pressing <kbd>enter</kbd>.

![alfred-github-repositories-menu](doc/images/alfred-repos-menu.png?raw=true "")

![alfred-github-repositories-submenu](doc/images/alfred-repos-submenu.png?raw=true "")


## Configuration
Before the first usage, you are required to fill the workflow variables.

- `user` is your Github username,
- `personalToken` is your Github Personal Token created in your [user settings][3]. If you want to show your private repositories, not just the public ones, select the `repo scope` during the personal token generation.

[1]: https://www.alfredapp.com/
[2]: https://github.com/vookimedlo/alfred-github-repositories/releases/latest
[3]: https://github.com/settings/tokens
