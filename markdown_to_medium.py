# Mardown para plataforma Medium

# Convertendo um arquivo markdown para ser publicado na plataforma Medium.
    # Instalar mdium.
    # pip install mdium

# Criar o token de integração com o Medium. 
    # Acesse https://medium.com/me/settings e na seção Integration tokens crie o token que será acessado pelo mdium.

# Executar o comando abaixo para configurar o mdium com o token. Será criado o arquivo ~/.mdium contendo o token e o ID di usuário.

# mdium init <token-medium>
# Modificar os arquivos mardown conforme o exemplo abaixo. Se quiser pulicar sem antes aprovar o rascunho mude o status para status: public.

# ---
# title: Titulo do artigo
# tags: ['algumas', 'tags', 'do artigo']
# status: draft
# ---

# ## conteúdo markdown aqui
# Publicar o arquivo markdown para o Medium executando o comando abaixo. Depois o arquivo markdown não é mais necessário.


# $ mdium publish path/to/markdown.md

# Done! Your post has been published at https://medium.com/<usuario>/<id-artigo>
# Alguns recursos do markdown não podem ser convertidos para o Medium, como por exemplo, tabelas. Neste caso, a solução é dar um print na tabela, ou converter em uma tabela ascii como neste link. Outra solução é criar uma tabela no airtable e postar o link de compartilhamento no Medium.

# Referências¶
# https://medium.com/@icyphox/mdium-publish-your-markdown-to-medium-from-the-cli-79906ef6b16b
