---
name: greetings-cli
description: "Use the greetings package CLI to print a friendly greeting for a requested name."
---

# Greetings CLI

Use this skill when asked to greet someone or demonstrate the `greetings` package CLI.

## Run the command

Run commands from the monorepo root. Use `uv tool run` with this package as the command provider:

```console
uv tool run --from ./packages/greetings greetings --name NAME
```

If the user did not provide a name, omit `--name` to use the CLI's default (`world`). The command prints the greeting to stdout. Return that output to the user; do not invent a successful result if the command fails.

Use `uv tool run --from ./packages/greetings greetings --help` to inspect the available options. Do not use shell commands other than the documented `greetings` CLI invocation for this skill.
