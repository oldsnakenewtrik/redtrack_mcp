# Running Your Server - FastMCP

**URL:** https://gofastmcp.com/deployment/running-server
**Date:** 9/1/2025, 11:14:11 PM

---

**Description:** Learn how to run your FastMCP server locally for development and testing



Remote MCP that just works:  [FastMCP Cloud is here!](https://fastmcp.link/IhmBxWn)[FastMCP home page![](https://mintcdn.com/fastmcp/hUosZw7ujHZFemrG/assets/brand/logo-wordmark.svg?maxW=1803&auto=format&n=hUosZw7ujHZFemrG&q=85&s=96ef87af45f084c3000db5216c15ce81)![](https://mintcdn.com/fastmcp/hUosZw7ujHZFemrG/assets/brand/logo-wordmark-dark.svg?maxW=1803&auto=format&n=hUosZw7ujHZFemrG&q=85&s=28a86fbefd5211ed56ceaaa520e8a5b2)](/)Search the docs...Ctrl KSearch...NavigationDeploymentRunning Your Server[Documentation](/getting-started/welcome)[SDK Reference](/python-sdk/fastmcp-exceptions)[Documentation](/getting-started/welcome)[What's New](/updates)[Community](/community/showcase)Get Started[Welcome!](/getting-started/welcome)[Installation](/getting-started/installation)[Quickstart](/getting-started/quickstart)Servers[Overview](/servers/server)Core ComponentsAdvanced FeaturesAuthenticationDeployment[Running](/deployment/running-server)[Project Configuration](/deployment/server-configuration)[Testing](/deployment/testing)[Self-Hosted](/deployment/self-hosted)[FastMCP CloudNEW](/deployment/fastmcp-cloud)ClientsEssentialsCore OperationsAdvanced FeaturesAuthenticationIntegrationsAuthenticationAuthorizationAI AssistantsAI SDKsWeb FrameworksPatterns[Tool Transformation](/patterns/tool-transformation)[Decorating Methods](/patterns/decorating-methods)[CLI](/patterns/cli)[Contrib Modules](/patterns/contrib)Tutorials[What is MCP?](/tutorials/mcp)[Creating an MCP Server](/tutorials/create-mcp-server)[Connect LLMs to REST APIs](/tutorials/rest-api)On this page[The run() Method](#the-run-method)[Transport Protocols](#transport-protocols)[STDIO Transport (Default)](#stdio-transport-default)[HTTP Transport (Streamable)](#http-transport-streamable)[SSE Transport (Legacy)](#sse-transport-legacy)[Choosing the Right Transport](#choosing-the-right-transport)[The FastMCP CLI](#the-fastmcp-cli)[Dependency Management](#dependency-management)[Passing Arguments to Servers](#passing-arguments-to-servers)[Async Usage](#async-usage)[Custom Routes](#custom-routes)[Alternative Initialization Patterns](#alternative-initialization-patterns)[CLI-Only Servers](#cli-only-servers)[ASGI Applications](#asgi-applications)Deployment# Running Your Server

Learn how to run your FastMCP server locally for development and testingFastMCP servers can be run in different ways depending on your needs. This guide focuses on running servers locally for development and testing. For production deployment to a URL, see the [Self-Hosted Deployment](/deployment/self-hosted) guide.
## [​](#the-run-method)The run() Method

Every FastMCP server needs to be started to accept connections. The simplest way to run a server is by calling the run() method on your FastMCP instance. This method starts the server and blocks until it’s stopped, handling all the connection management for you.
For maximum compatibility, it’s best practice to place the run() call within an if __name__ == "__main__": block. This ensures the server starts only when the script is executed directly, not when imported as a module.
my_server.pyCopyfrom fastmcp import FastMCP

mcp = FastMCP(name="MyServer")

@mcp.tool
def hello(name: str) -> str:
    return f"Hello, {name}!"

if __name__ == "__main__":
    mcp.run()

You can now run this MCP server by executing python my_server.py.
## [​](#transport-protocols)Transport Protocols

MCP servers communicate with clients through different transport protocols. Think of transports as the “language” your server speaks to communicate with clients. FastMCP supports three main transport protocols, each designed for specific use cases and deployment scenarios.
The choice of transport determines how clients connect to your server, what network capabilities are available, and how many clients can connect simultaneously. Understanding these transports helps you choose the right approach for your application.
### [​](#stdio-transport-default)STDIO Transport (Default)

STDIO (Standard Input/Output) is the default transport for FastMCP servers. When you call run() without arguments, your server uses STDIO transport. This transport communicates through standard input and output streams, making it perfect for command-line tools and desktop applications like Claude Desktop.
With STDIO transport, the client spawns a new server process for each session and manages its lifecycle. The server reads MCP messages from stdin and writes responses to stdout. This is why STDIO servers don’t stay running - they’re started on-demand by the client.
Copyfrom fastmcp import FastMCP

mcp = FastMCP("MyServer")

@mcp.tool
def hello(name: str) -> str:
    return f"Hello, {name}!"

if __name__ == "__main__":
    mcp.run()  # Uses STDIO transport by default

STDIO is ideal for:

- Local development and testing

- Claude Desktop integration

- Command-line tools

- Single-user applications

### [​](#http-transport-streamable)HTTP Transport (Streamable)

HTTP transport turns your MCP server into a web service accessible via a URL. This transport uses the Streamable HTTP protocol, which allows clients to connect over the network. Unlike STDIO where each client gets its own process, an HTTP server can handle multiple clients simultaneously.
The Streamable HTTP protocol provides full bidirectional communication between client and server, supporting all MCP operations including streaming responses. This makes it the recommended choice for network-based deployments.
To use HTTP transport, specify it in the run() method along with networking options:
Copyfrom fastmcp import FastMCP

mcp = FastMCP("MyServer")

@mcp.tool
def hello(name: str) -> str:
    return f"Hello, {name}!"

if __name__ == "__main__":
    # Start an HTTP server on port 8000
    mcp.run(transport="http", host="127.0.0.1", port=8000)

Your server is now accessible at http://localhost:8000/mcp/. This URL is the MCP endpoint that clients will connect to. HTTP transport enables:

- Network accessibility

- Multiple concurrent clients

- Integration with web infrastructure

- Remote deployment capabilities

For production HTTP deployment with authentication and advanced configuration, see the [Self-Hosted Deployment](/deployment/self-hosted) guide.
### [​](#sse-transport-legacy)SSE Transport (Legacy)

Server-Sent Events (SSE) transport was the original HTTP-based transport for MCP. While still supported for backward compatibility, it has limitations compared to the newer Streamable HTTP transport. SSE only supports server-to-client streaming, making it less efficient for bidirectional communication.
Copyif __name__ == "__main__":
    # SSE transport - use HTTP instead for new projects
    mcp.run(transport="sse", host="127.0.0.1", port=8000)

We recommend using HTTP transport instead of SSE for all new projects. SSE remains available only for compatibility with older clients that haven’t upgraded to Streamable HTTP.
### [​](#choosing-the-right-transport)Choosing the Right Transport

Each transport serves different needs. STDIO is perfect when you need simple, local execution - it’s what Claude Desktop and most command-line tools expect. HTTP transport is essential when you need network access, want to serve multiple clients, or plan to deploy your server remotely. SSE exists only for backward compatibility and shouldn’t be used in new projects.
Consider your deployment scenario: Are you building a tool for local use? STDIO is your best choice. Need a centralized service that multiple clients can access? HTTP transport is the way to go.
## [​](#the-fastmcp-cli)The FastMCP CLI

FastMCP provides a powerful command-line interface for running servers without modifying the source code. The CLI can automatically find and run your server with different transports, manage dependencies, and handle development workflows:
Copyfastmcp run server.py

The CLI automatically finds a FastMCP instance in your file (named mcp, server, or app) and runs it with the specified options. This is particularly useful for testing different transports or configurations without changing your code.
### [​](#dependency-management)Dependency Management

The CLI integrates with uv to manage Python environments and dependencies:
Copy# Run with a specific Python version
fastmcp run server.py --python 3.11

# Run with additional packages
fastmcp run server.py --with pandas --with numpy

# Run with dependencies from a requirements file
fastmcp run server.py --with-requirements requirements.txt

# Combine multiple options
fastmcp run server.py --python 3.10 --with httpx --transport http

# Run within a specific project directory
fastmcp run server.py --project /path/to/project

When using --python, --with, --project, or --with-requirements, the server runs via uv run subprocess instead of using your local environment.
### [​](#passing-arguments-to-servers)Passing Arguments to Servers

When servers accept command line arguments (using argparse, click, or other libraries), you can pass them after --:
Copyfastmcp run config_server.py -- --config config.json
fastmcp run database_server.py -- --database-path /tmp/db.sqlite --debug

This is useful for servers that need configuration files, database paths, API keys, or other runtime options.
For more CLI features including development mode with the MCP Inspector, see the [CLI documentation](/patterns/cli).
### [​](#async-usage)Async Usage

FastMCP servers are built on async Python, but the framework provides both synchronous and asynchronous APIs to fit your application’s needs. The run() method we’ve been using is actually a synchronous wrapper around the async server implementation.
For applications that are already running in an async context, FastMCP provides the run_async() method:
Copyfrom fastmcp import FastMCP
import asyncio

mcp = FastMCP(name="MyServer")

@mcp.tool
def hello(name: str) -> str:
    return f"Hello, {name}!"

async def main():
    # Use run_async() in async contexts
    await mcp.run_async(transport="http", port=8000)

if __name__ == "__main__":
    asyncio.run(main())

The run() method cannot be called from inside an async function because it creates its own async event loop internally. If you attempt to call run() from inside an async function, you’ll get an error about the event loop already running.Always use run_async() inside async functions and run() in synchronous contexts.
Both run() and run_async() accept the same transport arguments, so all the examples above apply to both methods.
## [​](#custom-routes)Custom Routes

When using HTTP transport, you might want to add custom web endpoints alongside your MCP server. This is useful for health checks, status pages, or simple APIs. FastMCP lets you add custom routes using the @custom_route decorator:
Copyfrom fastmcp import FastMCP
from starlette.requests import Request
from starlette.responses import PlainTextResponse

mcp = FastMCP("MyServer")

@mcp.custom_route("/health", methods=["GET"])
async def health_check(request: Request) -> PlainTextResponse:
    return PlainTextResponse("OK")

@mcp.tool
def process(data: str) -> str:
    return f"Processed: {data}"

if __name__ == "__main__":
    mcp.run(transport="http")  # Health check at http://localhost:8000/health

Custom routes are served by the same web server as your MCP endpoint. They’re available at the root of your domain while the MCP endpoint is at /mcp/. For more complex web applications, consider [mounting your MCP server into a FastAPI or Starlette app](/deployment/self-hosted#integration-with-web-frameworks).
## [​](#alternative-initialization-patterns)Alternative Initialization Patterns

The if __name__ == "__main__" pattern works well for standalone scripts, but some deployment scenarios require different approaches. FastMCP handles these cases automatically.
### [​](#cli-only-servers)CLI-Only Servers

When using the FastMCP CLI, you don’t need the if __name__ block at all. The CLI will find your FastMCP instance and run it:
Copy# server.py
from fastmcp import FastMCP

mcp = FastMCP("MyServer")  # CLI looks for 'mcp', 'server', or 'app'

@mcp.tool
def process(data: str) -> str:
    return f"Processed: {data}"

# No if __name__ block needed - CLI will find and run 'mcp'

### [​](#asgi-applications)ASGI Applications

For ASGI deployment (running with Uvicorn or similar), you’ll want to create an ASGI application object. This approach is common in production deployments where you need more control over the server configuration:
Copy# app.py
from fastmcp import FastMCP

def create_app():
    mcp = FastMCP("MyServer")
    
    @mcp.tool
    def process(data: str) -> str:
        return f"Processed: {data}"
    
    return mcp.http_app()

app = create_app()  # Uvicorn will use this

See the [Self-Hosted Deployment](/deployment/self-hosted) guide for more ASGI deployment patterns.[Full OAuth Server](/servers/auth/full-oauth-server)[Project Configuration](/deployment/server-configuration)AssistantResponses are generated using AI and may contain mistakes.