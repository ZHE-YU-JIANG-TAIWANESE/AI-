# Security Policy

Open Character Workbench operates around local files, Blender, scripts, and optional external agents. Treat untrusted repositories, `.blend` files, Python scripts, add-ons, shell commands, and agent-generated code as executable content.

## Please do not publish

- API keys, tokens, passwords, cookies, or private connector credentials;
- private client references or proprietary character assets;
- secrets copied from CI logs or local environment files.

## Reporting

For security-sensitive problems, avoid posting working secrets or private user data in a public issue. Provide the smallest reproducible description possible and rotate any credential that may have been exposed.

## Agent boundary

An agent adapter should declare what tools, network access, files, and credentials it receives. A successful agent run does not imply that generated scripts or assets are safe; review them before reuse.
