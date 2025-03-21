# Marketing AI Workflow

## Introdução
O **Marketing AI Workflow** é um projeto que automatiza a criação de conteúdo de marketing utilizando uma abordagem modular baseada em múltiplos agentes de inteligência artificial. Com uma arquitetura inspirada em fluxos de trabalho distribuídos, o sistema gera estratégias, cria e revisa conteúdos e até produz elementos visuais, culminando na simulação de publicação de postagens (por exemplo, no LinkedIn). Todo o processo é orquestrado por uma cadeia de agentes que garantem a coerência, conformidade e alinhamento com as diretrizes da marca.

## Arquitetura do Projeto
O projeto é composto por três módulos principais:

- **agents.py**  
  Este arquivo define os agentes e as tarefas que compõem o fluxo de criação de conteúdo. Entre as funções destacam-se:
  - **StrategyBriefingAgent**: Analisa os dados da empresa e gera um briefing de marketing estruturado em JSON.
  - **Agents_Chain**: Coordena a execução dos agentes responsáveis pela geração de ideias, criação textual, revisão, otimização de engajamento, geração de criativos visuais e simulação de publicação.

- **helpers.py**  
  Contém funções utilitárias para:
  - Limpeza e tratamento da saída dos agentes.
  - Salvamento de arquivos (como o briefing de estratégia) em formato JSON.
  - Leitura de dados específicos de arquivos (por exemplo, regras gerais e briefings salvos).

- **main.ipynb**  
  Um notebook que demonstra o fluxo completo do projeto. Nele:
  - São configurados o ambiente (carregamento de variáveis de ambiente, logging, etc.).
  - São importados os módulos e funções.
  - O fluxo de trabalho é executado utilizando dados reais de uma empresa (exemplo: TechNova) e regras definidas para a criação de conteúdo.

## Como Funciona
O fluxo de trabalho é dividido em diversas etapas, cada uma gerenciada por um agente especializado:

1. **Briefing de Estratégia**  
   - O `StrategyBriefingAgent` processa os dados da empresa para criar um documento de briefing de marketing em formato JSON.

2. **Geração de Ideia para Tema**  
   - O agente de ideação (Idea Generation Agent) propõe ou valida um tema para o post, considerando temas recentemente utilizados e tendências atuais.

3. **Criação de Conteúdo**  
   - O agente de copywriting (WritingCopywritingAgent) gera o conteúdo textual (headline, corpo e call-to-action) com base no briefing e no tema escolhido.

4. **Revisão e Conformidade**  
   - O `ReviewComplianceAgent` revisa o conteúdo para garantir que a gramática, o estilo e as diretrizes da marca estejam corretos, retornando o texto revisado em um formato único.

5. **Geração de Criativo Visual**  
   - Utilizando a API do DALL-E por meio do `VisualCreativeGenerationAgent`, o sistema gera uma imagem que complementa o tema do post.

6. **Otimização de Engajamento**  
   - O `EngagementOptimizationAgent` integra hashtags e possíveis menções ao conteúdo revisado para maximizar o alcance e o engajamento, mantendo a coerência com a identidade da marca.

7. **Publicação de Conteúdo**  
   - Por fim, o `PostingAgent` simula a publicação do conteúdo (por exemplo, no LinkedIn), retornando um status e um identificador do post para acompanhamento.

## Pré-requisitos
- **Python 3.7** ou superior.
- Dependências instaladas via *pip* (geralmente listadas em um arquivo `requirements.txt`):
  - `crewai`
  - `langchain`
  - `crewai_tools`
  - `python-dotenv`
  - Outras bibliotecas utilizadas para logging e manipulação de arquivos.

## Configuração
1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/marketing-ai-workflow.git
