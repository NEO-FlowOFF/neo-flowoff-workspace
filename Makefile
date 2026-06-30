# ========================================
# 🚀 NEO-FlowOFF Control Plane
# ========================================
# Modern workspace automation and governance
#
# Usage: make [target]
# Example: make help

.PHONY: help install clean build lint test update doctor

# Default target (show help)
.DEFAULT_GOAL := help

# Colors for output
CYAN := \033[36m
GREEN := \033[32m
YELLOW := \033[33m
RED := \033[31m
RESET := \033[0m

# ========================================
# 📚 HELP & BANNER
# ========================================

help: ## Exibe este menu de ajuda
	@echo "$(CYAN)"
	@echo "╔══════════════════════════════════════════════════════════╗"
	@echo "║                                                          ║"
	@echo "║               NEO-FlowOFF CONTROL PLANE                  ║"
	@echo "║               Workspace & Governança                    ║"
	@echo "║                                                          ║"
	@echo "╚══════════════════════════════════════════════════════════╝"
	@echo "$(RESET)"
	@echo "$(GREEN)Comandos disponíveis:$(RESET)\n"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "$(CYAN)%-20s$(RESET) %s\n", $$1, $$2}'
	@echo ""
	@echo "$(YELLOW)Exemplos:$(RESET)"
	@echo "  make install        # Instala dependências do workspace inteiro"
	@echo "  make clean          # Varre todos os node_modules e dists"
	@echo "  make doctor         # Checa a saúde da governança"
	@echo ""

# ========================================
# 📦 WORKSPACE PACKAGES
# ========================================

install: ## Instala dependências para todo o ecossistema (pnpm install)
	@echo "$(CYAN)📦 Instalando dependências globais...$(RESET)"
	pnpm install

clean: ## Remove pastas node_modules, dist e build de todos os projetos
	@echo "$(CYAN)🧹 Limpando node_modules e caches do workspace...$(RESET)"
	rm -rf node_modules
	pnpm -r exec rm -rf node_modules dist build .turbo .next .ape
	@echo "$(GREEN)✅ Limpeza concluída.$(RESET)"

build: ## Roda o script de build em todos os repositórios (se aplicável)
	@echo "$(CYAN)🏗️  Executando builds...$(RESET)"
	pnpm -r run build

lint: ## Roda o script de lint em todos os repositórios (se aplicável)
	@echo "$(CYAN)🔍 Executando lint global...$(RESET)"
	pnpm -r run lint

test: ## Roda testes em todos os repositórios (se aplicável)
	@echo "$(CYAN)🧪 Rodando testes globais...$(RESET)"
	pnpm -r run test

update: ## Atualiza as dependências interativamente em todo o workspace
	@echo "$(CYAN)🔄 Atualizando dependências...$(RESET)"
	pnpm update -i -r

# ========================================
# 🛡️  GOVERNANÇA
# ========================================

doctor: ## Executa o workspace-doctor para validar integridade do Control Plane
	@echo "$(CYAN)🩺 Diagnosticando workspace...$(RESET)"
	python3 scripts/workspace-doctor

