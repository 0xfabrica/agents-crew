from crew import IaTutorCrew
from rich.console import Console
from rich.markdown import Markdown
import os

def run_interactive_chat():
    """
    Inicia un bucle de chat interactivo en la terminal.
    """
    console = Console()
    console.print("\n[bold cyan]Bienvenido al Tutor de IA de CrewAI.[/bold cyan]")
    console.print("[yellow]Escribe tu pregunta o 'salir' para terminar.[/yellow]\n")

    # Instanciamos la crew una sola vez fuera del bucle para mayor eficiencia
    tutor_crew = IaTutorCrew().crew()

    while True:
        try:
            # 1. Pedimos la pregunta al usuario
            user_question = console.input("[bold green]Tú:[/bold green] ")

            if user_question.lower() in ['salir', 'exit', 'quit']:
                console.print("[bold red]¡Hasta luego![/bold red]")
                break

            # 2. Preparamos los inputs para la crew
            inputs = {'user_question': user_question}

            # 3. Ejecutamos la crew con la pregunta
            console.print("\n[bold blue]Tutor IA está pensando...[/bold blue]")
            result = tutor_crew.kickoff(inputs=inputs)
            
            # Limpiamos la consola si se generó un archivo de salida
            output_file_path = 'respuesta.md'
            if os.path.exists(output_file_path):
                 os.remove(output_file_path)

            # 4. Mostramos el resultado en la terminal
            console.print("\n[bold blue]Tutor IA:[/bold blue]")
            console.print(Markdown(result))
            console.print("\n" + "="*80 + "\n")


        except KeyboardInterrupt:
            # Permite salir con Ctrl+C
            console.print("\n[bold red]Interrupción detectada. Saliendo...[/bold red]")
            break
        except Exception as e:
            console.print(f"\n[bold red]Ocurrió un error:[/bold red] {e}")
            break

# Para ejecutar este script directamente
if __name__ == "__main__":
    run_interactive_chat()