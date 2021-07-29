# dio-desafio-dataproc

# Digital Innovation One

Código criado para utilização junto a plataforma da Digital Innovation One


## Desafio GCP Dataproc

O desafio faz parte do curso na plataforma da Digital Innovation One:

__*Criando um ecossitema Hadoop totalmente gerenciado com Google Cloud Platform*__

O desafio consiste em efetuar um processamento de dados utilizando o produto Dataproc do GCP. Esse processamento irá efetuar a contahem das palavras de  __*FILMES*__ e informar quantas vezes cada __*PERSONAGEM*__ aparece nos mesmos.


Nesse caso, utilizei as transcrições de audio dos filmes da Disney/Pixar Toy Story e Toy Story 2, disponíveis em https://transcripts.fandom.com/wiki/Toy_Story e https://transcripts.fandom.com/wiki/Toy_Story_2


### Etapas do Desafio

1. Criar um bucket no Cloud Storage __*OK*__
2. Atualizar o arquivo ```contador.py``` com o nome do Bucket criado nas linhas que contém ```{SEU_BUCKET}```. __*OK - gs://desafiodata/...*__
3. Fazer o upload dos arquivos ```contador.py``` e ```livro.txt``` para o bucket criado (instruções abaixo)
    - https://cloud.google.com/storage/docs/uploading-objects

4. Utilizar o código em um cluster Dataproc, executando um Job do tipo PySpark chamando ```__*OK - gs://desafiodata/...contador.py*__```
5. O Job irá gerar uma pasta no bucket chamada ```resultado```. Dentro dessa pasta o arquivo ```part-00000``` irá conter a lista de palavras e quantas vezes ela é repetida em todos __* os FILMES*__.

### Entrega do Resultado

1. Criar um repositório no GitHub. __*OK*__ 
2. Criar um arquivo chamado ```resultado.txt```. Dentro desse arquivo, colocar as  ̶1̶0̶ ̶p̶a̶l̶a̶v̶r̶a̶s̶ __*QUAIS PERSONAGENS*__  que mais aparecem nos __*FILMES*__, de acordo com o resultado do Job. Para isso, utilizei o script ```characters.py``` para alterar a saída do job e gerar arquivo combinando os nomes que apareciam mais de uma vez, por motivo de pontuação, sotaques na transcrição etc.__*OK*__
3. Inserir os arquivo ```resultado.txt``` e ```part-00000``` no repositório e informar na plataforma da Digital Innovation One. __*OK*__

---


