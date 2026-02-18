# Poker Vision ♠♥♦♣ (Em Construção 🚧)

Uma ferramenta simples de análise de mesas de poker em tempo real utilizando visão computacional e inteligência artificial.

## 📋 Sobre o Projeto

O **Poker Vision** captura a tela do seu computador, identifica uma mesa de poker ativa e utiliza a API do Google Gemini (`gemini-3-pro-preview`) para analisar a mão do jogador e as cartas comunitárias. Baseado nessa análise, ele calcula e exibe as probabilidades de diferentes combinações de mãos.

**Status:** 🚧 Em desenvolvimento.

## 🚀 Como Usar

### Pré-requisitos

- Python 3.x instalado.
- Uma chave de API do Google Gemini (obtenha em [Google AI Studio](https://aistudio.google.com/)).

### Instalação

1. Clone este repositório.
2. Instale as dependências necessárias:

```bash
pip install -r requirements.txt
```

3. Copie o arquivo de exemplo para configurar suas variáveis de ambiente:

```bash
cp .env.example .env
# Ou no Windows: copy .env.example .env
```

4. Edite o arquivo `.env` gerado e adicione sua chave de API do Gemini:

```env
GEMINI_API_KEY=sua_chave_real_aqui
```

### Executando

Com o ambiente configurado e uma mesa de poker visível na tela (monitor principal ou secundário, dependendo da configuração do `mss` no código), execute:

```bash
python main.py
```

O script irá capturar a tela, enviar para a IA e imprimir a análise no terminal.

## 🛠️ Tecnologias Utilizadas

- **Python**: Linguagem principal.
- **MSS**: Para captura de tela ultra-rápida.
- **Google GenAI SDK**: Para comunicação com o modelo Gemini.
- **Dotenv**: Para gerenciamento de variáveis de ambiente.

## 📄 Estrutura dos Arquivos

- `main.py`: Script principal que captura a tela e chama a API.
- `prompt.txt`: Instruções enviadas para a IA sobre como analisar a imagem.
- `requirements.txt`: Lista de bibliotecas Python necessárias.

## ✅ Todo / Funcionalidades Futuras

- [ ] Otimizar tempo de resposta da IA (diminuir latência).
- [ ] Criar interface gráfica (Popup/Overlay) para exibir os resultados na tela.
