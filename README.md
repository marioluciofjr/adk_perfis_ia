# adk_perfis_ia
Multiagentes em ADK para resolver problemas com base em x horas.

![license - MIT](https://img.shields.io/badge/license-MIT-green)
[![site - prazocerto.me](https://img.shields.io/badge/site-prazocerto.me-230023)](https://prazocerto.me)
[![linkedin - @marioluciofjr](https://img.shields.io/badge/linkedin-marioluciofjr-blue)](https://linkedin.com/in/marioluciofjr)

## Índice

* [Introdução](#introdução)
* [Estrutura do projeto](#estrutura-do-projeto)
* [Tecnologias utilizadas](#tecnologias-utilizadas)
* [Requisitos](#requisitos)
* [Como obter a API KEY no Google AI Studio](#como-obter-a-api-key-no-google-ai-studio)
* [Como executar](#como-executar)
* [Links úteis](#links-úteis)
* [Contribuições](#contribuições)
* [Licença](#licença)
* [Contato](#contato)

## Introdução

Este projeto apresenta uma coleção de agentes inteligentes especializados em resolver problemas utilizando os recursos do modelo `gemini-2.0-flash`. Cada agente possui perfil único, inspirado em 10 arquétipos. Com instruções detalhadas e ferramentas específicas, a solução integra pesquisas, análises e execução de tarefas, garantindo abordagens diversificadas para desafios propostos pelos usuários.

## Estrutura do projeto

A ideia deste projeto de multiagentes surgiu do post ["Qual é o seu tipo de perfil de quem usa IA?"](https://www.linkedin.com/posts/giomangoni_tipos-de-perfis-de-quem-usa-ia-activity-7334255562668343296-q-5p?utm_source=share&utm_medium=member_desktop&rcm=ACoAACHvXJYBKyTyP1ggw536I9ZWCnCwD7LTax0), da Gio Mangoni, consultora de IA na Adapta.

Como o post tem uma estrutura de 10 arquétipos de possíveis usuários de inteligência artificial, eu utilizei essa premissa para desenvolver um fluxo sequencial de mutiagentes com a arquitetura do [ADK (Agent Development Kit)](https://google.github.io/adk-docs/), do Google. É apenas um projeto para fins didáticos, de modo que sirva para estudar um pouco mais sobre o desenvolvimento de agentes inteligentes.

Logo abaixo, confira a breve descrição de cada agente desse fluxo sequencial.

### automatizador
**Descrição**: Agente que automatiza processos, integrando diversas ferramentas de API e webhooks.\
**O que faz**: Pesquisa soluções, organiza fluxos e automatiza ações utilizando resultados do Google Search.\
**Como pode ajudar a pessoa usuária**: Auxilia na identificação de formas práticas para otimização e automação de tarefas, economizando tempo e otimizando processos.

### ai_first
**Descrição**: Agente multifuncional que atua como conselheiro, personal stylist e amigo.\
**O que faz**: Conta histórias e oferece soluções empáticas e criativas para problemas cotidianos.\
**Como pode ajudar a pessoa usuária**: Ajuda a pessoa a lidar emocionalmente com desafios, oferecendo insights e narrativas motivadoras.

### multitool
**Descrição**: Agente que domina diversas ferramentas de IA e realiza curadoria de soluções tecnológicas.\
**O que faz**: Pesquisa e recomenda múltiplas ferramentas de IA dos últimos meses, com justificativas detalhadas.\
**Como pode ajudar a pessoa usuária**: Proporciona uma visão ampla das melhores soluções disponíveis, ajudando a escolher a ferramenta ideal para o problema apresentado.

### gestora
**Descrição**: Agente com perfil analítico e estratégico, focado em métricas e impactos.\
**O que faz**: Utiliza a Matriz de Eisenhower para categorizar tarefas e planejar ações de forma estruturada.\
**Como pode ajudar a pessoa usuária**: Auxilia na organização do tempo e priorização de tarefas, garantindo uma abordagem metódica e eficiente para resolver problemas.

### cetico
**Descrição**: Agente cético que questiona o uso excessivo de IA generativa e defende métodos tradicionais.\
**O que faz**: Sugere soluções analógicas e critica a dependência excessiva da tecnologia, sempre com humor ácido.\
**Como pode ajudar a pessoa usuária**: Oferece uma perspectiva crítica e alternativas simples para resolução de problemas, evitando um uso desnecessário da tecnologia.

### sensei
**Descrição**: Agente mestre em engenharia de prompt e refinamento de instruções para IA.\
**O que faz**: Sugere o melhor prompt possível, otimizando a entrada para que a IA gere respostas precisas e contextualizadas.\
**Como pode ajudar a pessoa usuária**: Melhora a qualidade das interações com a IA ao fornecer templates e técnicas de engenharia de prompt, resultando em respostas mais eficazes.

### criadora
**Descrição**: Agente focado em criatividade e inovação para desenvolver projetos com IA generativa.\
**O que faz**: Estrutura passos de execução de projetos por meio de tabelas e esquemas, estimulando o brainstorm.\
**Como pode ajudar a pessoa usuária**: Inspira e organiza ideias, ajudando a elaborar estratégias e fluxos criativos para resolver desafios de forma inovadora.

### executor
**Descrição**: Agente prático e orientado para a ação, com foco em produtividade.\
**O que faz**: Analisa problemas, recomenda tarefas e utiliza a tool produtividade para distribuir o tempo idealmente.\
**Como pode ajudar a pessoa usuária**: Facilita a execução de projetos, organizando tarefas e garantindo que as atividades sejam realizadas de forma eficiente.

### evangelizador
**Descrição**: Agente inspirador que prega os benefícios da IA generativa.\
**O que faz**: Orienta com analogias e dicas, incentivando a divulgação e compartilhamento de conhecimentos sobre IA.\
**Como pode ajudar a pessoa usuária**: Motiva a adoção da IA e amplia a visão sobre como essa tecnologia pode transformar processos, promovendo aprendizado e engajamento.

### artista
**Descrição**: Agente especializado em design e geração de imagens, utilizando técnicas avançadas de engenharia de prompt.\
**O que faz**: Cria prompts para imagens, explorando métodos 3W1H e traduzindo-os para múltiplos idiomas com ajustes de qualidade.\
**Como pode ajudar a pessoa usuária**: Transforma ideias em visuais impactantes, auxiliando na criação de conteúdos gráficos de alta qualidade para diversas finalidades.

## Tecnologias utilizadas

<div>
  <img align="center" height="60" width="80" src="https://github.com/user-attachments/assets/63e3b960-3dc5-48fc-a300-b3104430235f" />&nbsp;&nbsp;&nbsp
  <img align="center" height="60" width="80" src="https://github.com/user-attachments/assets/18c95cc3-d8bc-486c-b0cf-b5d128980176" />&nbsp;&nbsp;&nbsp
  <img align="center" height="60" width="80" src="https://github.com/user-attachments/assets/31ed57e7-f4b7-4d86-9373-668a38f8db17" />&nbsp;&nbsp;&nbsp
  <img align="center" height="60" width="80" src="https://github.com/user-attachments/assets/0324b2d2-c9f4-4c2e-ba62-703a7f346de6" />&nbsp;&nbsp;&nbsp
  <img align="center" height="60" width="80" src="https://github.com/user-attachments/assets/76e7aca0-5321-4238-9742-164c20af5b4a" />&nbsp;&nbsp;&nbsp    
</div><br><br>

* ADK (Agent Development Kit);
* Visual Studio Code
* Google AI Studio
* Gemini
* Python

## Requisitos

Para utilizar este projeto, você precisa de:

- **Conta Google**: para acessar o Google AI Studio
- **Chave de API do Google AI Studio (Gemini API)**: instruções para obtenção abaixo
- **IDE**: para realizar o projeto escolhi o VS Code, mas pode ser outra da sua preferência (Cursor, Windsurf etc.)
- **UV**: instalador rápido de pacotes python

## Como obter a API KEY no Google AI Studio

Para utilizar este código, você precisará de uma chave de API do Google Gemini:

1. Acesse o [Google AI Studio](https://ai.dev/app/apikey)
2. Faça login com sua conta Google
3. Clique no botão "Criar chave de API"
4. Aceite os termos de serviço, se solicitado
5. Copie a chave gerada e guarde-a em local seguro

> [!IMPORTANT]
> Atualmente, o Google AI Studio oferece um uso gratuito da API para testes. Sobre demais detalhes da API do Gemini, leia a [documentação oficial](https://ai.google.dev/gemini-api/docs/pricing?hl=pt-br#:~:text=O%20uso%20do%20Google%20AI,em%20todos%20os%20pa%C3%ADses%20dispon%C3%ADveis). Caso você não queira utilizar o Gemini, pesquise como obter a API KEY do modelo generativo de sua preferência.

## Como executar

1. Instale o VS Code se ainda não tiver em sua máquina (confira o link na seção [`Links úteis`](#links-úteis));
2. No cabeçalho deste repositório, clique no botão `<> Code`, que fica do lado de `Add file`. Escolha a opção 'Download ZIP';
3. Descompacte o arquivo na sua máquina na pasta de sua preferência;
4. Abra o VSCode e ache a sua pasta com o atalho `CTRL + O` (File > Open Folder);
5. Abra o terminal com o atalho `CTRL + J`;
6. Caso ainda não tenha o uv instalado, faça isso com o comando:
   ```powershell
   pip install uv
   ```
7. Crie o ambiente virtual com o comando:
   ```powershell
   uv venv
   ```
8. Ative o ambiente virtual com o comando (no Windows):
   ```powershell
   .venv\Scripts\activate
   ```
9. Coloque a api_key, que pegou no Google AI Studio, no seu arquivo `.env`:
    ```env
    GOOGLE_API_KEY=sua_api_key
    ```
10. Volte ao terminal e digite o comando:
    ```powershell
    adk web
    ```
11. Aparecerá essa informação no seu terminal. Basta clicar em `CTRL`e depois no link que aparece em `http://localhost:8000`:
    
    ![Image](https://github.com/user-attachments/assets/5ec45cbd-38f8-4e67-b1fc-286b509141f9)

12. Logo em seguida abrirá uma aba no seu navegador que tem essa interface:

    ![Image](https://github.com/user-attachments/assets/b5d2bfa7-e368-4436-97c7-f6ead8f29457)

13. Basta digitar em `Type a message`:
    ```prompt
    Problema: relate um problema pessoal ou profissional
    Horas: quantidade de horas que focará em resolver esse problema (inforrme apenas o número. Exemplo: "Horas: 5")
    ```

## Links úteis

* [Documentação oficial do ADK (Agent Development Kit)](https://google.github.io/adk-docs/) - Tudo que você precisa saber sobre o ADK do Google;
* [Como instalar o VSCode](https://code.visualstudio.com/download) - Link direto para download (retorne para a seção [`Como executar`](#como-executar))
* [O que são agentes de IA?](https://www.ibm.com/br-pt/think/topics/ai-agents) - Explicação da IBM sobre agentes inteligentes de IA;
* [6 segredos do GitHub Copilot no VSCode](https://youtu.be/FaR6tQ1VMnc?si=vvtBvtGKnhNmline) - vídeo do canal `Código Fonte TV`sobre o GitHub Copilot no VSCode, com explicação bem didática a respeito do assunto;
* [O que é uma API?](https://www.alura.com.br/artigos/api) - Guia da Alura sobre APIs;
* [venv — Criação de ambientes virtuais](https://docs.python.org/pt-br/3/library/venv.html) - Explicação completa de como funcionam os venvs
* [Features do UV](https://docs.astral.sh/uv/getting-started/features/) - algumas funcionalidades para utilizar o uv no terminal da melhor maneira;
* [Agentes de IA poderosos com o Google ADK](https://www.youtube.com/watch?v=NkIZgBvA6G4&list=PLbmt8d_ueDMWHIv-HgdM532MLFSju6W2D&ab_channel=Sandeco) - playlist de vídeos do canal Sandeco sobre o framework ADK.

## Contribuições

Contribuições são bem-vindas! Se você tem ideias para melhorar este projeto, sinta-se à vontade para fazer um fork do repositório. Deixei o arquivo [`tools.py`](https://github.com/marioluciofjr/adk_perfis_ia/blob/main/adk_perfis_ia/perfis_ia/tools.py) com lacunas para outras pessoas criarem tools diferenciadas para os agentes.

## Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](https://github.com/marioluciofjr/adk_perfis_ia/blob/main/LICENSE) para detalhes.

## Contato
    
Mário Lúcio - Prazo Certo®
<div>  	
  <a href="https://www.linkedin.com/in/marioluciofjr" target="_blank"><img src="https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white"></a> 
  <a href = "mailto:marioluciofjr@gmail.com" target="_blank"><img src="https://img.shields.io/badge/-Gmail-%23333?style=for-the-badge&logo=gmail&logoColor=white"></a>
  <a href="https://prazocerto.me/contato" target="_blank"><img src="https://img.shields.io/badge/prazocerto.me/contato-230023?style=for-the-badge&logo=wordpress&logoColor=white"></a>
</div> 
