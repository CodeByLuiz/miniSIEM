# Mini SIEM em Python

Projeto que simula um sistema SIEM (Security Information and Event Management) capaz de processar logs, identificar padrões suspeitos e gerar alertas de segurança.

---

## Sobre o projeto

Este projeto implementa um fluxo básico de análise de eventos de segurança, inspirado no funcionamento de um SOC (Security Operations Center). O objetivo é demonstrar, de forma prática, como logs podem ser coletados, normalizados e analisados para detecção de ameaças.

---

## Funcionalidades

* Leitura e processamento de logs
* Parsing e normalização de eventos
* Classificação de eventos (login falho, sucesso, etc.)
* Detecção de tentativa de brute force
* Classificação de risco (LOW, MEDIUM, HIGH)
* Geração de alertas
* Exportação de dados em JSON

---

## Como funciona

O sistema segue o fluxo abaixo:

Logs → Parsing → Normalização → Detecção → Alertas → Armazenamento

---

## Configuração

O arquivo `config.py` centraliza os parâmetros utilizados na detecção de ameaças.

Exemplo:


FAILED_THRESHOLD = 5
HIGH_RISK_THRESHOLD = 10


Esses valores definem:

* Quantidade mínima de tentativas falhadas para considerar um possível ataque
* Critérios para classificação de risco

Essa abordagem permite ajustar facilmente o comportamento do sistema sem alterar a lógica principal do código.

---

## Detecção implementada

### Brute force (SSH)

O sistema identifica múltiplas tentativas de login falhadas a partir de um mesmo IP.

* 5 tentativas ou mais: risco MEDIUM
* 10 tentativas ou mais: risco HIGH

---

## Como executar

Clone o repositório:

```bash id="lrswz9"
git clone https://github.com/CodeByLuiz/miniSIEM.git
cd miniSIEM
```

Execute o projeto:

```bash id="wbslbm"
python main.py
```

---

## Observação sobre os logs

Ao executar o projeto, os logs são **gerados automaticamente por uma função interna (`generate_fake_logs`)**, que simula um cenário de ataque com múltiplas tentativas de login falhadas.

Essa abordagem foi utilizada para facilitar testes e demonstração do funcionamento do sistema sem depender de logs reais.

---

## Saída

O sistema gera dois arquivos:

* data/events.json: eventos processados
* data/alerts.json: alertas detectados

Exemplo de alerta:


[MEDIUM] brute_force - 192.168.0.10 (8 tentativas)


---

## Objetivo

Demonstrar conhecimentos em:

* análise de logs
* detecção de eventos de segurança
* estruturação de projetos em Python
* conceitos básicos de SIEM

---

## Possíveis melhorias

* ingestão de logs reais (ex: Linux auth.log)
* detecção baseada em janela de tempo
* dashboard para visualização
* suporte a múltiplas fontes de log

---

## Autor

Luiz André Almeida dos Santos

