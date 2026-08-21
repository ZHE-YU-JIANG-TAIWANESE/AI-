# Agent Adapters

OCW keeps the core job/evidence/delivery contract vendor-neutral. Put runtime-specific instructions here.

An adapter should document:

- how the agent is launched;
- how local reference images are made visible to the model;
- how Blender is exposed to the runtime;
- tool/network permissions;
- secret requirements without including secret values;
- expected output path (`vendor-output/`);
- how runtime failures are distinguished from modeling failures.

Good adapters should be thin. They should not redefine geometry evidence or silently inject prior character answers.

Suggested adapter folders:

```text
adapters/
  gemini-cli/
  codex/
  local-model/
  human-artist/
```

Community adapters are welcome as long as their permissions and evidence behavior are explicit.
