# Mardown para plataforma Medium

Converta um arquivo markdown para ser publicado na plataforma Medium.

1. Instalar mdium.

    ```python
    pip install mdium
    ```

2. Criar o token de integração com o Medium

    Acesse [https://medium.com/me/settings](https://medium.com/me/settings) e na seção Integration tokens crie o token que será acessado pelo mdium.

3. Executar o comando abaixo para configurar o mdium com o token. Será criado o arquivo ~/.mdium contendo o token e o ID di usuário.

    ```python
    mdium init <token-medium>
    ```

4. Modificar os arquivos mardown conforme o exemplo abaixo.

    ```text
    ---
    title: Titulo do artigo
    tags: ['algumas', 'tags', 'do artigo']
    status: draft
    ---

    [Conteúdo markdown aqui.]
    ```

5. Publicar o arquivo markdown para o Medium executando o comando abaixo.

    ```cmd
    $ mdium publish path/to/markdown.md
    
    Done! Your post has been published at https://medium.com/<usuario>/<id-artigo>
    ```

Alguns recursos do markdown não podem ser convertidos para o Medium, como por exemplo, tabelas. Neste caso, a solução é dar um print na tabela, ou converter em uma tabela ascii como neste link. Outra solução é criar uma tabela no Airtable e postar o link de compartilhamento no Medium.

## Referências

[https://ajuda.gitlab.io/guia-rapido/markdown/markdown-to-medium/](https://ajuda.gitlab.io/guia-rapido/markdown/markdown-to-medium/)

[https://medium.com/@icyphox/mdium-publish-your-markdown-to-medium-from-the-cli-79906ef6b16b](https://medium.com/@icyphox/mdium-publish-your-markdown-to-medium-from-the-cli-79906ef6b16b)
