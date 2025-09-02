# Quickstart - FastMCP

**URL:** https://gofastmcp.com/getting-started/quickstart
**Date:** 9/1/2025, 11:14:00 PM

---



Remote MCP that just works:  [FastMCP Cloud is here!](https://fastmcp.link/IhmBxWn)[FastMCP home page![](https://mintcdn.com/fastmcp/hUosZw7ujHZFemrG/assets/brand/logo-wordmark.svg?maxW=1803&auto=format&n=hUosZw7ujHZFemrG&q=85&s=96ef87af45f084c3000db5216c15ce81)![](https://mintcdn.com/fastmcp/hUosZw7ujHZFemrG/assets/brand/logo-wordmark-dark.svg?maxW=1803&auto=format&n=hUosZw7ujHZFemrG&q=85&s=28a86fbefd5211ed56ceaaa520e8a5b2)](/)Search the docs...Ctrl KSearch...NavigationGet StartedQuickstart[Documentation](/getting-started/welcome)[SDK Reference](/python-sdk/fastmcp-exceptions)[Documentation](/getting-started/welcome)[What's New](/updates)[Community](/community/showcase)Get Started[Welcome!](/getting-started/welcome)[Installation](/getting-started/installation)[Quickstart](/getting-started/quickstart)Servers[Overview](/servers/server)Core ComponentsAdvanced FeaturesAuthenticationDeploymentClientsEssentialsCore OperationsAdvanced FeaturesAuthenticationIntegrationsAuthenticationAuthorizationAI AssistantsAI SDKsWeb FrameworksPatterns[Tool Transformation](/patterns/tool-transformation)[Decorating Methods](/patterns/decorating-methods)[CLI](/patterns/cli)[Contrib Modules](/patterns/contrib)Tutorials[What is MCP?](/tutorials/mcp)[Creating an MCP Server](/tutorials/create-mcp-server)[Connect LLMs to REST APIs](/tutorials/rest-api)On this page[Creating a FastMCP Server](#creating-a-fastmcp-server)[Adding a Tool](#adding-a-tool)[Testing the Server](#testing-the-server)[Running the server](#running-the-server)[Interacting with the Python server](#interacting-with-the-python-server)[Using the FastMCP CLI](#using-the-fastmcp-cli)Get Started# Quickstart

Welcome! This guide will help you quickly set up FastMCP and run your first MCP server.
If you haven’t already installed FastMCP, follow the [installation instructions](/getting-started/installation).
## [​](#creating-a-fastmcp-server)Creating a FastMCP Server

A FastMCP server is a collection of tools, resources, and other MCP components. To create a server, start by instantiating the FastMCP class.
Create a new file called my_server.py and add the following code:
my_server.pyCopyfrom fastmcp import FastMCP

mcp = FastMCP("My MCP Server")

That’s it! You’ve created a FastMCP server, albeit a very boring one. Let’s add a tool to make it more interesting.
## [​](#adding-a-tool)Adding a Tool

To add a tool that returns a simple greeting, write a function and decorate it with @mcp.tool to register it with the server:
my_server.pyCopyfrom fastmcp import FastMCP

mcp = FastMCP("My MCP Server")

@mcp.tool
def greet(name: str) -> str:
    return f"Hello, {name}!"

## [​](#testing-the-server)Testing the Server

To test the server, create a FastMCP client and point it at the server object.
my_server.pyCopyimport asyncio
from fastmcp import FastMCP, Client

mcp = FastMCP("My MCP Server")

@mcp.tool
def greet(name: str) -> str:
    return f"Hello, {name}!"

client = Client(mcp)

async def call_tool(name: str):
    async with client:
        result = await client.call_tool("greet", {"name": name})
        print(result)

asyncio.run(call_tool("Ford"))

There are a few things to note here:

- Clients are asynchronous, so we need to use asyncio.run to run the client.

- We must enter a client context (async with client:) before using the client. You can make multiple client calls within the same context.

## [​](#running-the-server)Running the server

In order to run the server with Python, we need to add a run statement to the __main__ block of the server file.
my_server.pyCopyfrom fastmcp import FastMCP

mcp = FastMCP("My MCP Server")

@mcp.tool
def greet(name: str) -> str:
    return f"Hello, {name}!"

if __name__ == "__main__":
    mcp.run()

This lets us run the server with python my_server.py, using the default stdio transport, which is the standard way to expose an MCP server to a client.
Why do we need the if __name__ == "__main__": block?Within the FastMCP ecosystem, this line may be unnecessary. However, including it ensures that your FastMCP server runs for all users and clients in a consistent way and is therefore recommended as best practice.
### [​](#interacting-with-the-python-server)Interacting with the Python server

Now that the server can be executed with python my_server.py, we can interact with it like any other MCP server.
In a new file, create a client and point it at the server file:
my_client.pyCopyimport asyncio
from fastmcp import Client

client = Client("my_server.py")

async def call_tool(name: str):
    async with client:
        result = await client.call_tool("greet", {"name": name})
        print(result)

asyncio.run(call_tool("Ford"))

### [​](#using-the-fastmcp-cli)Using the FastMCP CLI

To have FastMCP run the server for us, we can use the fastmcp run command. This will start the server and keep it running until it is stopped. By default, it will use the stdio transport, which is a simple text-based protocol for interacting with the server.
Copyfastmcp run my_server.py:mcp

Note that FastMCP *does not* require the __main__ block in the server file, and will ignore it if it is present. Instead, it looks for the server object provided in the CLI command (here, mcp). If no server object is provided, fastmcp run will automatically search for servers called “mcp”, “app”, or “server” in the file.
We pointed our client at the server file, which is recognized as a Python MCP server and executed with python my_server.py by default. This executes the __main__ block of the server file. There are other ways to run the server, which are described in the [server configuration](/servers/server#running-the-server) guide.[Installation](/getting-started/installation)[Overview](/servers/server)AssistantResponses are generated using AI and may contain mistakes.