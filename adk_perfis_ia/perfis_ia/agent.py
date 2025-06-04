from . import prompts
from . import tools
from google.adk.agents import Agent, SequentialAgent
from google.adk.tools import google_search
from google.adk.tools.agent_tool import AgentTool

modelo = "gemini-2.0-flash"

automatizador = Agent(
    name="automatizador",
    model=modelo,
    description= "Automatiza até o parabéns do grupo da família",
    instruction=prompts.perfil_automatizador,
    tools=[google_search]
)

ai_first = Agent(
    name="ai_first",
    model=modelo,
    description= "Tem uma tarefa? Essa pessoa vai fazer com IA generativa",
    instruction=prompts.perfil_ai_first,
    tools=[]
)

multitool = Agent(
    name="multitool",
    model=modelo,
    description= "Aquela pessoa que testa várias ferramentas de IA generativa ao mesmo tempo",
    instruction=prompts.perfil_multitool,
    tools=[google_search]
)

gestora = Agent(
    name="gestora",
    model=modelo,
    description= "Faz planilha de ROI antes de testar uma IA generativa nova",
    instruction=prompts.perfil_gestora,
    tools=[google_search]
)

cetico = Agent(
    name="cetico",
    model=modelo,
    description= "Não se convenceu ainda do potencial das IAs generativas",
    instruction=prompts.perfil_cetico,
    tools=[]
)

sensei = Agent(
    name="sensei",
    model=modelo,
    description= "Ela sempre diz palavras sábias como 'Sua resposta depende da sua pergunta'",
    instruction=prompts.perfil_sensei,
    tools=[]
)

criadora = Agent(
    name="criadora",
    model=modelo,
    description= "Vive de brainstormings com a IA",
    instruction=prompts.perfil_criadora,
    tools=[google_search]
)

produtividade = Agent(
    name="produtividade",
    model=modelo,
    description="Agente encarregado da tool 'produtividade'",
    instruction="Executa a tool 'produtividade'",
    tools=[tools.produtividade]

)

executor = Agent(
    name="executor",
    model=modelo,
    description= "Menos tempo e mais entrega",
    instruction=prompts.perfil_executor,
    tools=[AgentTool(agent=produtividade)]
)

evangelizador = Agent(
    name="evangelizador",
    model=modelo,
    description= "Espalha a palavra da IA generativa",
    instruction=prompts.perfil_evangelizador,
    tools=[]
)

artista = Agent(
    name="artista",
    model=modelo,
    description= "Dá para jurar que sua cabeça é o Pinterest da IA",
    instruction=prompts.perfil_artista,
    tools=[]
)

perfis_ia = SequentialAgent(
    name="perfis_ia",
    sub_agents=[automatizador, ai_first, multitool, gestora, cetico, sensei, criadora, executor, evangelizador, artista],
    description="Sequência de funcionamento do fluxo de agentes a partir de arquétipos de perfis de IA users"
)

root_agent = perfis_ia