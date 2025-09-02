# FastMCP Cloud - FastMCP

**URL:** https://gofastmcp.com/deployment/fastmcp-cloud
**Date:** 9/1/2025, 11:18:59 PM

---

**Description:** The fastest way to deploy your MCP server



Remote MCP that just works:  [FastMCP Cloud is here!](https://fastmcp.link/IhmBxWn)[FastMCP home page![](https://mintcdn.com/fastmcp/hUosZw7ujHZFemrG/assets/brand/logo-wordmark.svg?maxW=1803&auto=format&n=hUosZw7ujHZFemrG&q=85&s=96ef87af45f084c3000db5216c15ce81)![](https://mintcdn.com/fastmcp/hUosZw7ujHZFemrG/assets/brand/logo-wordmark-dark.svg?maxW=1803&auto=format&n=hUosZw7ujHZFemrG&q=85&s=28a86fbefd5211ed56ceaaa520e8a5b2)](/)Search the docs...Ctrl KSearch...NavigationDeploymentFastMCP Cloud[Documentation](/getting-started/welcome)[SDK Reference](/python-sdk/fastmcp-exceptions)[Documentation](/getting-started/welcome)[What's New](/updates)[Community](/community/showcase)Get Started[Welcome!](/getting-started/welcome)[Installation](/getting-started/installation)[Quickstart](/getting-started/quickstart)Servers[Overview](/servers/server)Core ComponentsAdvanced FeaturesAuthenticationDeployment[Running](/deployment/running-server)[Project Configuration](/deployment/server-configuration)[Testing](/deployment/testing)[Self-Hosted](/deployment/self-hosted)[FastMCP CloudNEW](/deployment/fastmcp-cloud)ClientsEssentialsCore OperationsAdvanced FeaturesAuthenticationIntegrationsAuthenticationAuthorizationAI AssistantsAI SDKsWeb FrameworksPatterns[Tool Transformation](/patterns/tool-transformation)[Decorating Methods](/patterns/decorating-methods)[CLI](/patterns/cli)[Contrib Modules](/patterns/contrib)Tutorials[What is MCP?](/tutorials/mcp)[Creating an MCP Server](/tutorials/create-mcp-server)[Connect LLMs to REST APIs](/tutorials/rest-api)On this page[Prerequisites](#prerequisites)[Getting Started](#getting-started)[Step 1: Create a Project](#step-1%3A-create-a-project)[Step 2: Deploy Your Server](#step-2%3A-deploy-your-server)[Step 3: Connect to Your Server](#step-3%3A-connect-to-your-server)Deployment# FastMCP Cloud

The fastest way to deploy your MCP server[FastMCP Cloud](https://fastmcp.cloud) is a managed platform for hosting MCP servers, built by the FastMCP team. While the FastMCP framework will always be fully open-source, we created FastMCP Cloud to solve the deployment challenges we’ve seen developers face. Our goal is to provide the absolute fastest way to make your MCP server available to LLM clients like Claude and Cursor.
FastMCP Cloud is a young product and we welcome your feedback. Please join our [Discord](https://discord.com/invite/aGsSC3yDF4) to share your thoughts and ideas, and you can expect to see new features and improvements every week.
FastMCP Cloud supports both **FastMCP 2.0** servers and also **FastMCP 1.0** servers that were created with the official MCP Python SDK.
FastMCP Cloud is completely free while in beta!
## [​](#prerequisites)Prerequisites

To use FastMCP Cloud, you’ll need a [GitHub](https://github.com) account. In addition, you’ll need a GitHub repo that contains a FastMCP server instance. If you don’t want to create one yet, you can proceed to [step 1](#step-1-create-a-project) and use the FastMCP Cloud quickstart repo.
Your repo can be public or private, but must include at least a Python file that contains a FastMCP server instance.
To ensure your file is compatible with FastMCP Cloud, you can run fastmcp inspect <file.py:server_object> to see what FastMCP Cloud will see when it runs your server.
If you have a requirements.txt or pyproject.toml in the repo, FastMCP Cloud will automatically detect your server’s dependencies and install them for you. Note that your file *can* have an if __name__ == "__main__" block, but it will be ignored by FastMCP Cloud.
For example, a minimal server file might look like:
Copyfrom fastmcp import FastMCP

mcp = FastMCP("MyServer")

@mcp.tool
def hello(name: str) -> str:
    return f"Hello, {name}!"

## [​](#getting-started)Getting Started

There are just three steps to deploying a server to FastMCP Cloud:
### [​](#step-1%3A-create-a-project)Step 1: Create a Project

Visit [fastmcp.cloud](https://fastmcp.cloud) and sign in with your GitHub account. Then, create a project. Each project corresponds to a GitHub repo, and you can create one from either your own repo or using the FastMCP Cloud quickstart repo.
![](https://mintcdn.com/fastmcp/hUosZw7ujHZFemrG/assets/images/fastmcp_cloud/quickstart.png?maxW=2656&auto=format&n=hUosZw7ujHZFemrG&q=85&s=558b0fdedc40e1ef6befb4c2fbcc28d9)
Next, you’ll be prompted to configure your project.
![](https://mintcdn.com/fastmcp/hUosZw7ujHZFemrG/assets/images/fastmcp_cloud/create_project.png?maxW=2656&auto=format&n=hUosZw7ujHZFemrG&q=85&s=90c3ae46bc2e5379af5000df656c6847)
The configuration screen lets you specify:

- **Name**: The name of your project. This will be used to generate a unique URL for your server.

- **Entrypoint**: The Python file containing your FastMCP server (e.g., echo.py). This field has the same syntax as the fastmcp run command, for example echo.py:my_server to specify a specific object in the file.

- **Authentication**: If disabled, your server is open to the public. If enabled, only other members of your FastMCP Cloud organization will be able to connect.

Note that FastMCP Cloud will automatically detect yours server’s Python dependencies from either a requirements.txt or pyproject.toml file.
### [​](#step-2%3A-deploy-your-server)Step 2: Deploy Your Server

Once you configure your project, FastMCP Cloud will:

- Clone the repository

- Build your FastMCP server

- Deploy it to a unique URL

- Make it immediately available for connections

![](https://mintcdn.com/fastmcp/hUosZw7ujHZFemrG/assets/images/fastmcp_cloud/deployment.png?maxW=2656&auto=format&n=hUosZw7ujHZFemrG&q=85&s=866328c5d29b6a5b1c14d13886c9fc2b)
FastMCP Cloud will monitor your repo and redeploy your server whenever you push a change to the main branch. In addition, FastMCP Cloud will build and deploy servers for every PR your open, hosting them on unique URLs, so you can test changes before updating your production server.
### [​](#step-3%3A-connect-to-your-server)Step 3: Connect to Your Server

Once your server is deployed, it will be accessible at a URL like:
Copyhttps://your-project-name.fastmcp.app/mcp

You should be able to connect to it as soon as you see the deployment succeed! FastMCP Cloud provides instant connection options for popular LLM clients:
![](https://mintcdn.com/fastmcp/hUosZw7ujHZFemrG/assets/images/fastmcp_cloud/connect.png?maxW=2568&auto=format&n=hUosZw7ujHZFemrG&q=85&s=ec757e16ba436fa944716d19661d787a)[Self-Hosted](/deployment/self-hosted)[Overview](/clients/client)AssistantResponses are generated using AI and may contain mistakes.![](https://mintcdn.com/fastmcp/hUosZw7ujHZFemrG/assets/images/fastmcp_cloud/create_project.png?w=840&maxW=2656&auto=format&n=hUosZw7ujHZFemrG&q=85&s=55a5861adecac472a0da93b4778c48a7)![](https://mintcdn.com/fastmcp/hUosZw7ujHZFemrG/assets/images/fastmcp_cloud/quickstart.png?w=840&maxW=2656&auto=format&n=hUosZw7ujHZFemrG&q=85&s=4c9250f955697d67616d115532a26fe7)![](https://mintcdn.com/fastmcp/hUosZw7ujHZFemrG/assets/images/fastmcp_cloud/connect.png?w=840&maxW=2568&auto=format&n=hUosZw7ujHZFemrG&q=85&s=0415826f639c38f28f9f3fd51875640e)![](https://mintcdn.com/fastmcp/hUosZw7ujHZFemrG/assets/images/fastmcp_cloud/deployment.png?w=840&maxW=2656&auto=format&n=hUosZw7ujHZFemrG&q=85&s=6351df613fe6abc1d8aa4ac05df80b35)