# alfred-github-repositories
[Alfred 4][1] workflow for opening your GitHub Repositories in your default browser.

# Installation
1) Install [alfred-github-repositories][2] workflow.
2) All further updates are handled automatically.
3) Requires a _python3_ interpreter to be installed (e.g. via a [Homebrew][4]).

## Usage
In Alfred, type `repos`. This initiate a repository retrieval process, which shows all your public and private GitHub Repositories.
Then, you could preview a selected repository content by pressing <kbd>⌘</kbd>+<kbd>y</kbd>, or open a selected repository in default browser by pressing <kbd>enter</kbd>.

![alfred-github-repositories-menu](doc/images/alfred-repos-menu.png?raw=true "")

Opening in default browser could be overridden, either by pressing the <kbd>⌘</kbd> key, or <kbd>⌥</kbd> key, or <kbd>⌃</kbd> key.

- The first one - <key>⌘</key> - instructs workflow to copy a repository clone URL to clipboard.
- The second one - <key>⌥</key> - instructs workflow to copy a repository CLI git clone command to clipboard.
- The last one - <key>⌃</key> - instructs workflow to open a repository in GitHub Client.

![alfred-github-repositories-submenu](doc/images/alfred-repos-submenu.png?raw=true "")

Repositories could be filtered by their names. Regular expressions (Python) are supported.

## Configuration
Before the first usage, you are required to fill the workflow variables.

Mandatory settings:
- `user` is your Github username,
- `personalToken` is your Github Personal Token created in your [user settings][3]. If you want to show your private repositories, not just the public ones, select the `repo scope` during the personal token generation.

Optional settings:
- `keyword` contains the main workflow keyword, which is used to start this workflow. By default, it's set to `repos`,
- `showStarStats` instructs to show the Stars count for the given repository. By default, it's set to `true`,
- `showForkStats` instructs to show the Forks count for the given repository. By default, it's set to `true`,
- `starPictogram` is a unicode pictogram for showing a Star count statistics. By default, it's set to `🎖`,
- `forkPictogram` is a unicode pictogram for showing a Star count statistics. By default, it's set to `ᛘ`. 

![alfred-github-repositories-submenu-stats](doc/images/alfred-repos-submenu-stats.png?raw=true "")

[1]: https://www.alfredapp.com/
[2]: https://github.com/vookimedlo/alfred-github-repositories/releases/latest
[3]: https://github.com/settings/tokens
[4]: https://brew.sh/
