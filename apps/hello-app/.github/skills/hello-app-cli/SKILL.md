---
name: hello-app-cli
description: "Use the hello-app package CLI to greet a name through its greet command."
---

# Hello App CLI

Use this skill when asked to run or demonstrate the `hello-app` package CLI.

## Run the command

Run commands from the monorepo root. Use `uv tool run` with this package as the command provider:

```console
uv tool run --from ./apps/hello-app hello-app greet --name NAME
```

If the user did not provide a name, omit `--name` to use the CLI's default (`uv workspace`). The command prints the greeting to stdout. Return that output to the user; do not invent a successful result if the command fails.

Use `uv tool run --from ./apps/hello-app hello-app --help` to inspect available commands, or `uv tool run --from ./apps/hello-app hello-app greet --help` for the greeting options. Do not use shell commands other than the documented `hello-app` CLI invocation for this skill.
