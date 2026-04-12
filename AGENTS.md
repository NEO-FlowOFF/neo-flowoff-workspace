# AGENTS.md

## Workspace Identity

- Official workspace root: `/Users/nettomello/neomello/NEO-FlowOFF`
- Recommended coordination repository name:
  `neo-flowoff-workspace`
- GitHub organization: `NEO-FlowOFF`

## Operating Model

This directory is an organizational multi-repo workspace.

Structural contract:

- the workspace root versions coordination
- child repositories version product
- the workspace root is not a product monorepo
- child repositories keep sovereign history and runtime ownership

## Workspace Root Responsibilities

- repository manifests
- integration manifests
- cross-repo documentation
- operational standards
- bootstrap scripts
- diagnostic scripts
- environment, domain, webhook and dependency maps
  when relevant

## Child Repository Responsibilities

- source code
- runtime behavior
- product dependencies
- tests
- service-specific documentation
- release history

## Hard Rules

- Never move child repository code into the workspace root.
- Never version child directories inside the coordination repository.
- Never create a parallel backlog that diverges from execution reality.
- Product changes must happen in the correct child repository.
- Cross-repo topology, patterns and operational automation
  belong to the workspace root.

## Documentation Contract

- `MARKDOWN_STYLE_GUIDE.md` at the workspace root is canonical.
- Structural docs in this workspace must follow that guide.
- Strategic documentation must translate real execution.
- Do not invent parallel truth in docs.

## Local Tooling Contract

- On this Mac, workspace root script execution must assume `python3`.
- Use `python3` in workspace docs, handoffs and automation references.
- Do not normalize local guidance back to `npm` for workspace root operations.

## Routing Contract

1. Classify the task as coordination or product.
2. If it is coordination, operate in the workspace root.
3. If it is product, operate in the correct child repository.
4. If it touches several repositories, register the shared pattern
   here and apply product changes in each sovereign repo.

## Local Source Of Truth

- [README.md](/Users/nettomello/neomello/NEO-FlowOFF/README.md)
- [manifests/repos.json](/Users/nettomello/neomello/NEO-FlowOFF/manifests/repos.json)
- [manifests/integrations.json](/Users/nettomello/neomello/NEO-FlowOFF/manifests/integrations.json)
- [manifests/tokens/base-neoflow.json](/Users/nettomello/neomello/NEO-FlowOFF/manifests/tokens/base-neoflow.json)
- [manifests/workspace.json](/Users/nettomello/neomello/NEO-FlowOFF/manifests/workspace.json)
- [docs/workspace/WORKSPACE_MODEL.md](/Users/nettomello/neomello/NEO-FlowOFF/docs/workspace/WORKSPACE_MODEL.md)
- [docs/workspace/WORKSPACE_TOPOLOGY.md](/Users/nettomello/neomello/NEO-FlowOFF/docs/workspace/WORKSPACE_TOPOLOGY.md)
- [docs/workspace/DRIFT_BACKLOG.md](/Users/nettomello/neomello/NEO-FlowOFF/docs/workspace/DRIFT_BACKLOG.md)
- [scripts/workspace-doctor](/Users/nettomello/neomello/NEO-FlowOFF/scripts/workspace-doctor)
- [scripts/generate-workspace-topology](/Users/nettomello/neomello/NEO-FlowOFF/scripts/generate-workspace-topology)
