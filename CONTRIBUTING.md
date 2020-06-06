# How to contribute

#### **Do you intend to add a new command, tool or change an existing one?**
   * Suggest your change by creating a [pull Request to apolo-users-tools](https://github.com/eafit-apolo/apolo-user-tools/pull/new/master)
   * Ensure you follow the repository structure and the instructions to submit changes bellow. 
   * One of our team members in Apolo will review your contribution and send you feedback, if everything is in order we will deploy it on the cluster and make it available to all our users.

#### **Did you find a bug?**
   * Send us an email to <apolo@eafit.edu.co> with a brief description of the bug and how to replicate it. We will reach as soon as possible.
   * If you want to suggest a solution, open a new github pull request with the patch. Ensure the PR description clearly describes the problem and solution. Please follow the instruction for submitting changes.

#### **Did you fix whitespace, format code, or make a purely cosmetic patch?**
   * Send us an email to <apolo@eafit.edu.co> with a description of the change or patch. 
   * Changes that are cosmetic or do not add anything substantial to the repository will not be accepted via pull request.

## Submitting changes

Please send a [GitHub Pull Request to apolo-users-tools](https://github.com/eafit-apolo/apolo-user-tools/pull/new/master) with a clear list of what you've done (read more about [pull requests](http://help.github.com/pull-requests/)). When you send a pull request it is important to follow the directory structure of this repository and include all the elements needed for your contribution. For more information please check [README](README.md). Please follow our coding conventions (below) and make sure all of your commits are atomic (one feature per commit).

Always write a clear log message for your commits. One-line messages are fine for small changes, but bigger changes should look like this:

    $ git commit -m "A brief summary of the commit
    > 
    > A paragraph describing what changed and its impact."

## Coding conventions
   * If you are writing anything related with shell scripting please follow [Google's Shell Style Guide](https://google.github.io/styleguide/shellguide.html).
   * In case you are writing a command script: 
      * Include the name of your command in the description of the pull request.
      * Add a help message using the ``--help`` flag with a brief description of what the command does and a further explanation of the arguments if necessary. This is an example:
        ```
        $ command-apolo --help
        usage: command-apolo [-h]

        A custom utility to something

        optional arguments:
           -h, --help  show this help message and exit

        More information about the command.
        This command is part of apolo-users-tools, feel free to contribute
        https://github.com/eafit-apolo/apolo-user-tools
        ```

      * In all cases, please follow the directory structure of this repository and include the elements of your specific contribution.  

Thanks for reading this, we appreciate any improvement you made to this repository.

**Apolo Team**.

