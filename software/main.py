from enum import Enum

prompt_template = """
### Instruction ###
Develop a software based on the description available in the `./docs` directory.

Also, consider the context in the `Context` section below.

### Context ###
You are a senior software developer and architect and you are developing an {application_type} application.

This software must:
- Build software that will run on {os_platform} operating system.
- Be deployed in the {deploy_environment} environment.
- Use {architecture} architecture.
- Have code executed in the {infrastructure}.
- Use {paradigm} paradigm and {ecosystem} ecosystem.
- Use {code_design} code design.
- Use {framework} framework with {programming_language} programming language.
- Use {test_framework} test framework to make the {tests} tests.

### Output Indicator ###
Put everything you develop in a new directory with the name {project_name}.

Don't put comments in the code.

Write the code in English.

Use the Uncle Bob's Clean Code book techniques to write the code.
""".lstrip().rstrip()

def main():
    project_name = project_name_choice()
    application_type = application_type_choice()
    os_platform = os_platform_choice()
    deploy_environment = deploy_environment_choice()
    architecture = architecture_choice()
    infrastructure = infrastructure_choice()
    paradigm = paradigm_choice()
    ecosystem = ecosystem_choice()
    code_design = code_design_choice()
    framework = framework_choice()    
    programming_language = programming_language_choice()
    test_framework = test_framework_choice()
    tests = tests_choice()
    
    final_prompt = prompt_template.format(
        application_type=application_type,
        os_platform=os_platform,
        deploy_environment=deploy_environment,
        architecture=architecture,
        infrastructure=infrastructure,
        paradigm=paradigm,
        ecosystem=ecosystem,
        code_design=code_design,
        framework=framework,
        programming_language=programming_language,
        test_framework=test_framework,
        tests=tests,
        project_name=project_name
    )
    with open("./docs/prompt.txt", "w", encoding="utf-8") as file:
        file.write(final_prompt)

def project_name_choice() -> str:
    return input("What is the name of the project?\n")

def application_type_choice() -> str:
    class ApplicationType(Enum):
        WEB_CLIENT = "web client"
        WEB_SERVER = "web server"
        DESKTOP_CLIENT = "desktop client"
        DESKTOP_SERVER = "desktop server"
        MOBILE = "mobile"

    return input_with_option([application_type.value for application_type in ApplicationType])

def input_with_option(valid_options: list):
    value = input(f"Choose an option: {valid_options}\n")
    while value not in valid_options:
        print("Invalid option")
        value = input(f"Choose an option: {valid_options}\n")

    return value

def os_platform_choice() -> str:
    return input("Which OS will the software run on? Example: Android, iOS, macOS, Windows, Linux, BSD...\n")

def deploy_environment_choice() -> str:
    return input("Where will it be deployed? Example: AWS, Heroku, VPS, on-premises...\n")

def architecture_choice() -> str:
    class Architecture(Enum):
        MONOLITHIC = "monolithic"
        MICROSERVICE = "microservice"

    return input_with_option([architecture.value for architecture in Architecture])

def infrastructure_choice() -> str:
    return input("What type of infrastructure will the code run on? Example: Containers, Virtual Machine, Serverless, Bare metal...\n")

def paradigm_choice() -> str:
    class Paradigm(Enum):
        OBJECT_ORIENTED = "object oriented"
        IMPERATIVE = "imperative"
        FUNCTIONAL = "functional"

    return input_with_option([paradigm.value for paradigm in Paradigm])

def ecosystem_choice() -> str:
    return input("What is the ecosystem? Example: jvm, .net, node ...\n")

def code_design_choice() -> str:
    return input("What is/are the code design? Example: mvc, mvvm, layered, ports and adapters, onion architecture, clean architecture...\n")

def framework_choice() -> str:
    return input("What is the framework? Example: ExpressJS, Vue, Spring Boot, Laravel, Django...\n")

def programming_language_choice() -> str:
    return input("What is the programming language? Example: Kotlin, Java, Javascript, Typescript, C#, F#...\n")

def test_framework_choice() -> str:
    return input("What is/are the test framework? Example: Jest, JUnit, XUnit, PHPUnit...\n")

def tests_choice() -> str:
    return input("Which tests must be done? Example: unit, integration, components, end to end...\n")

main()
