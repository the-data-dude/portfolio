## Crawler de informações do site Canaltech

#### O crawler foi feito de uma forma bem simplista, foi dado 7 dias para o desenvolvimento de algo mais robusto, porém tive só tive efetivamente um dia para olhar e estou enferrujado em muita coisa... Atualmente eu trabalho mais fazendo processos de ETL usando pyspark, disponibilizando informações para equipes de negócio.

#### O Objetivo principal aqui é ler as noticias da sessão "últimas noticias", para criar um algoritmo simples de coleta "near real time" das informações disponibilizadas no portal

#### O arquivo naive_nrt_news.py é o arquivo principal dessa aplicação, ao executar, a cada 2 minutos ele irá ver no site se há novas noticias e adicionará as informações no arquivo canaltech_news.csv.

#### As informações disponibilizadas no csv são:
- article_url : url do artigo;
- article_title : titulo do artigo;
- article_category : categoria do artigo;
- article_author : autor do artigo

#### O algoritmo também disponibiliza o conteúdo do artigo, mas como essa aplicação inicial foi feita pensando em um simples arquivo .csv para armazenar as informações, decidi não armazenar. Mas deixei a informação disponível para melhorias futuras do projeto.

### Problemas encontrados na elaboração do projeto:
- Não consegui rodar o docker no windows, mesmo usando as configurações do WSL2 disponibilizadas no site da Microsoft e seguindo alguns tutoriais no youtube;
- Dificuldade em coletar os comentários e carregar mais do que 12 artigos, pois é necessário interação com o site para carregar mais conteúdos e para carregar os comentários (o que pode ser resolvido usando o selenium ao invés do beautifulsoup). Acabei não coletando os comentários, mas usei eles para exemplificar possíveis análises mencionadas mais a baixo neste readme

### Como o projeto pode ficar melhor e mais escalável?
- Passar a aplicação para rodar em um ambiente docker;
- Criar um container docker com a imagem do MongoDB para adicionar as informações, inclusive com o conteúdo do artigo, facilitando a busca por conteúdo relevante;
- Criar mais crawlers de portais concorrentes, para conseguirmos realizar comparações entre eles;
- Passar a estrutura para o Google Cloud Plataform;
- Criar um fluxo no dataflow da GCP para disponibilizar as informações do MongoDB no BigQuery, facilitando exploração e plotagem das informações por ferramentas de BI ou até mesmo no próprio Google Data Studio

### Métricas relevantes que podem ser tiradas desse projeto:
- Autores mais relevantes por portal e por categoria de assunto (usando #likes e #comentarios no post como critério de relevância);
- Número de noticias por hora por portal e por categoria;
- Mapa de calor por portal, categoria e autor;
- Correlação entre noticias por hora e número de likes/comentários, para ver se a velocidade de publicação de conteúdo corre junto com a qualidade do que é publicado
- Palavras mais frequentes por categoria e autor, identificando possíveis gatilhos de comunicação ou vicios de escrita

