# 📦 Ecossistema de Pacotes NEO-FlowOFF

Este documento centraliza o catálogo de pacotes modulares (libraries) do ecossistema **NEO-FlowOFF**.
Todos os pacotes aqui listados são publicados no GitHub Packages de forma privada, mantendo a coerência transversal entre os múltiplos repositórios soberanos (miniapps, interfaces, serviços e agentes).

────────────────────────────────────────

## 1. `@neo-flowoff/shared`

**O Primeiro Pacote do Ecossistema!** 🏆
Criado como a espinha dorsal de infraestrutura comum, este pacote unifica o código que deve ser idêntico em todas as aplicações NEO-FlowOFF.

### ⧉ Detalhes

- **Localização Original:** `/neo-shared/` (Monorepo Workspace)
- **Registro de Publicação:** `npm.pkg.github.com` (GitHub Packages Privado)
- **Instalação:** `pnpm add @neo-flowoff/shared`

### ⍟ Funcionalidades Atuais

- **Logger Centralizado:** Um sistema unificado de log (Pino/Console) para formatar e padronizar o output em tempo de execução (runtime), simplificando a depuração no Railway e mantendo o padrão em toda a frota de aplicações.
- *(Expansível para utilitários de banco de dados, tipagens compartilhadas, funções utilitárias e regras de negócio universais).*

### 🔐 Requisitos de Consumo

Como o pacote é privado, todas as aplicações que o consomem precisam das credenciais de acesso no build-time (Railway, Actions e local):

1. **`GITHUB_TOKEN`**: Token clássico com permissão `read:packages`.
2. **`.npmrc`**: Configuração explícita atrelando o escopo ao registro do GitHub:

   ```ini
   @neo-flowoff:registry=https://npm.pkg.github.com
   //npm.pkg.github.com/:_authToken=${GITHUB_TOKEN}
   ```

────────────────────────────────────────

*(Mantenha este arquivo atualizado conforme novos pacotes de utilitários, UI kits ou serviços base forem abstraídos e publicados no registry da organização).*
