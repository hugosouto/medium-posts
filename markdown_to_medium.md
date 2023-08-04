# Markdown for Medium Platform

Convert a markdown file for publication on the Medium platform.

1. Install *mdium*.

    ```python
    pip install mdium
    ```

2. Create the integration token with Medium.

    Visit [https://medium.com/me/settings](https://medium.com/me/settings) and
    in the Integration tokens section create the token that will be accessed by
    *mdium*.

3. Execute the command below to configure *mdium* with the token.

    The file ~/.mdium will be created, containing the token and the user ID.

    ```python
    mdium init <medium-token>
    ```

4. Modify the markdown files according to the example below.

    ```markdown
    ---
    title: Article title
    tags: ['some', 'article', 'tags']
    status: draft
    ---

    [Markdown content here.]
    ```

5. Publish the markdown file to Medium by executing the command below.

    ```bash
    $ mdium publish path/to/markdown.md
    
    Done! Your post has been published at https://medium.com/<user>/<article-id>
    ```

Some markdown features cannot be converted to Medium, such as tables. In this
case, the solution is to take a screenshot of the table, or convert it into an
ASCII table like in this link. Another solution is to create a table in Airtable
and post the sharing link on Medium.

## References

[https://help.gitlab.com/quick-start/markdown/markdown-to-medium/](https://help.gitlab.com/quick-start/markdown/markdown-to-medium/)

[https://medium.com/@icyphox/mdium-publish-your-markdown-to-medium-from-the-cli-79906ef6b16b](https://medium.com/@icyphox/mdium-publish-your-markdown-to-medium-from-the-cli-79906ef6b16b)
