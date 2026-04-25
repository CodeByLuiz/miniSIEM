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

## Estrutura do projeto

```
siem/
│
├── main.py
├── config.py
│
├── parser/
│   └── log_parser.py
│
├── detection/
│   └── detector.py
│
├── utils/
│   └── storage.py
│
├── logs/
│   └── sample.log
│
└── data/
    ├── events.json
    └── alerts.json
```

---

## Como funciona

O sistema segue o fluxo abaixo:

Logs → Parsing → Normalização → Detecção → Alertas → Armazenamento

---

## Detecção implementada

### Brute force (SSH)

O sistema identifica múltiplas tentativas de login falhadas a partir de um mesmo IP.

* 5 tentativas ou mais: risco MEDIUM
* 10 tentativas ou mais: risco HIGH

---

## Como executar

Clone o repositório:

```bash
git clone https://github.com/CodeByLuiz/miniSIEM.git
cd miniSIEM
```

Execute o projeto:

```bash
python main.py
```

---

## Saída

O sistema gera dois arquivos:

* `data/events.json`: eventos processados
* `data/alerts.json`: alertas detectados

Exemplo de alerta:

```
[MEDIUM] brute_force - 192.168.0.10 (8 tentativas)
```

---

## Objetivo

Demonstrar conhecimentos em:

* análise de logs
* detecção de eventos de segurança
* estruturação de projetos em Python
* conceitos básicos de SIEM

---

## Possíveis melhorias

* detecção baseada em janela de tempo
* integração com logs reais
* dashboard para visualização
* suporte a múltiplas fontes de log

---

## Autor

Luiz André Almeida dos Santos
