from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from langchain_openai import ChatOpenAI

# Importa tus herramientas personalizadas con la ruta correcta
from .tools.general_search_tool import GeneralWebSearchTool
from .tools.deep_research_tool import DeepResearchTool
from crewai_tools import FileReadTool


@CrewBase
class IaTutorCrew():
    """IaTutorCrew crew"""
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    manager_llm = ChatOpenAI(model="gpt-4o", temperature=0)

    # --- AGENTES SINCRONIZADOS ---

    @agent
    def OrchestratorAgent(self) -> Agent:
        return Agent(
            config=self.agents_config['OrchestratorAgent'], # Sincronizado!
            tools=[GeneralWebSearchTool()],
            verbose=True
        )

    @agent
    def WebReconAgent(self) -> Agent:
        return Agent(
            config=self.agents_config['WebReconAgent'], # Sincronizado!
            tools=[GeneralWebSearchTool()], 
            verbose=True
        )

    @agent
    def AcademicResearcherAgent(self) -> Agent:
        return Agent(
            config=self.agents_config['AcademicResearcherAgent'], # Sincronizado!
            tools=[DeepResearchTool()],
            verbose=True
        )

    @agent
    def CodeSynthesistAgent(self) -> Agent:
        return Agent(
            config=self.agents_config['CodeSynthesistAgent'], # Sincronizado!
            verbose=True
        )
        
    @agent
    def LeadTutorAgent(self) -> Agent:
        return Agent(
            config=self.agents_config['LeadTutorAgent'], # Sincronizado!
            tools=[FileReadTool(file_path='knowledge/user_preference.txt')],
            verbose=True
        )

    # --- TAREAS SINCRONIZADAS ---

    @task
    def triage_task(self) -> Task:
        return Task(
            config=self.tasks_config['triage_task'],
            agent=self.OrchestratorAgent()
        )

    @task
    def web_search_task(self) -> Task:
        return Task(
            config=self.tasks_config['web_search_task'],
            agent=self.WebReconAgent()
        )

    @task
    def deep_research_task(self) -> Task:
        return Task(
            config=self.tasks_config['deep_research_task'],
            agent=self.AcademicResearcherAgent(),
            context=[self.web_search_task()]
        )

    @task
    def practical_code_task(self) -> Task:
        return Task(
            config=self.tasks_config['practical_code_task'],
            agent=self.CodeSynthesistAgent(),
            context=[self.deep_research_task()]
        )

    @task
    def final_response_task(self) -> Task:
        return Task(
            config=self.tasks_config['final_response_task'],
            agent=self.LeadTutorAgent(),
            context=[self.deep_research_task(), self.practical_code_task()]
        )

    # --- CREW DEFINITION ---

    @crew
    def crew(self) -> Crew:
        """Creates the IaTutorCrew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.hierarchical,
            manager_llm = self.manager_llm,
            verbose=True
        )